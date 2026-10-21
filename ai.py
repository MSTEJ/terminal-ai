
import os
import sys
import time
from google import genai

def main():
    if len(sys.argv) < 2:
        print("Fehler: Bitte gib eine Frage in Anführungszeichen mit an!")
        sys.exit(1)
    
    user_frage = sys.argv[1]

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungsvariable GEMINI_API_KEY wurde nicht gefunden!")
        sys.exit(1)

    max_versuche = 3
    for versuch in range(1, max_versuche + 1):
        print(f"Verbinde mit der KI (Versuch {versuch}/{max_versuche})... Bitte warten...")
        
        try:
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=user_frage,
            )
            
            print("\n=== KI-ASSISTENT ===")
            print(response.text)
            print("====================")
            return

        except Exception as e:
            if versuch == max_versuche:
                print(f"\nGoogle-Server dauerhaft überlastet: {e}")
            else:
                print("Server überlastet (503). Warte 4 Sekunden vor dem nächsten Versuch...\n")
                time.sleep(4)

if __name__ == "__main__":
    main()

import sys
from google import genai

def main():
    # 1. Prüfen, ob der Benutzer überhaupt eine Frage eingegeben hat
    if len(sys.argv) < 2:
        print("Fehler: Bitte gib eine Frage in Anführungszeichen mit an!")
        print('Beispiel: python ai.py "Was ist der Unterschied zwischen Git und GitHub?"')
        sys.exit(1)
    
    # 2. Den Text der Frage aus den Terminal-Argumenten auslesen
    user_frage = sys.argv[1]

    # 3. Den API-Schlüssel aus dem Linux-System auslesen
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungsvariable GEMINI_API_KEY wurde nicht gefunden!")
        print("Bitte führe zuerst aus: export GEMINI_API_KEY='dein_schluessel'")
        sys.exit(1)

    print("Verbinde mit der KI... Bitte warten...\n")

    try:
        # 4. Den Google GenAI Client initialisieren
        client = genai.Client(api_key=api_key)
        
        # 5. Die Anfrage an das aktuelle, schlanke Modell senden
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=user_frage,
        )
        
        # 6. Die Antwort sauber im Terminal ausgeben
        print("=== KI-ASSISTENT ===")
        print(response.text)
        print("=========
