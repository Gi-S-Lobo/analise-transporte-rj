"""Gera as figuras do artigo a partir do CSV produzido pelo ETL."""
import matplotlib.pyplot as plt
import pandas as pd

from .etl import MODAIS, OUTPUT, ROOT

ASSETS = ROOT / "docs/assets"
CORES = ["#005c63", "#167882", "#334775", "#94532e", "#526c40", "#83567a"]


def gerar(dados):
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(3, 2, figsize=(9, 8), layout="constrained", sharex=True)
    for eixo, (campo, nome), cor in zip(axes.flat, MODAIS.items(), CORES):
        eixo.plot(dados.index, dados[campo] / 1000, color=cor, lw=2)
        eixo.set_title(nome, loc="left", weight="bold")
        eixo.set_ylim(bottom=0)
        eixo.set_xticks([1995, 2005, 2015, 2025])
        eixo.grid(axis="y", alpha=.2)
    fig.supylabel("Milhões de passageiros por ano")
    fig.savefig(ASSETS / "series.png", dpi=175, bbox_inches="tight")
    plt.close(fig)
    indices = dados.loc[[2020, 2025]].div(dados.loc[2019]).mul(100).T
    indices.index = MODAIS.values()
    eixo = indices.plot.barh(color=["#879ab2", "#005c63"], figsize=(8, 4), width=.75)
    eixo.axvline(100, color="#222", linestyle="--", lw=1)
    eixo.set_xlabel("Índice de movimento (2019 = 100)")
    eixo.legend(title="Ano")
    eixo.figure.tight_layout()
    eixo.figure.savefig(ASSETS / "retomada.png", dpi=175, bbox_inches="tight")
    plt.close(eixo.figure)


if __name__ == "__main__":
    gerar(pd.read_csv(OUTPUT, index_col="ano"))
