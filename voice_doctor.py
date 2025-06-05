import os
import logging
from dotenv import load_dotenv
from gtts import gTTS
import requests
from pydub import AudioSegment
from pydub.playback import play

# Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# class VoiceAssistant:
#     def __init__(self):
#         self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
#         self.elevenlabs_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
#         self.headers = {
#             "xi-api-key": self.elevenlabs_api_key,
#             "Content-Type": "application/json",
#             "accept": "audio/mpeg"
#         }

#     def play_audio(self, filepath):
#         try:
#             sound = AudioSegment.from_file(filepath)
#             play(sound)
#         except Exception as e:
#             logger.error(f"Erreur de lecture : {e}")
#             raise

#     def text_to_speech_with_gtts(self, input_text, output_file="output.mp3"):
#         try:
#             tts = gTTS(text=input_text, lang='fr')
#             tts.save(output_file)
#             logger.info(f"Audio MP3 sauvegardé : {output_file}")
#             return output_file
#         except Exception as e:
#             logger.error(f"Échec gTTS : {e}")
#             raise

#     def text_to_speech_with_elevenlabs(self, input_text, output_file="output_el.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):
#         """Utilise l'API ElevenLabs directement avec le bon modèle"""
#         try:
#             if not self.elevenlabs_api_key:
#                 raise ValueError("Clé API ElevenLabs manquante")

#             data = {
#                 "text": input_text,
#                 "model_id": "eleven_turbo_v2",  # Modèle valide
#                 "voice_settings": {
#                     "stability": 0.5,
#                     "similarity_boost": 0.5
#                 }
#             }

#             response = requests.post(
#                 self.elevenlabs_url.format(voice_id=voice_id),
#                 json=data,
#                 headers=self.headers
#             )

#             if response.status_code == 200:
#                 with open(output_file, "wb") as f:
#                     f.write(response.content)
#                 logger.info(f"Audio ElevenLabs sauvegardé : {output_file}")
#                 return output_file
#             else:
#                 raise Exception(f"Erreur API: {response.status_code} - {response.text}")

#         except Exception as e:
#             logger.error(f"Échec ElevenLabs : {e}")
#             raise

# class VoiceAssistant:
#     def __init__(self):
#         self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

#     def generate_response(self, text, output_file="response.mp3", use_elevenlabs=False, lang='fr'):
#         """Génère une réponse vocale à partir du texte"""
#         try:
#             if use_elevenlabs and self.elevenlabs_api_key:
#                 return self.text_to_speech_with_elevenlabs(text, output_file)
#             else:
#                 return self.text_to_speech_with_gtts(text, output_file, lang)
#         except Exception as e:
#             raise Exception(f"Erreur de synthèse vocale: {str(e)}")

#     def text_to_speech_with_gtts(self, text, output_file, lang='fr'):
#         tts = gTTS(text=text, lang=lang)
#         tts.save(output_file)
#         return output_file

#     # def text_to_speech_with_elevenlabs(self, text, output_file, voice_id="21m00Tcm4TlvDq8ikWAM"):
#     #     headers = {
#     #         "xi-api-key": self.elevenlabs_api_key,
#     #         "Content-Type": "application/json"
#     #     }
#     #     data = {
#     #         "text": text,
#     #         "model_id": "eleven_turbo_v2"
#     #     }
#     #     response = requests.post(
#     #         f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
#     #         json=data,
#     #         headers=headers
#     #     )
#     #     with open(output_file, "wb") as f:
#     #         f.write(response.content)
#     #     return output_file
#     def text_to_speech_with_elevenlabs(self, text, output_file="output.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):
#      """Synthèse vocale avec ElevenLabs"""
#     try:
#         if not self.elevenlabs_api_key:
#             raise ValueError("Clé API ElevenLabs manquante")

#         headers = {
#             "xi-api-key": self.elevenlabs_api_key,
#             "Content-Type": "application/json"
#         }
#         data = {
#             "text": text,
#             "model_id": "eleven_turbo_v2",
#             "voice_settings": {
#                 "stability": 0.5,
#                 "similarity_boost": 0.5
#             }
#         }

#         response = requests.post(
#             f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
#             json=data,
#             headers=headers
#         )
#         response.raise_for_status()

#         # Écriture du fichier
#         with open(output_file, "wb") as f:
#             f.write(response.content)  
#         print(type(output_file)) 

#     except Exception as e:
#         raise Exception(f"Erreur ElevenLabs: {str(e)}")

# if __name__ == "__main__":
#     assistant = VoiceAssistant()
    
#     # Test gTTS
#     print("Test gTTS...")
#     try:
#         mp3_file = assistant.text_to_speech_with_gtts("Bonjour avec gTTS", "gtts_output.mp3")
#         assistant.play_audio(mp3_file)
#     except Exception as e:
#         logger.error(f"Erreur gTTS : {e}")
    
#     # Test ElevenLabs
#     if assistant.elevenlabs_api_key:
#         print("Test ElevenLabs...")
#         try:
#             mp3_file = assistant.text_to_speech_with_elevenlabs("Bonjour avec ElevenLabs", "el_output.mp3")
#             assistant.play_audio(mp3_file)
#         except Exception as e:
#             logger.error(f"Erreur ElevenLabs : {e}")
#     else:
#         logger.warning("Skipping ElevenLabs test - aucune clé API trouvée")


class VoiceAssistant:
    def __init__(self):
        """Initialise avec la clé API ElevenLabs si disponible"""
        self.elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
        self.logger = logging.getLogger(__name__)
        
    def text_to_speech_with_gtts(self, text, output_file="output.mp3", lang='fr'):
        """Synthèse vocale avec gTTS (Google)"""
        try:
            tts = gTTS(text=text, lang=lang)
            tts.save(output_file)
            self.logger.info(f"Audio généré avec gTTS: {output_file}")
            return output_file
        except Exception as e:
            self.logger.error(f"Erreur gTTS: {e}")
            raise

    def text_to_speech_with_elevenlabs(self, text, output_file="output.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):
        """Synthèse vocale avec ElevenLabs API"""
        try:
            if not hasattr(self, 'elevenlabs_api_key') or not self.elevenlabs_api_key:
                raise ValueError("Clé API ElevenLabs non configurée")

            headers = {
                "xi-api-key": self.elevenlabs_api_key,
                "Content-Type": "application/json"
            }
            data = {
                "text": text,
                "model_id": "eleven_turbo_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }

            response = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
                json=data,
                headers=headers
            )
            response.raise_for_status()

            with open(output_file, "wb") as f:
                f.write(response.content)
            
            self.logger.info(f"Audio ElevenLabs généré: {output_file}")
            return output_file

        except Exception as e:
            self.logger.error(f"Erreur ElevenLabs: {e}")
            raise

    def generate_response(self, text, output_file="response.mp3", use_elevenlabs=False, lang='fr'):
        """Point d'entrée unifié pour la synthèse vocale"""
        if use_elevenlabs and hasattr(self, 'elevenlabs_api_key') and self.elevenlabs_api_key:
            return self.text_to_speech_with_elevenlabs(text, output_file)
        return self.text_to_speech_with_gtts(text, output_file, lang)