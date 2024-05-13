import keyboard
keys = keyboard.record(until ='ENTER')

for letra in keys:
    if letra.event_type == 'down':
        if letra.name.lower() != "enter":
            print(letra.name, end="")

# keyboard.play(keys)