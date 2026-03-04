# Image de python avec uv inclus

FROM ghcr.io/astral-sh/uv:python3.12-alpine

# # 1. Image de base officielle Python Slim
# FROM python:3.11-slim

# # 2. On récupère le binaire 'uv' depuis l'image officielle d'Astral
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 4. Optimisation : on ne crée pas de fichiers .pyc et on force l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copie des fichiers de lock
COPY pyproject.toml uv.lock ./

# Installation : ON EXCLUT LES DEVS DEPENDENCIES ICI 
RUN uv sync --frozen --no-dev --no-cache

COPY . .

EXPOSE 5000

# Petit test rapide pour vérifier que pandas est là
CMD ["uv", "run", "python", "-m", "app.main"]