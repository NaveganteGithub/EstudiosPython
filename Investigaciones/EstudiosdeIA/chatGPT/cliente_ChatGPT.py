import openai
from openai import OpenAI

try:
    # Point to the local server
    client = OpenAI(api_key="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")

    consulta = ""

    def conector(prompt: str = "Hello"):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
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

except openai.RateLimitError:
    print("Has alcanzado el limite mensual, tienes que pagar un poco más.")