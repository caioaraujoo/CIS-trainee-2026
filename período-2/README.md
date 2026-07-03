# Período 2 — Classificação Estelar (Stellar Classification)

## Objetivo

Pipeline de ML para classificar corpos celestes (estrela, galáxia ou quasar) a partir de características espectrais, com tratamento de desbalanceamento de classes.

## Dataset

- **Fonte:** [Stellar Classification Dataset (Kaggle)](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17)
- **Conteúdo:** features numéricas espectrais + classe alvo (`Star`, `Galaxy`, `QSO`)

## Ambiente

- **Python:** 3.14.5
- **Libs principais:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `imbalanced-learn` (SMOTE)

## Pipeline

1. **Pré-processamento** — remoção de colunas identificadoras, `LabelEncoder` na variável alvo, `StandardScaler` nas features.
2. **Balanceamento** — `SMOTE` aplicado só no treino, antes do scaling (evita data leakage).
3. **Modelo** — `RandomForestClassifier`, avaliado com `classification_report` e matriz de confusão.

## Como rodar

```bash
pip install -r requirements.txt
```

1. Baixe o dataset e coloque `star_classification.csv` na mesma pasta do notebook (ou ajuste o path).
2. Rode `stellar_classification.ipynb` célula a célula.

## Observações

- SMOTE aplicado estritamente no treino, antes do scaling — decisão deliberada pra evitar vazamento de dados e manter o teste fiel à proporção real das classes.
- Tive dificuldades com o ambiente Python 3.14.5: problemas recorrentes de compatibilidade com o LangChain. Depois de identificar isso, passei a usar Python 3.12.9, que tinha suporte mais estável. Boa parte do notebook foi escrita já contornando esses erros de ambiente.