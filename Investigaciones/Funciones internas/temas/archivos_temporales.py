import tempfile

lectura = ""
with tempfile.TemporaryFile() as at:
    at.write(b"Hola")
    at.seek(0)
    lectura = "".join(chr(char) for char in at.read())
    print(lectura)

with tempfile.TemporaryDirectory() as dt:
    print(dt)