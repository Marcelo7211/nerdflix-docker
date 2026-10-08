# Imagem da API: Python enxuto com o Flask
FROM python:3.12-slim

WORKDIR /app

# Dependências primeiro: o cache do Docker só refaz esta camada quando o requirements.txt muda
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
