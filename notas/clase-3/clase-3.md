# Clase 3: Tu primer sistema RAG

## RAG
Retrieval-Augmented Generation (Generación Aumentada por Recuperación). Obtiene data específica previo a la generación de parte del modelo.

## BM25 vs Embedding
|               | Tipo                                  | Enfoque                    |
| ------------- |:-------------------------------------:|:--------------------------:|
| BM25          | Algoritmo de búsqueda                 | Léxico, palabras exactas   |
| Embedding     | Representaciones numéricas (vectores) | Semántico, por significado |

## Búsqueda hibrida
Combina BM25 y Embedding mejorando la exactitud de los resultados.

## Fine tuning vs RAG
|               | Ventaja                               | Desafíos                         |
| ------------- |:-------------------------------------:|:--------------------------------:|
| Fine tuning   | Modelo adaptado al caso especifico    | Costos, actualización continua   |
| RAG           | Brinda el conocimiento                | Integración segura               |

## Alternativas
* Prompt específico: Mejora en las instrucciones, calidad u cantidad de información.
* Few-shot: Se ofrecen ejemplos previos al modelo.
* Structured output: Establecimiento de un esquema.
* Context stuffing: Introduce el corpus completo.

## Proceso
1.	Chunking: Cargar, dividir y leer el resultado.
2.	Vectores: Codificar y guardar en la BBDD vectorial.
3.	Recuperación: Consulta a vectores similares. Se evalúa previo a generar.
4.	Generación: Ignora su conocimiento sobre el contexto, debe citar.

## Código de la clase
[Repositorio oficial](https://github.com/RamsesCamas/Mi-Primer-RAG) compartido por el instructor. No olvides dejar tu estrella ;)