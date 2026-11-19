# analise-transporte-rj

**Movimento de passageiros no município do Rio de Janeiro, 1995–2025**

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue) ![Código MIT](https://img.shields.io/badge/código-MIT-green)

**Autores** · Giovanna Sigette Lobo e Theo Cubas Reis  
**Orientador** · Alexandre Neves Louzada  
**Filiação** · Centro Universitário La Salle do Rio de Janeiro (UniLaSalle-RJ) · Sistemas de Informação · 6º período · 2026.2  
**Disciplina** · Linguagem de Programação (Análise e Visualização de Dados com Python)

## Resumo executivo

Este artigo analisa a evolução do movimento anual de passageiros de seis modais registrados na Tabela 440 do Data.Rio, no município do Rio de Janeiro, entre 1995 e 2025. A pesquisa busca descrever as trajetórias de demanda, a composição do movimento observado e a recuperação frente a 2019. Os dados oficiais foram processados em Python, com verificação de 31 anos, tratamento de três observações ausentes do bonde e construção de indicadores de participação e variação relativa. Os ônibus mantiveram o maior volume, mas sua participação entre os seis modais caiu de 84,7% (1995) para 68,1% (2025); a parcela do metrô passou de 6,0% para 18,9%. Em 2020, todos os modais registraram contração em relação a 2019. Em 2025, apenas o bonde (+72,8%) e o aeroviário (+7,7%) superavam os respectivos volumes de 2019, embora o bonde representasse somente 0,07% do total observado. Eventos como a expansão dos corredores de transporte e as mudanças operacionais fornecem contexto, mas a série agregada não permite atribuir causas às oscilações. Os resultados indicam recuperação heterogênea e recomendam análises complementares de oferta, tarifas e distribuição territorial.

**Palavras-chave** · Mobilidade urbana, transporte de passageiros, Rio de Janeiro, séries temporais, dados abertos.

## Perguntas e resultados

1. **RQ1 — Evolução:** como variou o volume anual em cada modal?
2. **RQ2 — Composição:** como se alterou a participação de cada modal na soma dos seis sistemas observados entre 1995 e 2025?
3. **RQ3 — Recuperação:** quais modais superaram em 2025 o próprio volume de 2019 após a queda de 2020?

As duas primeiras colunas numéricas representam a participação na **soma dos seis modais cobertos pela Tabela 440**, não em todas as viagens do Rio. As duas últimas medem a variação percentual frente a 2019. O KPI principal é a participação dos ônibus nessa soma, calculada apenas para anos com os seis registros válidos.

| Modal | 1995 (%) | 2025 (%) | 2020 vs. 2019 (%) | 2025 vs. 2019 (%) |
|---|---|---|---|---|
| Ônibus | 84,7 | 68,1 | -45,1 | -33,3 |
| Metrô | 6,0 | 18,9 | -52,9 | -25,8 |
| Trem | 7,0 | 9,1 | -40,2 | -45,3 |
| Bonde | 0,01 | 0,07 | -66,7 | 72,8 |
| Hidroviário | 1,8 | 1,4 | -58,4 | -34,3 |
| Aeroviário | 0,5 | 2,5 | -57,0 | 7,7 |

> **Interpretação:** o bonde é exibido com duas casas decimais para não arredondar sua participação a zero. Os resultados foram calculados a partir dos 31 anos da base (1995–2025); em 2012–2014, o bonde está ausente, de modo que a composição conjunta daqueles anos não é calculada.

## Contextualização e discussão

A expansão do metrô, incluindo a Linha 4 em 2016 ([MetrôRio](https://metrorio.com.br/25anos)), e a implantação dos corredores BRT Transoeste, Transcarioca e Transolímpica ([Prefeitura do Rio — Legado Olímpico](https://prefeitura-rio.github.io/LegadoOlimpico2/)) compõem o contexto de transformação da infraestrutura urbana. O [histórico do bonde de Santa Teresa](https://cbn.globoradio.globo.com/institucional/historia/aniversario/cbn-25-anos/boletins/2016/07/21/2011-BONDINHO-DE-SANTA-TERESA-TOMBA-E-DEIXA-SEIS-MORTOS.htm?v=classica) documenta a interrupção em 2011 e a retomada parcial em 2015. A [Organização Mundial da Saúde](https://www.who.int/news-room/speeches/item/who-director-general-s-opening-remarks-at-the-media-briefing-on-covid-19---11-march-2020) registrou a pandemia de COVID-19 em 2020; em 2022, a [Secretaria Municipal de Transportes](https://transportes.prefeitura.rio/noticias/prefeitura-do-rio-assina-acordo-judicial-para-a-melhoria-do-transporte-feito-por-onibus-na-cidade/) documentou um acordo de reorganização e subsídios para os ônibus.

Esses eventos **oferecem contexto**, mas não são causas comprovadas das variações de volume. Como indica a literatura sobre [deslocamentos pendulares metropolitanos](https://doi.org/10.1590/2236-9996.2023-5711), fatores territoriais e sociais exigem outros dados para uma interpretação explicativa.

### Conclusões para as três perguntas

- **RQ1:** os ônibus mantiveram o maior volume anual da série; o metrô apresentou crescimento em termos absolutos entre os extremos do período.
- **RQ2:** a participação dos ônibus nos seis sistemas caiu de 84,7% para 68,1% (−16,6 pontos percentuais), enquanto a do metrô passou de 6,0% para 18,9% (+12,9 p.p.).
- **RQ3:** em 2025, apenas o bonde e o aeroviário haviam ultrapassado seus volumes de 2019; o trem estava 45,3% abaixo.

O artigo apresenta a discussão detalhada e as **nove referências bibliográficas organizadas no padrão APA**, enquanto o notebook documenta a EDA, os cálculos e suas limitações.

## Fonte e acesso

A [Tabela 440 do Data.Rio](https://www.data.rio/documents/5d5849bf28bf4f689214f890e3f4ac04/about) reúne dados de operadores e órgãos de transporte. O arquivo bruto está em [data/raw/440.xls](data/raw/440.xls). A aba analisada é `T 440`. Cada linha corresponde a um ano do município do Rio de Janeiro. Vans e kombis estão fora da cobertura. Consulte as unidades, as lacunas e os créditos no [dicionário de dados](data/data_dictionary.md).

[Artigo acadêmico em HTML](docs/index.html) · [Notebook de análise](notebooks/analise_exploratoria.ipynb) · [Base tratada em CSV.GZ](data/processed/movimento_passageiros_rio.csv.gz)

## Estrutura do repositório

```text
analise-transporte-rj/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/440.xls
│   ├── processed/movimento_passageiros_rio.csv.gz
│   └── data_dictionary.md
├── notebooks/analise_exploratoria.ipynb
├── src/
│   ├── __init__.py
│   ├── etl.py
│   └── figuras.py
└── docs/
    ├── index.html
    └── assets/
        ├── series.png
        └── retomada.png
```

## Reprodução

Extraia o ZIP e abra o terminal na pasta que contém este README. Para obter uma cópia a partir do repositório publicado, copie a URL HTTPS no botão **Code** do GitHub e use `git clone URL_COPIADA` seguido de `cd analise-transporte-rj`.

Com Python 3.12, crie o ambiente com `python -m venv .venv`. Ative com `source .venv/bin/activate` em Linux/macOS ou `.\.venv\Scripts\Activate.ps1` em PowerShell. Execute na raiz:

```bash
python -m pip install -r requirements.txt
python -m src.etl
python -m src.figuras
python -m http.server 8000 --directory docs
```

Abra http://localhost:8000 para ler o artigo. O primeiro módulo lê o XLS e grava 31 linhas em CSV comprimido com cabeçalho UTF-8. O segundo refaz as duas figuras. A tabela do artigo corresponde à edição 1995–2025. Para abrir o notebook localmente no mesmo ambiente, instale a interface com `python -m pip install jupyterlab==4.4.10` e execute `python -m jupyterlab notebooks/analise_exploratoria.ipynb`. Execute as células em ordem a partir da raiz ou da pasta `notebooks`.

## Publicação no GitHub Pages

Envie o conteúdo da pasta do projeto para a raiz de um repositório público chamado `analise-transporte-rj`. Em **Settings → Pages → Build and deployment**, selecione **Deploy from a branch**, branch **main**, pasta **/docs** e salve. O endereço público aparecerá nessa mesma tela após a publicação. O artigo identifica o repositório a partir do endereço padrão do GitHub Pages.

## Reutilização e limites

O [código usa a licença MIT](LICENSE). Para o texto e as figuras de autoria da dupla, aplica-se [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), com atribuição aos autores e à fonte. Para os dados originais e seus valores derivados, consulte as condições do provedor. A planilha anexada não informa uma licença específica. Os totais medem movimento de passageiros e podem contar a mesma pessoa em diferentes viagens ou modais. A fonte não é um censo de todas as viagens urbanas, não cobre vans e kombis, não informa passageiros únicos e não separa BRT em uma série independente. O conjunto anual tampouco permite inferir causalidade entre alterações de infraestrutura, pandemia ou decisões tarifárias e os volumes observados.
