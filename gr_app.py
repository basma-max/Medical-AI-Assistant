
# import os
# import base64
# import gradio as gr
# from brain_doctor import analyser_image 
# from voice_patient import transcribe_with_groq
# from voice_doctor import VoiceAssistant

# # Configuration initiale
# voice_doctor = VoiceAssistant()

# SYSTEM_PROMPT = """En tant que spécialiste médical, analysez cette image en :
# 1. Identifiant 1-2 pathologies potentielles
# 2. Recommandant des actions appropriées
# 3. Indiquant l'urgence de consultation
# Répondez en français, clairement et avec bienveillance (max 3 phrases)."""

# def encode_image(image_path):
#     """Encode l'image en base64 de manière optimisée"""
#     with open(image_path, "rb") as f:
#         return base64.b64encode(f.read()).decode('utf-8')


# def process_medical_request(audio_filepath, image_filepath):
#     try:
#         # 1. Transcription vocale
#         speech_text = transcribe_with_groq(
#         audio_filepath=audio_filepath,
#         GROQ_API_KEY=os.getenv("GROQ_API_KEY"),
#         stt_model="whisper-large-v3"
#         ) if audio_filepath else ""

#         # 2. Analyse médicale
#         if image_filepath:
#             # prompt = f"{SYSTEM_PROMPT}\n\nPatient: {speech_text}" if speech_text else SYSTEM_PROMPT
#             doctor_response = analyser_image(image_filepath+speech_text)
#         else:
#             doctor_response = "Veuillez fournir une image pour une analyse précise."

#         # 3. Synthèse vocale
#         if os.getenv("ELEVENLABS_API_KEY"):
#             audio_file = voice_doctor.text_to_speech_with_elevenlabs(
#             text=doctor_response,
#             output_file="response.mp3"  # Bon nom de paramètre
#              )
#         else:
#             audio_file = voice_doctor.text_to_speech_with_gtts(
#                 text=doctor_response,
#                 output_filepath="response.mp3",
#                 lang='fr'
#             )

#         return speech_text, doctor_response, audio_file

#     except Exception as e:
#         error = f"Erreur système : {str(e)}"
#         return error, error, None

# # Interface Gradio optimisée
# with gr.Blocks(theme=gr.themes.Soft(), title="Assistant Médical IA") as app:
#     gr.Markdown("""
#     # 🩺 Diagnostic Médical Assisté
#     *Analyse préliminaire d'images médicales avec IA*
#     """)
    
#     with gr.Row():
#         with gr.Column():
#             audio_input = gr.Audio(
#                 sources=["microphone"],
#                 type="filepath",
#                 label="Décrivez vos symptômes"
#             )
#             image_input = gr.Image(
#                 type="filepath",
#                 label="Image Médicale"
#             )
#             submit_btn = gr.Button("Analyser", variant="primary")
        
#         with gr.Column():
#             transcription = gr.Textbox(label="Transcription")
#             diagnosis = gr.Textbox(label="Diagnostic Préliminaire")
#             voice_output = gr.Audio(
#                 label="Réponse Vocale",
#                 autoplay=True,
#                 interactive=False
#             )
    
#     submit_btn.click(
#         fn=process_medical_request,
#         inputs=[audio_input, image_input],
#         outputs=[transcription, diagnosis, voice_output]
#     )

# if __name__ == "__main__":
#     # Validation des clés API
#     if not os.getenv("GROQ_API_KEY"):
#         raise ValueError("Clé GROQ_API_KEY manquante dans .env")
    
#     app.launch(
#         server_name="0.0.0.0",
#         server_port=7860,
#         show_error=True,
#         share=False  # True pour un lien public
#     )


import os
import base64
import gradio as gr
from brain_doctor import analyser_image 
from voice_patient import transcribe_with_groq
from voice_doctor import VoiceAssistant

# Configuration initiale
voice_doctor = VoiceAssistant()

SYSTEM_PROMPT = """En tant que spécialiste médical, analysez cette image en :
1. Identifiant 1-2 pathologies potentielles
2. Recommandant des actions appropriées
3. Indiquant l'urgence de consultation
Répondez en français, clairement et avec bienveillance (max 3 phrases)."""

def encode_image(image_path):
    """Encode l'image en base64 de manière optimisée"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')


def process_medical_request(audio_filepath, image_filepath):
    try:
        # 1. Transcription vocale
        speech_text = transcribe_with_groq(
            audio_filepath=audio_filepath
            # GROQ_API_KEY=os.getenv("GROQ_API_KEY"),
            # stt_model="whisper-large-v3"
        ) if audio_filepath else ""

        # 2. Analyse médicale
        if image_filepath:
            # Important : ne pas concaténer chemin + texte
            # On envoie ici uniquement le chemin d'image, ou encode l'image si nécessaire
            # Si analyser_image accepte un paramètre "contexte" avec la transcription, il faudrait l’ajouter
            # Exemple (si ta fonction supporte) :
            # doctor_response = analyser_image(image_path=image_filepath, context_text=speech_text)

            # Sinon, en l'état, on envoie juste l'image
            doctor_response = analyser_image(image_filepath)
            
            # Optionnel : tu peux préfixer le prompt système + transcription dans ta fonction analyser_image si tu veux
        else:
            doctor_response = "Veuillez fournir une image pour une analyse précise."

        # 3. Synthèse vocale
        if os.getenv("ELEVENLABS_API_KEY"):
            audio_file = voice_doctor.text_to_speech_with_elevenlabs(
                text=doctor_response,
                output_file="response.mp3"  # Vérifie bien que c’est le nom attendu par ta fonction
            )
        else:
            audio_file = voice_doctor.text_to_speech_with_gtts(
                text=doctor_response,
                output_filepath="response.mp3",  # Vérifie si c’est output_filepath ou output_file selon ta fonction
                lang='fr'
            )

        # On retourne le chemin du fichier audio pour Gradio
        return speech_text, doctor_response, "response.mp3"

    except Exception as e:
        error = f"Erreur système : {str(e)}"
        return error, error, None

# Interface Gradio optimisée
with gr.Blocks(theme=gr.themes.Soft(), title="Assistant Médical IA") as app:
    gr.Markdown("""
    # 🩺 Diagnostic Médical Assisté
    *Analyse préliminaire d'images médicales avec IA*
    """)

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="Décrivez vos symptômes"
            )
            image_input = gr.Image(
                type="filepath",
                label="Image Médicale"
            )
            submit_btn = gr.Button("Analyser", variant="primary")

        with gr.Column():
            transcription = gr.Textbox(label="Transcription")
            diagnosis = gr.Textbox(label="Diagnostic Préliminaire")
            voice_output = gr.Audio(
                label="Réponse Vocale",
                type="filepath",  # Important pour lire un fichier généré dynamiquement
                autoplay=True,
                interactive=False
            )

    submit_btn.click(
        fn=process_medical_request,
        inputs=[audio_input, image_input],
        outputs=[transcription, diagnosis, voice_output]
    )

if __name__ == "__main__":
    # Validation des clés API
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("Clé GROQ_API_KEY manquante dans .env")

    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        share=False  # True pour un lien public
    )
