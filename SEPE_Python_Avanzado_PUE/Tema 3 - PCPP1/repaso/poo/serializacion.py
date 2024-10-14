import shelve

ruta = "."
archivo = "almacenaje"

obj_seri = shelve.open(ruta + "/" + archivo, "n")
obj_seri["factores"] = [1, 2, 3, 4]
obj_seri["calculos"] = ["Suma", "Resta"]

obj_seri.close()

obj_seri2 = shelve.open(ruta + "/" + archivo, "r")
print(obj_seri2["factores"])
obj_seri2.close()
