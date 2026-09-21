#!/bin/bash
set -e

export PATH="$HOME/.local/bin:$PATH"

PROJECT_DIR="/var/www/consultor"

echo "Entrando al proyecto..."
cd "$PROJECT_DIR"

echo "Instalando dependencias..."
uv sync

echo "Aplicando migraciones..."
uv run python manage.py migrate

echo "Recolectando archivos estáticos..."
uv run python manage.py collectstatic --noinput

echo "Reiniciando Uvicorn..."
sudo systemctl restart consultor

echo "Deploy completado correctamente."