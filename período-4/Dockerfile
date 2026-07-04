# Imagem base leve com Python
FROM python:3.12.9-slim
 
WORKDIR /app
 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
COPY app.py .
COPY modelo_api ./modelo_api
 
EXPOSE 8000
 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
 