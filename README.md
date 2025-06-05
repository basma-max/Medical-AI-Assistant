# 🩺 Assistant Médical IA

<img src="image/cap" width="800"/>
*(Prévisualisation de l'interface)*


  ## 📌 Description du Projet
**Objectif** : Développer une solution IA permettant aux utilisateurs de :
- Analyser des images médicales (lésions cutanées, radiographies, etc.)
- Décrire leurs symptômes vocalement
- Obtenir un diagnostic préliminaire avec synthèse vocale

**Public Cible** : Professionnels de santé (outil d'aide au diagnostic) et particuliers (première évaluation)

## 🌟 Fonctionnalités Principales
| Fonctionnalité | Technologie | 
|---------------|------------|
| Transcription vocale | Whisper (OpenAI) |
| Analyse d'images | Gemini Pro Vision | 
| Synthèse vocale | ElevenLabs/gTTS | 
| Interface utilisateur | Gradio | 


## 🛠 Architecture Technique

```mermaid
graph TD
    A[Entrée Utilisateur] -->|Audio| B(Transcription Whisper)
    A -->|Image| C(Analyse Gemini Vision)
    B --> D[Fusion des Données]
    C --> D
    D --> E{Diagnostic IA}
    E -->|Résultat| F[Synthèse Vocale]
    F --> G[Interface Gradio]
    G --> H[Utilisateur]
    
    style A fill:#4CAF50,stroke:#388E3C
    style B,C fill:#2196F3,stroke:#0b7dda
    style D fill:#9C27B0,stroke:#7B1FA2
    style E fill:#FF9800,stroke:#F57C00
    style F fill:#607D8B,stroke:#455A64
    style G fill:#00BCD4,stroke:#0097A7
    style H fill:#4CAF50,stroke:#388E3C

## 🛠 Installation
```bash
git clone https://github.com/votre-username/Medical-AI-Assistant.git
cd Medical-AI-Assistant
pip install -r requirements.txt
