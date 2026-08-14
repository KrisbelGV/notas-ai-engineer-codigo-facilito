# Clase 4: Langchain, el framework de IA para desarrolladores

## Scripts (solo los enteramente abordados)

* Chat básico
    * Copia paso1_chat_basico.py en tu entorno virtual
    * Ejecutar:
        * Python venv: `python tuvenv/paso1_chat_basico.py`
        * UV: `uv run tuvenv/paso1_chat_basico.py`

* RAG con Ollama (para PDFs)
    * Copia paso5_rag_pdf.py en tu entorno virtual
    * Descarga e instala Ollama: https://ollama.com/download
    * Inicia Ollama: `ollama serve`
    * Descarga el modelo: `ollama run qwen3-v1:8b`
    > U otro de la familia o similares acorde tu hardware: https://ollama.com/library/qwen3-vl Solo asegurate de establecer su respectivo nombre como argumento, línea 30
    * Instalar depedencias:
        * Python venv: `pip install requests langchain_ollama langchain_core langchain_community langchain_chroma langchain_text_splitters`
        * UV: `uv add requests langchain_ollama langchain_core langchain_community langchain_chroma langchain_text_splitters`
    * Copia la carpeta "docs" a tu entorno virtual (pdf convertido del pptx de su [bootcamp correspondiente](https://github.com/RamsesCamas/Bootcamp_AI_Engineer_Codigofacilito/blob/main/slides/Clase-02/Clase2_Tokens_Contexto_Costo_Latencia.pptx))
    * Ejecutar:
        * Python venv: `python tuvenv/paso5_chat_basico`
        * UV: `uv run tuvenv/paso5_chat_basico.py`