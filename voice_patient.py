import logging
import speech_recognition as sr
import os
from groq import Groq

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enregistrer_audio(output_path="enregistrement.wav", duree_max=30):
    """Enregistre l'audio depuis le microphone et le sauvegarde en WAV."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Ajustement au bruit ambiant...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            logging.info("Parlez maintenant (durée max : %ds)...", duree_max)
            audio = recognizer.listen(source, timeout=duree_max, phrase_time_limit=duree_max)
            
            with open(output_path, "wb") as f:
                f.write(audio.get_wav_data())
            
            logging.info(f"✅ Enregistrement sauvegardé sous : {os.path.abspath(output_path)}")
            return output_path

    except sr.WaitTimeoutError:
        logging.warning("⏱️ Aucun son détecté avant la fin du délai")
    except Exception as e:
        logging.error(f"❌ Erreur : {str(e)}")
    return None

def transcribe_with_groq(audio_filepath, language="en"):
    """Transcrit l'audio en utilisant l'API Groq."""
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    stt_model = "whisper-large-v3"
    
    if not GROQ_API_KEY:
        logging.error("❌ La clé API Groq n'est pas configurée")
        return None
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language=language
            )
        
        logging.info("✅ Transcription réussie")
        return transcription.text
    
    except Exception as e:
        logging.error(f"❌ Erreur lors de la transcription : {str(e)}")
        return None

# def transcribe_with_groq(audio_filepath, GROQ_API_KEY=None, stt_model="whisper-large-v3"):
#     """Transcrit un fichier audio en texte avec Groq
    
#     Args:
#         audio_filepath: Chemin vers le fichier audio
#         GROQ_API_KEY: Clé API Groq (optionnelle si déjà dans os.environ)
#         stt_model: Modèle de transcription à utiliser
#     """
#     try:
#         if not GROQ_API_KEY:
#             GROQ_API_KEY = os.getenv("GROQ_API_KEY")
            
#         if not GROQ_API_KEY:
#             raise ValueError("Clé API Groq manquante")

#         # Votre implémentation de la transcription ici
#         # ...
#         return "Transcription du texte"  # Résultat factice
        
#     except Exception as e:
#         raise Exception(f"Échec transcription: {str(e)}")
    
# Exemple d'utilisation
if __name__ == "__main__":
    # Enregistrement audio
    audio_file = enregistrer_audio("ma_voix.wav")
    
    if audio_file:
        print("Enregistrement réussi !")
        
        # Transcription
        transcription = transcribe_with_groq(audio_file)
        if transcription:
            print("\nTranscription:")
            print(transcription)