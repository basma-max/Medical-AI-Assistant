import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Charger la clé API depuis .env
load_dotenv()  # Charge automatiquement le fichier .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Créez un fichier .env avec votre clé API")

# Configurer Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def analyser_image(image_path):
    try:
        img = Image.open(image_path)
        response = model.generate_content([
            "you are an experienced doctor. I will describe the symptoms of a patient. Analyze these symptoms, provide a possible diagnosis, briefly explain the illness and its likely causes, and recommend the next steps for treatment or advice. Be clear, precise, and use easy-to-understand language.In a pragraphe  ",
            img
        ])
        return response.text
    except Exception as e:
        return f"Erreur : {str(e)}"

# Test
if __name__ == "__main__":
    resultat = analyser_image("image/image.png")  # Remplacez par votre image
    print(resultat)