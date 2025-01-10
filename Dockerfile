ARG PYTHON_VERSION=3.12.7
FROM python:${PYTHON_VERSION}-slim AS base
WORKDIR /app
COPY requirements.txt .
COPY .env .env
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8083
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]

# FROM mysql:5.7

# # Copy file SQL untuk inisialisasi database
# COPY tangguhpos_auth.sql /docker-entrypoint-initdb.d/
