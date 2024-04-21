"""Origen: Conversación con Bing, 25/1/2024
(1) python - multiprocessing vs multithreading vs asyncio - Stack Overflow. https://stackoverflow.com/questions/27435284/multiprocessing-vs-multithreading-vs-asyncio.
(2) AsyncIO, Threading, and Multiprocessing in Python - Medium. https://medium.com/analytics-vidhya/asyncio-threading-and-multiprocessing-in-python-4f5ff6ca75e8.
(3) Exploring Concurrency in Python: asyncio, Multithreading, and ... - Medium. https://medium.com/@bobbymistery/exploring-concurrency-in-python-asyncio-multithreading-and-multiprocessing-511d974eaed0.
(4) undefined. https://pypi.org/project/aiomultiprocess/."""

# **AsyncIO:**

import asyncio

async def main():
    print("¡Hola, AsyncIO!")
    await asyncio.sleep(1)
    print("¡Adiós, AsyncIO!")

asyncio.run(main())

# **Multithreading:**

import threading

def worker():
    """Función que realiza el trabajo en el hilo."""
    print("¡Hola, Multithreading!")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

