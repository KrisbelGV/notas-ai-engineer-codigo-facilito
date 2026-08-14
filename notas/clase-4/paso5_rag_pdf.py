"""
Url del curso: https://codigofacilito.com/curso-ia
Notas de la clase: https://github.com/KrisbelGV/notas-ai-engineer-codigo-facilito
Fundamentos de Ingeniero de IA con Python de Código Facilito
Clase #4
Profesor: Ramses Camas
Estudiante: KrisbelGV

Copia no oficial ni testeada del Script
"""

import os
import requests
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough

try:
    r = requests.get("http://localhost:11434/api/tags", timeout=3)
    models = [m["name"] for m in r.json().get("models", [])]
    print(f"Ollama corriendo. Modelos disponibles: {', '.join(models)}")
except Exception:
    print("Ollama no está corriendo. Inícialo con: ollama serve")
    exit(1)

llm = ChatOllama(model="qwen3-v1:8b", temperature=0.7, num_predict=500)

PDF_PATH = os.path.join(os.path.dirname(__file__), "docs", "Clase2_Tokens_Contexto_Costo_Latencia.pdf")
if not os.path.exists(PDF_PATH):
    print(f"No se encontró el PDF en: {PDF_PATH}")
    print("Asegúrate de que el archivo esté en la carpeta docs/")
    exit(1)

print()
print("=" * 60)
print("PASO 5: RAG con PDF - Chat con documentos reales")
print("=" * 60)

print(f"\nCargando PDF: {os.path.basename(PDF_PATH)}")
loader = PyPDFLoader(PDF_PATH)
pages = loader.load()
print(f"Páginas cargadas: {len(pages)}")
print(f"Primera página (preview): {pages[0].page_content[:150].strip()}...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", ",", " "],
)

chunks = text_splitter.split_documents(pages)
print(f"\nChunks generados: {len(chunks)}")
print(f"Tamaño promedio: {sum(len(c.page_content) for c in chunks) // len(chunks)} caracteres")


print("\nGenerando embeddings (esto puede tomar unos segundos)...")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="pdf_clase2",
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4},
)

print(f"Vector store creado con {len(chunks)} vectores")

rag_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Eres un asistente experto que responde preguntas basándote en el contenido "
     "de un documento PDF sobre Tokens, Contexto, Costo y Latencia en LLMs. "
     "Responde SOLO con información del contexto proporcionado. "
     "Si la información no está en el contexto, dilo claramente. "
     "Responde en español.\n\n"
     "Contexto del documento:\n{context}"),
    ("human", "{question}"),
])

def format_docs(docs):
    """Formatea los documentos recuperados como texto."""
    return "\n\n".join(
        f"[Página {doc.metadata.get('page', '?') + 1}]\n{doc.page_content.strip()}"
        for doc in docs
    )

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | rag_prompt
    | llm
    | StrOutputParser()
)

preguntas = [
    "¿Qué son los tokens en el contexto de los LLMs?",
    "¿Cómo afecta el tamaño del contexto al costo?",
    "¿Qué es la latencia y cómo se relaciona con los tokens?",
]

print("\nRAG con PDF en acción:")
print("-" * 50)

for pregunta in preguntas:
    print(f"\nPregunta: {pregunta}")
    respuesta = rag_chain.invoke(pregunta)
    print(f"IA: {respuesta}")

print("\n" + "-" * 50)
print("Ejemplo con streaming:")
pregunta_stream = "Resume los puntos principales del documento."
print(f"\nPregunta {pregunta_stream}")
print("IA: ", end="")
for chunk in rag_chain.stream(pregunta_stream):
    print(chunk, end="", flush=True)
print("\n")

vectorstore.delete_collection()

print("\nPaso 5 completado!")
print("(ARCHIVO NO EXISTENTE) Siguiente paso: ejecuta 'streamlit run app.py' para la interfaz web de chat")