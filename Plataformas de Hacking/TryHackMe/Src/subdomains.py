import sys
import Src.lib.pyclientweb as cliente

# He realizado tambien cambios en el script de python de tryhackme
# que copiamos anteriormente

# Vale, en el anterior video cometi un error garrafal, es necesario 
# si o si tener un nombre de dominio para este ejercicio, por la fuerza
# de la costumbre, creia que habia que hacer el ejercicio obligatoriamente
# en la maquina virtual que proporcionaba el experto, pero no, realmente
# podemos ampliarnos a otros objetivos, por cierto he hecho bastantes,
# cambios en los dos scripts, para adaptarlos a mis necesidades, por lo que
# mostrare ambos script de python, para dejar registro de mis progresos

# NOTA: si solamente tenemos una ip para trabajar y no el dominio, podemos
# hacer una busqueda "DNS reverse" para consultar los PTR de los servidores
# DNS y averiguar nombres de dominio

# c:/Users/ismae/git/tryhackme/python/Src/subdomains.py python.org
# c:/Users/ismae/git/tryhackme/python/Src/subdomains.py google.com
sub_list = open("python\\Src\\tools\\wordlist2.txt").read()  
subdoms = sub_list.splitlines()
# subdoms = ["docs", "www"]

for sub in subdoms:
    sub_domains = f"{sub}.{sys.argv[1]}"
    # print(sub_domains)
    respuesta = cliente.existe_dominio(sub_domains)
    if respuesta[0]:
        print(respuesta[1])