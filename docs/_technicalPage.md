# Neues Projekt

## Neues venv anlegen

python -m venv venv

## MkDocs + Material + watchdog installieren: 

pip install mkdocs-material watchdog

## MkDocs zwingen, watchdog zu verwenden

pip install watchdog[watchmedo]

# Neustart VS Code (existierendes Projekt)

## venv aktivieren  

venv\Scripts\activate.bat

## Server für Live-Reload starten
mkdocs serve --livereload

## proxy für ngrok starten
python proxy.py

## ngrok starten
ngrok start portfolio


