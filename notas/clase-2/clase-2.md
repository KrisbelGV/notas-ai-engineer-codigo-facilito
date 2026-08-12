# Clase 2: Cómo consumir la API de OpenAI (O Google AI Studio).

* Preparación del entorno virtual (virtual environment):

    * Opcion A: Usando venv (módulo de Python):
        * Crear entorno virtual:
            * Windows: `python –m venv mivenv`
            * Linux/Mac: `python3 –m venv mivenv`
        > Si no funciona intenta repetir los pasos de instalación y asegurate de añadir la ruta al PATH
        * Activar:
            * Windows: `mivenv\Scripts\activate.bat`
            * Linux/Mac: `source mivenv/bin/activate`
        * Instalar dependencias: `pip install requests python-dotenv`
        * Comprobar dependencias: `pip freeze`
        * Ejecutar Script: `python mivenv/main.py`
        * Terminar: `deactivate`

    * Opcion B: Usando UV:
        * Instalar: `pip install uv`
        * Crear entorno virtual: `uv init mivenv`
        * Instalar dependencias: `uv add requests python-dotenv`
        * Ejecutar Script: `uv run mivenv/main.py`

* Ejecutar Script desde el nuevo entorno virtual:

    * Usa el [código de la clase](main.py) (escrito a mano, no oficial) siguiendo las instrucciones en el primer comentario para conectarte a la Api de OpenAI.
    * O alternativamente el que proporciono para [AI Studio](aistudio.py) de Google.  