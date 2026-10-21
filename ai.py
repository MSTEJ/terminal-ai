import os
import sys
import time
from google import genai

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: Die Umgebungsvariable GEMINI_API_KEY wurde nicht gefunden!")
        sys.exit(1)

    print("Initialisiere KI-Chat-Sitzung... Bitte warten...")
    
    try:
        # 1. Client mit dem aktuellen Modell vorbereiten
        client = genai.Client(api_key=api_key)
        
        # 2. Eine fortlaufende Chat-Sitzung starten (das "Gedächtnis")
        chat = client.chats.create(model="gemini-3.8-flash")
        
        print("\n==================================================")
        print("🤖 KI-ASSISTENT MIT GEDÄCHTNIS INITIALISIERT")
        print("Tippe 'exit', 'quit' oder 'beenden' zum Schließen.")
        print("==================================================\n")

        # 3. Die interaktive Chat-Schleife starten
        while True:
            try:
                # Benutzereingabe live im Terminal abfragen
                user_input = input("Du: ")
                
                # Abbruchbedingungen prüfen
                if user_input.lower() in ['exit', 'quit', 'beenden']:
                    print("\nChat beendet. Auf Wiedersehen!")
                    break
                    
                if not user_input.strip():
                    continue

                # Nachricht an die bestehende Chat-Sitzung senden
                response = chat.send_message(user_input)
                
                # Antwort ausgeben
                print(f"\nKI: {response.text}\n")
                print("-" * 30)

            except Exception as e:
                print(f"\nFehler bei der Übertragung: {e}")
                print("Bitte versuche es gleich noch einmal.\n")
                time.sleep(2)

    except Exception as init_error:
        print(f"Fehler bei der Chat-Initialisierung: {init_error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
