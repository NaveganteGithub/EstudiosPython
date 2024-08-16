import requests as r

resultado = r.get("https://linuxcontainers.org/")

print(resultado.text)
print(dir(resultado.cookies))
print(resultado.cookies._policy)
print(resultado.status_code)

