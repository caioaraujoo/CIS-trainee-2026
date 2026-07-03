# Período 4 — Previsão de Churn (Telco Customer Churn)

## Objetivo

Modelo preditivo para identificar cancelamento de clientes (churn), com rastreamento organizado de experimentos, hiperparâmetros, métricas e artefatos via MLflow.

## Dataset

- **Fonte:** [Telco Customer Churn (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Conteúdo:** perfil de clientes, serviços assinados, dados financeiros e indicação de cancelamento (`Churn`)

## Ambiente

- **Python:** 3.12.9
- **Libs principais:** `mlflow`, `scikit-learn`, `pandas`, `numpy`, `matplotlib`

## Pipeline

1. **Pré-processamento** — tratamento de nulos em `TotalCharges`, One-Hot Encoding nas features categóricas, Label Encoding no alvo, padronização com `StandardScaler`.
2. **Modelagem e rastreamento** — `LogisticRegression` treinado com `train_all_models`, função implementada para automatizar o treino e comparação de modelos. Experimentos, hiperparâmetros e modelo final registrados via `mlflow` (`mlruns.db`).
3. **Avaliação** — métricas de Acurácia e ROC-AUC; curva ROC salva como artefato visual no MLflow.

## Como rodar

```bash
pip install -r requirements.txt
```

1. Baixe o dataset e coloque em `/data/` (ou na pasta do notebook).
2. Rode `telco_customer_churn1.ipynb` célula a célula para treinar o modelo e registrar o experimento.
3. Para ver os resultados: abra o terminal na pasta do notebook, execute `mlflow ui` e acesse `http://127.0.0.1:5000`.

## Observações

- A função `train_all_models` centraliza o treino de diferentes modelos, facilitando comparação de métricas entre execuções registradas no MLflow.
- O registro dos experimentos é local (`mlruns.db`); para reproduzir os resultados, é necessário rodar o notebook no mesmo diretório onde essa base será criada.