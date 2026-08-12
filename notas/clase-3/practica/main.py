"""
Url del curso: https://codigofacilito.com/curso-ia
Repositorio de notas: https://github.com/KrisbelGV/notas-ai-engineer-codigo-facilito
Fundamentos de Ingeniero de IA con Python de Código Facilito

Práctica previo a la Clase #3
Estudiante: KrisbelGV
"""

import os
import json
import csv
import requests
from dotenv import load_dotenv
from fastembed import TextEmbedding
import chromadb

load_dotenv()

def procesar_txt(nombre_archivo: str, prefix_id: str) -> list[dict]:
  chunks = []
  if not os.path.exists(nombre_archivo):
    return chunks

  with open(nombre_archivo, "r", encoding="utf-8") as f:
    contenido = f.read().strip()
    if contenido:
      parrafos = [p.strip() for p in contenido.split("\n\n") if p.strip()]
      for i, p in enumerate(parrafos):
        chunks.append({
          "id": f"{prefix_id}_p_{i}",
          "texto": p,
          "fuente": nombre_archivo
        })
  return chunks

def procesar_csv(nombre_archivo: str, prefix_id: str) -> list[dict]:
  chunks = []
  if not os.path.exists(nombre_archivo):
    return chunks

  with open(nombre_archivo, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, fila in enumerate(reader):
      texto_fila = ", ".join([f"{columna}: {valor}" for columna, valor in fila.items() if valor])
      chunks.append({
        "id": f"{prefix_id}_row_{i}",
        "texto": texto_fila,
        "fuente": nombre_archivo
      })
  return chunks

def procesar_json(nombre_archivo: str, prefix_id: str) -> list[dict]:
  chunks = []
  if not os.path.exists(nombre_archivo):
    return chunks

  with open(nombre_archivo, "r", encoding="utf-8") as f:
    contenido = f.read().strip()
    if contenido:
      try:
        data = json.loads(contenido)
        if isinstance(data, list):
          for i, elemento in enumerate(data):
            if isinstance(elemento, dict):
              texto_json = ", ".join([f"{clave}: {valor}" for clave, valor in elemento.items()])
            else:
              texto_json = str(elemento)
            chunks.append({
              "id": f"{prefix_id}_item_{i}",
              "texto": texto_json,
              "fuente": nombre_archivo
            })
        elif isinstance(data, dict):
          for clave, valor in data.items():
            texto_json = f"{clave}: {valor}"
            chunks.append({
              "id": f"{prefix_id}_{clave}",
              "texto": texto_json,
              "fuente": nombre_archivo
            })
      except Exception:
        pass
  return chunks

def cargar_chunks() -> list[dict]:
  chunks = []
  chunks.extend(procesar_txt("politicas_y_servicios.txt", "txt"))
  chunks.extend(procesar_csv("inventario_flores.csv", "csv"))
  chunks.extend(procesar_json("combos_y_promociones.json", "json"))
  return chunks

def inicializar_bd_vectorial(embedding_model):
  client = chromadb.PersistentClient(path="./vector_db_floristeria")
  coleccion = client.get_or_create_collection(name="floristeria")

  if coleccion.count() > 0:
    print("\nBase de datos vectorial detectada en disco. Reutilizando colección...")
    return coleccion

  print("\nIndexando base de conocimiento por primera vez...")
  chunks = cargar_chunks()

  for chunk in chunks:
    texto_limpio = str(chunk["texto"])
    vector = list(embedding_model.embed([texto_limpio]))[0].tolist()

    coleccion.upsert(
      ids=[chunk["id"]],
      embeddings=[vector],
      documents=[texto_limpio],
      metadatas=[{"fuente": chunk["fuente"]}]
    )

  print("Indexación completada.")
  return coleccion

def main():
  api_key = os.getenv("API_KEY")

  if not api_key:
    print("No fue posible obtener el valor para API_KEY")
    return

  ai_model = os.getenv("AI_MODEL")

  if not ai_model:
    print("No fue posible obtener el valor para AI_MODEL")
    return

  print("Cargando modelo local de embeddings y base de datos...")
  embedding_model = TextEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
  coleccion = inicializar_bd_vectorial(embedding_model)

  print("\n=======================================================")
  print("Bienvenid@ al chat de la floristeria 'Pétalos y Encantos'")
  print("=========================================================")
  print("\n¿En qué podemos ayudarte hoy?")

  while True:
    myinput = input("\nDescribe tu consulta: ")

    vector_pregunta = list(embedding_model.embed([myinput]))[0].tolist()
    resultados = coleccion.query(query_embeddings=[vector_pregunta], n_results=3)

    textos_recuperados = resultados.get("documents", [[]])[0]
    contexto = "".join(textos_recuperados)

    if not contexto.strip():
      print("Alerta: El contexto está vacío")

    system_instruction = f"""Eres un asistente de atención al cliente de la floristeria 'Pétalos y Encantos'.
    Responde a la solicitud del usuario utilizando ÚNICAMENTE la siguiente información recuperada de la base de datos local.
    Si la respuesta no se encuentra en el contexto, indica expresamente que no posees la información en la documentación. 

    CONTEXTO RECUPERADO DE LA BASE DE DATOS: {contexto}"""

    response = requests.post(
      url=f"https://generativelanguage.googleapis.com/v1/models/{ai_model}:generateContent?key={api_key}",
      headers={"Content-Type": "application/json"},
      json={
        "system_instruction": {"parts": [{"text": system_instruction}]},
        "contents": [{"parts": [{"text": myinput}]}]
      }
    )

    if response.status_code != 200:
      print(f"No fue posible completar la operación \n Error {response.status_code}: {response.text}")
      return

    candidates: list[dict] = response.json().get("candidates")
    content: dict = candidates[0].get("content")
    parts: list = content.get("parts")
    text = parts[0].get("text")
    print("Respuesta:\n", text)

    exit = input("\n¿Salir? S/N ")

    if exit == "S" or exit == "s":
      break

if __name__ == '__main__':
  main()