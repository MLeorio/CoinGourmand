# Coin Gourmand

## Introduction

Projet API de gestion de la patisserie Coin-Gourmand

## Use

```bash
# Activate your desired environment with
. venv/bin/activate
. source venv/Script/activate

# and run server
python manage.py runserver

```

## Installation


### Installer l'environnement

```
python -m venv venv 

. venv/bin/activate ou source venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Configurer la base de données

Le systeme utilise SQLite3 comme base de donnees. Plus de besoin de faire une installation tierce.
```bash
python manage.py migrate
```
