# Utilise Python stable (pas encore 3.13)
FROM python:3.12-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le code
COPY ./app /app

# Copier requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Lancer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
