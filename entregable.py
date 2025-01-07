from transformers import pipeline
import torch

class AnalizadorSentimientos:
    def __init__(self):
        self.modelo = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            device=-1 if not torch.cuda.is_available() else 0
        )
    
    def analizar_texto(self, texto):
        resultado = self.modelo(texto)[0]
        puntuacion = int(resultado['label'][0])
        
        if puntuacion >= 4:
            sentimiento = "ES HAPPY"
        elif puntuacion <= 2:
            sentimiento = "ES SAD"
        else:
            sentimiento = "NI BIEN NI MAL"
            
        return sentimiento, puntuacion/5

def main():
    print("=== Analizador de Sentimientos ===")
    print("Inicializando modelo... (puede tardar unos segundos en la primera ejecución)")
    
    analizador = AnalizadorSentimientos()
    
    while True:
        texto = input("\nIngresa el texto a analizar (o '0' para salir): ")
        
        if texto.lower() == '0':
            break
            
        sentimiento, puntuacion = analizador.analizar_texto(texto)
        print(f"Resultado: {sentimiento} (confianza: {puntuacion:.2f})")

if __name__ == "__main__":
    main()