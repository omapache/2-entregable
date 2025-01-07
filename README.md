# Proyectos con Hugging Face Transformers

Este repositorio contiene tres proyectos que exploran diferentes aplicaciones de modelos de Transformers y su implementación tanto de manera local como mediante APIs de Hugging Face.

## Configuración del Token

Antes de ejecutar los proyectos, asegúrate de configurar correctamente tu token de Hugging Face. Para utilizar modelos a través de la API, es necesario:

1. Crear un token de acceso en tu cuenta de Hugging Face.
   - Ve a [Tu cuenta en Hugging Face](https://huggingface.co/settings/tokens) y genera un nuevo token con los permisos necesarios.
2. Agregar permisos específicos para el modelo que deseas usar.
   - Durante la configuración del token, asegúrate de incluir los modelos requeridos en la lista de permisos.

---

## Requisitos para la Ejecución

- **Python 3.7 o superior**
- **Librerías necesarias**:
  - `transformers`
  - `openai`
  - `torch`

Instala las dependencias necesarias con:

```bash
pip install transformers torch sentencepiece
```

---

## Proyecto 1: Análisis de Sentimientos

Este proyecto utiliza un modelo de análisis de sentimientos que se ejecuta localmente para clasificar texto en categorías como positivo, negativo o neutral.

### Detalles del Modelo Usado
- **Modelo**: nlptown/bert-base-multilingual-uncased-sentiment
- **Características**:
  - Multilingüe, con soporte para español.
  - Clasificación de sentimientos en cinco categorías.

### Implementación
1. Descarga del modelo utilizando la librería `transformers`.
2. Entrada del texto por parte del usuario.
3. Salida con la categoría del sentimiento y su puntuación.

### Ejemplo de Ejecución

```bash
python entregable.py
```
Cuando se solicite, ingresa el texto:
```text
Ingresa tu texto: "Me encanta este producto, es fantástico."

Salida: ES HAPPY (0.95)
```

---

## Proyecto 2: Aplicación de Preguntas y Respuestas (LLM)

Este proyecto utiliza una API de Hugging Face para implementar una aplicación donde el usuario puede realizar preguntas y obtener respuestas del modelo.

### Detalles del Modelo Usado
- **Modelo**: mistralai/Mistral-7B-Instruct-v0.2
- **Características**:
  - Modelo de lenguaje grande (7 mil millones de parámetros).
  - Optimizado para tareas basadas en instrucciones.
  - Soporte multilingüe.

### Implementación
1. Carga del modelo a través de la API de Hugging Face.
2. Generación de respuestas con temperatura 0.7 para balancear creatividad y coherencia.

### Ejemplo de Ejecución

```bash
python entregable1.py
```
Cuando se solicite, ingresa tu pregunta:
```text
Ingresa tu token: "hf_ASUJDHAJDHASJDH"

Ingresa tu pregunta: "¿Cuál es la capital de Francia?"
Respuesta: "The capital city of Spain is Madrid. Madrid is a vibrant and major cultural and political center of Spain. Its rich history and art, including the Prado Museum and the Royal Palace, attract millions of tourists every year. Madrid is also known for its numerous parks, wide tree-lined boulevards, and lively atmosphere, making it a popular destination for both domestic and international travelers."
```

---

## Proyecto 3: Generación de Imágenes a partir de Texto generado por una pregunta

Este proyecto utiliza una API de Hugging Face para implementar una aplicación que permite al usuario generar texto y crear imágenes basadas en ese texto.

### Modelos Implementados

1. **Generación de Texto**
   - **Modelo**: mistralai/Mistral-7B-Instruct-v0.2
   - **Tarea**: Responder preguntas y generar texto a partir de instrucciones.

2. **Generación de Imágenes**
   - **Modelo**: black-forest-labs/FLUX.1-dev
   - **Tarea**: Crear imágenes a partir de descripciones textuales.

### Implementación
1. Creación de una clase que cargue dinámicamente diferentes modelos.
2. Uso de métodos específicos para alternar entre tareas.
3. Entrada y salida configuradas según la tarea seleccionada.

### Ejemplo de Ejecución

Cuando se solicite, ingresa tu pregunta:
```text
Ingresa tu token: "hf_ASUJDHAJDHASJDH"

Ingresa tu pregunta: ¿Cuál es la capital de España?

Salida: "The capital city of Spain is Madrid. Madrid is a vibrant and major cultural and political center of Spain. Its rich history and art, including the Prado Museum and the Royal Palace, attract millions of tourists every year. Madrid is also known for its numerous parks, wide tree-lined boulevards, and lively atmosphere, making it a popular destination for both domestic and international travelers."

crea la imagen llamada : "imagen_generada" en base a ese texto generado*
```
---

## Ejecución Local y Aprendizajes sobre Transformers

### ¿Qué son los Transformers?
Lo que llamamos Transformers son arquitecturas de redes neuronales diseñadas para procesar secuencias, como texto o imágenes, con alta eficiencia. Destacan por:
- **Atención bidireccional**: Contexto más rico para tareas de lenguaje.
- **Procesamiento en paralelo**: Mayor velocidad frente a las RNNs tradicionales.

### Ventajas
- **Independencia**: No se necesita conexión a APIs externas.
- **Privacidad**: Los datos se procesan localmente.
- **Menor latencia**: Respuestas más rápidas.

### Desventajas
- **Recursos computacionales**: Algunos modelos son exigentes.
- **Configuración de hardware**: Se recomienda el uso de GPU para modelos grandes.


##
por Owen 🦝
![alt text](imagenFinal.jpg)
