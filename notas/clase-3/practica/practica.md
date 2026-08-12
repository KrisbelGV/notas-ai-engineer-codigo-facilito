# Práctica: Creación de un Rag para Google AI Studio
> Script compartido por la alumna, NO forma parte de la clase ni el curso en general.

## Pasos requeridos:

* Instalar depedencias:
    * Python venv: `pip install fastembed chromadb`
    * UV: `uv add fastembed chromadb`
* Corta main.py, politicas_y_servicios.txt, inventario_flores.csv, combos_y_promociones.json al directorio correspondiente a entorno virtual (tambien necesitarás la api key y el [.env](../../clase-2/aistudio.env) con ese nombre exacto)
* Ejecutar:
    * Python venv: `python tuvenv/main.py`
    * UV: `uv run tuvenv/main.py`

## Contiene:
* Un chat enriquecido con la data de una floristeria ficticia
* Genera una BBDD vectorial en base a dicha información
* Extrae el contexto necesario y lo pasa al modelo
* SIN historial; solo responderá por pregunta