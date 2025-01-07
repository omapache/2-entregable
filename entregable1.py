from openai import OpenAI

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
        max_tokens=500,
        temperature=0.7
    )
    
    respuesta = completion.choices[0].message.content
    return respuesta

def main():
    api_key = input("Ingresa tu token: ")
    pregunta = input("Ingresa tu pregunta: ")
    texto_generado = generar_texto(api_key, pregunta)

    print(f"Tu Respuesta: {texto_generado}")

if __name__ == "__main__":
    main()