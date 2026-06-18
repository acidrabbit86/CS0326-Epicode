from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

config = types.GenerateContentConfig(
    system_instruction=(
        "Sei un esperto di Cyber Security per aziende con esperienza pluriennale. "
        "Spiega i concetti in modo semplice, con esempi pratici ed analogie capibili "
        "per tutti. Se non sai qualcosa, dillo chiaramente."
    )
)

while True:
    domanda = input("Cosa vuoi sapere? : ")
    if domanda.lower() == "esci":
        print("Arrivederci!")
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=domanda,
        config=config
    )
    print(f"AI: {response.text}\n")
