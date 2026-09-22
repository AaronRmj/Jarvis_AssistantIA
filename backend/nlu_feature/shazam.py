"""1. Déclencher le script (via terminal ou commande).
2. Capturer l'audio du micro pendant 5 à 7 secondes (sauvegarder temporairement en WAV).
3. Envoyer le fichier audio aux serveurs de Shazam via ShazamIO.
4. Parser le dictionnaire JSON de réponse.
5. Extraire 'title' (Titre) et 'subtitle' (Artiste).
6. Afficher dans le terminal (ou transmettre à la synthèse vocale de Jarvis)"""

import asyncio
import sounddevice as sd
import scipy.io.wavfile as wav
from shazamio import Shazam
from pathlib import Path

DURATION = 6
SAMPLE_RATE = 44100
TEMP_FILENAME = "temp_capture.wav"

# Chemin vers backend/Jarvis/services/reponse_ia/ia.txt
IA_TXT_PATH = Path(__file__).resolve().parents[1] / 'Jarvis' / 'services' / 'reponse_ia' / 'ia.txt'
current_dir = Path(__file__).resolve().parent
target_file_path = current_dir.parent / "Jarvis" / "services" / "reponse_ia" / "ia.txt"

def record_microphone():
    print("Ecoute en cours...")
    recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    wav.write(TEMP_FILENAME, SAMPLE_RATE, recording)
    print("chargement terminé, analyse en cours")


async def identify_song():
    shazam = Shazam()
    result = await shazam.recognize(TEMP_FILENAME)
    track = result.get('track')

    if track:
        title = track.get('title', 'titre inconnue')
        artist = track.get('subtitle','Artiste inconnu')
        return title, artist
    return None, None


def lancer_shazam():
    record_microphone()
    title, artiste = asyncio.run(identify_song())

    print("---------------------")
    if title and artiste:
        print(f"Il s'agit de {title} de {artiste}")
        # Ecrire le titre identifié dans backend/Jarvis/services/reponse_ia/ia.txt
        try:
            with open(target_file_path, "w", encoding="utf-8") as file:
                file.write(f"Il s'agit de {title} de {artiste}")
        except Exception as e:
            print(f"Erreur écriture ia.txt: {e}")
    else: 
        print("impossible d'identifier la musique")


