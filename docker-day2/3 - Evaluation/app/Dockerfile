# Image de base Python
FROM python:3.11-slim

# Métadonnées
LABEL maintainer="student@docker.com"
LABEL version="1.0"

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Exposer le port
EXPOSE 5000

# Variables d'environnement par défaut
ENV ENVIRONMENT=production
ENV FLASK_APP=app.py

# Créer un utilisateur non-root pour la sécurité (bonne pratique)
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Commande de démarrage
CMD ["python", "app.py"]