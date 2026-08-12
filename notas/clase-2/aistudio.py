"""
Url del curso: https://codigofacilito.com/curso-ia
Notas de la clase: https://github.com/KrisbelGV/notas-ai-engineer-codigo-facilito/blob/main/notas/clase-2/clase-2.md
Fundamentos de Ingeniero de IA con Python de Código Facilito
Clase #2
Profesor: Eduardo Ismael Garcia
Estudiante: KrisbelGV

Copia no oficial del Script adaptada para Google AI Studio

Pasos para obtener la api key:
1. Ir a: https://aistudio.google.com/
2. Completar los datos de registro (si no posee una cuenta)
4. Ve a Dashboard, Claves de api, Crear clave de api
5. Asignarle un nombre
6. Selecionar "Crear nueva clave"
7. Copiar y pegar en el archivo aistudio.env a continuación de API_KEY entre las comillas simples
8. Cambia el nombre del archivo aistudio.env a solo .env
9. Cambia el nombre del archivo aistudio.py a main.py
10. Corta main.py y .env al directorio correspondiente en tu entorno virtual

Asegurate de correr este Script en el entorno virtual con las dependencias indicadas en el archivo de la clase
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def main():
  api_key = os.getenv("API_KEY")

  if not api_key:
    print("No fue posible obtener el valor de la API_KEY")
    return

  ai_model = os.getenv("AI_MODEL")

  if not ai_model:
    print("No fue posible obtener el valor para AI_MODEL")
    return

  print("\n=================")
  print("Bienvenid@ al chat")
  print("===================")

  while True:

    instructions = input("\nDefine un rol: ")
    myinput = input("Solicitud: ")

    response = requests.post(
      url=f"https://generativelanguage.googleapis.com/v1/models/{ai_model}:generateContent?key={api_key}",
      headers={"Content-Type": "application/json"},
      json={
        "system_instruction": {"parts": [{"text": instructions}]},
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
