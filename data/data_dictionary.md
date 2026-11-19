# Dicionário da Tabela 440

**Origem** · [Data.Rio, Tabela 440](https://www.data.rio/documents/5d5849bf28bf4f689214f890e3f4ac04/about)  
**Cobertura** · Município do Rio de Janeiro, 1995–2025. Uma linha por ano.  
**Entrada** · XLS binário, aba `T 440`, cabeçalho hierárquico.  
**Saída** · CSV.GZ em UTF-8, vírgula entre campos, ponto decimal e campo vazio para ausências. Tipos abaixo são os usados pelo ETL.

| Campo | Tipo | Unidade | Descrição e tratamento |
|---|---|---|---|
| ano | int64 | AAAA | Ano de referência. Chave única. A rotina verifica a sequência anual. |
| onibus | float64 | mil passageiros | Movimento anual — Ônibus. Valor numérico preservado na unidade de origem. |
| metro | float64 | mil passageiros | Movimento anual — Metrô. Valor numérico preservado na unidade de origem. |
| trem | float64 | mil passageiros | Movimento anual — Trem. Valor numérico preservado na unidade de origem. |
| bonde | float64 | mil passageiros | Movimento anual — Bonde. O símbolo `...` torna-se ausente em 2012–2014. |
| hidroviario | float64 | mil passageiros | Movimento anual — Hidroviário. Valor numérico preservado na unidade de origem. |
| aeroviario | float64 | mil passageiros | Movimento anual — Aeroviário. Valor numérico preservado na unidade de origem. |

## Notas e proveniência

O rodapé da planilha credita SMTU, RIOÔNIBUS, Metrô-RJ, Opportrans/Metrô Rio, Flumitrens, SuperVia, TRANSTUR, Barcas S.A., CONERJ e INFRAERO. Vans e kombis não foram contempladas. O serviço de bondes de Santa Teresa foi interrompido em agosto de 2011 e retomado em julho de 2015. O sinal `...` significa dado numérico indisponível. Os anos de interrupção e retomada podem refletir operação parcial.

**Integridade do original (SHA-256)** · `64fa5f8894fae1e3d4a3af976e889957f9c406e5c180e9aee6f26040fad366e0`.

**Métricas da análise** · Milhões = valor original ÷ 1.000. Participação (%) = 100 × modal ÷ soma dos seis modais no mesmo ano, somente com seis observações válidas. Índice (2019 = 100) = 100 × volume no ano ÷ volume em 2019. Variação (%) = índice − 100. Contagens anuais agregadas não distinguem usuários únicos.

**Reuso da base** · Atribuir o Data.Rio e os provedores originais. A edição XLS não especifica licença. Consultar as condições do portal antes de redistribuir.

## Cuidados na interpretação e comparabilidade

- **Universo observado:** as seis séries da Tabela 440 são recortes por sistema de transporte, e sua soma não corresponde automaticamente a todas as viagens urbanas do município. A fonte não cobre vans e kombis e não apresenta uma série específica de BRT.
- **Contagem de movimentos:** os volumes não representam pessoas únicas; uma pessoa pode aparecer mais de uma vez ao realizar diferentes deslocamentos ou utilizar serviços distintos.
- **Ausências:** o campo `bonde` não tem informação numérica em 2012–2014. O valor ausente é preservado como `NaN`; não significa movimento zero. O cálculo das participações exige seis registros válidos, deixando de fora esses três anos.
- **Dois tipos de indicador:** a participação (pontos percentuais) compara um modal com a soma dos seis; a variação frente a 2019 (percentual) compara cada modal com seu próprio valor naquele ano. São métricas distintas e não devem ser confundidas.
- **Limites causais:** a granularidade anual não inclui informações sobre oferta, tarifa, integração, capacidade, bairros ou trajetos. A coincidência de picos ou quedas com inaugurações, alterações contratuais ou pandemia não estabelece causalidade.

Para o contexto documental, consulte a seção *Resultados e discussão* do artigo em `docs/index.html`, com bibliografia em estilo APA.
