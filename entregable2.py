import requests
from openai import OpenAI
import os

def generar_texto(api_key, pregunta):
    client = OpenAI(
        base_url="https://api-inference.huggingface.co/v1/",
        api_key=api_key
    )
    
    messages = [
        {
            "role": "user",
            "content": pregunta
        }
    ]
    
    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2", 
        messages=messages, 
        max_tokens=500
    )
    
    respuesta = completion.choices[0].message.content
    return respuesta

def generar_imagen(descripcion, api_key):
    url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"inputs": descripcion}
    for intento in range(5): 
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error al generar la imagen: {response.status_code} - {response.text}")
            return None
    return None

def main():
    api_key = input("Ingresa tu token: ")
    pregunta = input("Ingresa tu pregunta: ")
    texto_generado = generar_texto(api_key, pregunta)

    print(f"Texto generado: {texto_generado}")

    print("Generando imagen basada en el texto...")
    imagen = generar_imagen(texto_generado, api_key)

    if imagen:
        base_filename = "imagen_generada"
        extension = ".png"
        filename = base_filename + extension
        counter = 1
        
        while os.path.exists(filename):
            filename = f"{base_filename}_{counter}{extension}"
            counter += 1
        
        with open(filename, "wb") as f:
            f.write(imagen)
        print(f"Imagen generada y guardada como '{filename}'.")
    else:
        print("No se pudo generar la imagen.")

if __name__ == "__main__":
    main() 