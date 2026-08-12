# Clase 1: Inauguración y el mapa del AI Engineer

## Ingeniero de IA
Integra modelos existentes en aplicaciones y productos diseñados de forma escalable y segura.

## Constitución de sistemas inteligentes
Prompt del sistema + Historial + RAG + Prompt del usuario + Respuesta

## Function calling
Generación del modelo de invocaciones de función y sus argumentos, definidos en el código, en formato JSON. NO lo ejecuta.

## RAG: Retrieval-Augmented Generation
Consultar información no existente en el modelo, de origen privado, para obtener una respuesta.

## Catching semántico
Guardado en caché de respuestas a consultas con similitudes, reduciendo la latencia.

## Fine tuning
Especializar un modelo al re-entrenarlo sobre un dataset específico.

## Agente
Sistema inteligente con mayor autonomía. Se compone de un modelo, su respectivo sistema de desiciones y herramientas subyacentes.

## Patrón de diseño ReAct
Reason -> Act -> Observe (Razonar -> Actuar -> Observar). Brinda autonomía y adaptabilidad a los sistemas de agentes.

## LangGraph
Framework de Python para sistemas multiagentes conectados mediante un grafo de estados.

## Patrones de orquestación
Supervisor-Worker, un agente principal deconstruye y delega tareas al resto; Hand-off, los agentes se transfieren el control entre ellos tras cumplir su objetivo.