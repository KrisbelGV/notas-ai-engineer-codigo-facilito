"""
Url del curso: https://codigofacilito.com/curso-ia
Notas de la clase: Notas de la clase: https://github.com/KrisbelGV/notas-ia-engineer-codigo-facilito/notas/clase-2/clase-2.md
Fundamentos de Ingeniero de IA con Python de Código Facilito
Clase #2
Profesor: Eduardo Ismael Garcia
Estudiante: KrisbelGV

Copia no oficial ni testeada del Script 

Pasos para obtener la api key de OpenAI:
1. Ir a: https://developers.openai.com/api/docs/quickstart?language=python
2. Seleccionar "Create a Api Key"
3. Completar los datos de registro (si no posee una cuenta)
4. Seleccionar "Create new secret key"
5. Asignarle un nombre
6. Selecionar "Create secret key"
7. Copiar y pegar en el archivo openai.env a continuación de OPEN_API_KEY entre las comillas simples
8. Cambia el nombre del archivo openai.env a solo .env
9. Corta main.py y .env al directorio correspondiente en tu entorno virtual

Asegurate de correr este Script en el entorno virtual con las dependencias indicadas en el archivo de la clase
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPEN_API_ENDPOINT = "https://api.openai.com/v1/responses"

def main():
  open_api_key = os.getenv("OPEN_API_KEY")

  if not open_api_key:
    print("No fue posible obtener el valor para OPEN_API_KEY")
    return

  open_model = os.getenv("OPEN_API_MODEL")

  if not open_model:
    print("No fue posible obtener el valor para OPEN_API_MODEL")
    return

  response = requests.post(
    url=OPEN_API_ENDPOINT,
    headers={
      "Authorization": f"Bearer {open_api_key}",
      "Content-Type": "application/json"
    },
    json={
      "model": open_model,
      "instructions": "You are a senior developer",
      "input": "Can you explain to me about docker?"
    }
  )

  if response.status_code != 200:
    print(f">>> No fue posible completar la operación")
    return
  
  payload: dict = response.json()
  output: list[dict] = payload.get("output")
  message: dict = output[1]
  content: list[dict] = message.get("content")
  text: str = content[0].get("text")

  print(text)

if __name__ == '__main__':
    main()