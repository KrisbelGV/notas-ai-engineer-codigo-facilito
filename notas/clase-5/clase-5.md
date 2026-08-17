# Clase 5: Tu primer agente con Python

## Agente
Básicamente, un LLM en un bucle, con herramientas y un criterio de paro.

## Composición.
* Modelo: Al cual se disponen la pregunta y herramientas.
* Responde: Textualmente al usuario u realiza una solicitud a una herramienta.
* El historial: Incrementa en cada ciclo, añadidendo a una lista.
* La condición de parada: Respuesta al usuario u criterio propio.

## Características de las herramientas
* Deben ser descritas en el prompt.
* Brindan lo que el modelo no puede.
* Devuelven información, el modelo explica.
* El resultado va al historial como string.

## Límites de un agente
* Iteraciones: Evita reintentos interminables.
* Tokens: Reduce costos.
* Tiempo: No se "congela".

## Código
Repositorios oficiales:
* [Mi primer agente](https://github.com/RamsesCamas/Mi-Primer-Agente)
* [Mi primer agente deploy](https://github.com/RamsesCamas/Mi-Primer-Agente-Deploy)