import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
 
CAMINHO_LOCAL = "../modelo_api"
CAMINHO_DOCKER = "./modelo_api"
CAMINHO_MODELO = CAMINHO_DOCKER if os.path.exists(CAMINHO_DOCKER) else CAMINHO_LOCAL
 
modelo = joblib.load(f"{CAMINHO_MODELO}/modelo.pkl")
scaler = joblib.load(f"{CAMINHO_MODELO}/scaler.pkl")
colunas_treino = joblib.load(f"{CAMINHO_MODELO}/colunas_treino.pkl")
 
app = FastAPI(title="API de Previsão de Churn - Telco")
 
class Cliente(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float
 
 
@app.get("/")
def raiz():
    return {"status": "API de churn no ar. Veja /docs para testar."}
 
 
@app.post("/predict")
def prever(cliente: Cliente):
    # Transforma o cliente recebido em uma linha de DataFrame,
    dados = pd.DataFrame([cliente.dict()])
 
    # Aplica o mesmo One-Hot Encoding usado no treino.
    dados_codificados = pd.get_dummies(dados)
 
    # colunas que não apareceram nesse cliente específico são preenchidas com 0,
    # e a ordem das colunas é ajustada pra bater com o que o modelo espera.
    dados_alinhados = dados_codificados.reindex(columns=colunas_treino, fill_value=0)
 
    dados_escalados = scaler.transform(dados_alinhados)
 
    # Faz a previsão.
    probabilidade_churn = modelo.predict_proba(dados_escalados)[0][1]
    vai_cancelar = bool(probabilidade_churn >= 0.5)
 
    return {
        "probabilidade_churn": round(float(probabilidade_churn), 4),
        "vai_cancelar": vai_cancelar
    }
