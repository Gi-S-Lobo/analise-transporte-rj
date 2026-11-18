"""Preparação da Tabela 440 do Data.Rio (passageiros em milhares)."""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/440.xls"
OUTPUT = ROOT / "data/processed/movimento_passageiros_rio.csv.gz"
MODAIS = {"onibus": "Ônibus", "metro": "Metrô", "trem": "Trem", "bonde": "Bonde",
          "hidroviario": "Hidroviário", "aeroviario": "Aeroviário"}


def ler_tabela(arquivo=RAW):
    fonte = pd.read_excel(arquivo, sheet_name="T 440", header=None, engine="xlrd")
    if list(fonte.iloc[6, 1:5]) != list(MODAIS.values())[:4]:
        raise ValueError("Cabeçalho da tabela de origem mudou.")
    anos = pd.to_numeric(fonte.iloc[:, 0], errors="coerce")
    dados = fonte.loc[anos.notna()].copy()
    dados.columns = ["ano", *MODAIS]
    if sorted(dados.ano.tolist()) != list(range(1995, 2026)):
        raise ValueError("Verifique anos ausentes, duplicados ou fora da edição 1995–2025.")
    dados.ano = dados.ano.astype(int)
    for coluna in MODAIS:
        valores = dados[coluna].mask(dados[coluna].eq("..."))
        dados[coluna] = pd.to_numeric(valores, errors="raise").astype(float)
        if dados[coluna].lt(0).any():
            raise ValueError(f"Movimento negativo em {coluna}")
    return dados.sort_values("ano").reset_index(drop=True)


def executar():
    dados = ler_tabela()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    dados.to_csv(OUTPUT, index=False, compression={"method": "gzip", "mtime": 0})
    print(f"{len(dados)} anos · {dados[list(MODAIS)].isna().sum().sum()} valores ausentes · {OUTPUT.name}")


if __name__ == "__main__":
    executar()
