# Trainee CIS 2026 — Repositório de Atividades

**Nome:** Caio de Castro Araujo
**Programa:** Trainee IEEE Computational Intelligence Society (CIS) — Universidade de Brasília

Este repositório centraliza todas as entregas e projetos práticos desenvolvidos durante o processo de Trainee da CIS. Cada período tem sua própria pasta com o notebook, o README específico e as instruções de execução.

## Estrutura do repositório

```
CIS-trainee-2026/
│
├── período-2/
│   ├── exemplo.ipynb
│   └── README.md
│
├── período-3/
│   ├── exemplo.ipynb
│   └── README.md
│
├── período-4/
│   ├── exemplo.ipynb
│   └── README.md
│
├── período-5/
│   ├── exemplo.ipynb
│   └── README.md
│
├── treinos/
│   └── README.md
│
├── .gitignore
└── README.md
```

## Sumário de períodos

| Período | Tema | Ambiente | Python |
|---|---|---|---|
| 1 | Não realizado — dispensado pela organização para este trainee | — | — |
| 2 | Redes Neurais Artificiais e Classificação Estelar | Local | 3.14.9 |
| 3 | Pipeline de RAG com wikipedia-PT | Local | 3.12.9 |
| 4 | MLOps — rastreamento de experimentos com MLflow | Local | 3.12.9 |
| 5 | Explainable AI (xAI) e interpretabilidade de modelos | Google Colab (trabalho em grupo) | Colab (padrão) |

Detalhes de cada período (dataset, decisões técnicas, como rodar) estão no README de cada pasta.

> **Nota sobre as versões de Python:** o período 2 foi feito em uma versão diferente dos demais (3.14.9) por conta de instabilidade no ambiente de desenvolvimento no momento da entrega. A partir do período 3 o ambiente foi padronizado em 3.12.9.

## `treinos/`

Pasta com exercícios e práticas avulsas, sem vínculo direto com a entrega de um período específico — usada para consolidar conceitos entre as atividades oficiais.

## Como rodar os notebooks

Como os datasets são pesados, eles não estão incluídos neste repositório.

1. Baixe o CSV do dataset original no Kaggle/HuggingFace — o link está no README de cada período.
2. Crie uma pasta `data/` na raiz do projeto e coloque o arquivo baixado dentro dela.
3. Abra o notebook do período desejado e rode as células em ordem.

```
CIS-trainee-2026/
│
├── data/                         <-- crie esta pasta
│   └── exemplo_banco_de_dados.csv
│
├── período-2/
│   └── exemplo.ipynb
...
```

## Tecnologias utilizadas

- Python
- Jupyter Notebook / VS Code
- Google Colab
- PyTorch
- Pandas
- Seaborn
- LangChain
- MLflow
