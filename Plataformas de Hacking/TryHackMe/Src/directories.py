import sys 
import Src.lib.pyclientweb as cliente

# C:\Users\ismae\git\tryhackme\python\Src\directories.py 10.10.140.204

sub_list = open("python\\Src\\tools\\wordlist2.txt").read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = cliente.get(dir_enum)
    if r["Respuesta"][0] == 200:
        print("Existe un fichero llamado", r["Recurso"], "en el dominio", r["Domain"], f"\nhttp://{sys.argv[1]}/{dir}.html")