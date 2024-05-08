# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

consulta = ""

def conector(prompt: str = "Hello"):
    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        # {"role": "system", "content": "Always answer in rhymes."},
        # {"role": "user", "content": "Hello, my name Ismael"}
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    )

    return completion.choices[0].message

while True:

    consulta = input("Que quieres decirle a la IA: ")

    if consulta.lower() in ["exit now", "exit"]:
        break

    chat = conector(consulta)
    respuesta = chat.content
    rol = chat.role
    print(chat, respuesta, rol, sep="\n\n", end="\n\n")