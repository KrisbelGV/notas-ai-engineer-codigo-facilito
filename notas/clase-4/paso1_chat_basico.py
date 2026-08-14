"""
Url del curso: https://codigofacilito.com/curso-ia
Notas de la clase: https://github.com/KrisbelGV/notas-ai-engineer-codigo-facilito
Fundamentos de Ingeniero de IA con Python de Código Facilito
Clase #4
Profesor: Ramses Camas
Estudiante: KrisbelGV

Copia no oficial del Script
"""

import re
import requests
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

try:
    r = requests.get("http://localhost:11434/api/tags", timeout=3)
    models = [m["name"] for m in r.json().get("models", [])]
    print(f"Ollama corriendo. Modelos disponibles: {', '.join(models)}")
    if not any("qwen3-vl" in m for m in models):
        print("qwen3-vl no encontrado. Ejecuta ollama pull qwen3-vl")
except Exception:
    print("Ollama no está corriendo. Inicialo con: ollama serve")
    print("Y descarga el modelo con: ollama pull qwen3-vl")
    exit(1)

print()
print("=" * 60)
print("PASO 1: Chat Interactivo con Ollama")
print("=" * 60)

llm = ChatOllama(
    model="qwen3-vl:8b",
    temperature=0.7,
    num_predict=2048
)

def strip_thinking(text: str) -> str:
    cleaned = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()
    if cleaned:
        return cleaned
    cleaned = re.sub(r"<think>.*", "", text, flags=re.DOTALL).strip()
    return cleaned if cleaned else text.strip

history = [
    SystemMessage(content="Eres un asistente técnico experto en programación. "
                  "Responde en español y de forma concisa."),
]

print("\n Chat iniciado. Escribe tu mensaje (o 'salir' para terminar).")
print(" El modelo recuerda el contexto de la conversación \n")

while True:
    user_input = input("Tú: ").strip()
    if not user_input:
        continue
    if user_input.lower() in ("salir", "exit", "quit"):
        print("¡Hasta luego!")
        break

    history.append(HumanMessage(content=user_input))

    print("IA: ", end="", flush=True)
    full_response=""
    thinking_done = False
    for chunk in llm.stream(history):
        full_response += chunk.content
        if not thinking_done:
            if "<think>" in full_response:
                thinking_done = True
                after_think = full_response.split("<think>", 1)[1].lstrip()
                print(after_think, end="", flush=True)
            elif "<think>" not in full_response:
                thinking_done = True
                print(full_response, end="", flush=True)
        else:
            print(chunk.content, end="", flush=True)
    print()

    clean_response = strip_thinking(full_response)

    history.append(AIMessage(content=clean_response))

print("\n ¡Paso 1 completado!")