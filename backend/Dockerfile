FROM python:3.10-slim

WORKDIR /app/backend

# Installation des dépendances systèmes nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie des requirements et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du projet
COPY . .

# Exposition du port
EXPOSE 8000

# Command pour lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


