# 1. Imagem base leve
FROM python:3.13.5-slim

# 2. Define diretório de trabalho
WORKDIR /app

# 3. Evita pyc e buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Copia e instala dependências
COPY pyproject.toml poetry.lock /app/
RUN pip install "poetry" && poetry config virtualenvs.create false \
    && poetry install --no-interaction --without dev --no-root

# 5. Copia o código
COPY . .

# 6. Comando padrão ao iniciar
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]