import requests, sqlite3
"""
tipo text CHECK (tipo IN ("Agua", "Bicho", "Dragón", "Eléctrico", "Fantasma", 
                            "Fuego", "Hada", "Hielo", "Lucha", "Normal", "Planta", 
                            "Psíquico", "Roca", "Siniestro", "Tierra", "Veneno", 
                            "Volador", "???")),
"""
bd = "Librerias\\SRC\\Pokemon\\Extracion_Pokemon.sqlite"
try:
    
    conexion = sqlite3.connect(bd)
    
    conexion.execute("""
        Create table Movimiento (
                     Nombre text primary key,
                     Descripcion text,
                     Efecto_Descripcion text,
                     Tipo text CHECK (Tipo IN ("Normal", "Fire", "Water", "Electric", 
                                                "Grass", "Ice", "Fighting", "Poison", 
                                                "Ground", "Flying", "Psychic", "Bug", 
                                                "Rock", "Ghost", "Dragon", "Dark", "Steel", 
                                                "Fairy", "???")),
                     Potencia text, 
                     Puntos_Poder text,
                     Precision text,
                     Prioridad text,
                     Probabilidad_Critico text, 
                     Probabilidad_Efecto_Secundario text, 
                     min_golpes text, 
                     max_golpes text,
                     min_duracion text,
                     max_duracion text,
                     Poder_drenaje text,
                     Objetivo text
        )
    """)

    conexion.close()
    print("Tablas creadas.")

except sqlite3.OperationalError:
    print("Error al crear la tablas.")

# print("Nombre", "Tipo", "Puntos de Poder", "Poder Ataque", "Prioridad", "Probabilidad Golpe Critico", "Probabilidad Efecto Secundario", "Número de golpes minimo", "Número de golpes máximo", "Duracion minima", "Duracion Máxima", "Poder Drenaje", sep=" | ")

# for id in range(915):
# for id in range(1, 5 + 1):
# for id in range(500, 505 + 1):

consulta = """
            insert into Movimiento (Nombre, Descripcion, Efecto_Descripcion, 
            Tipo, Potencia, Puntos_Poder, Precision, Prioridad, Probabilidad_Critico, 
            Probabilidad_Efecto_Secundario, min_golpes, max_golpes, min_duracion, max_duracion, 
            Poder_drenaje, Objetivo) 
            values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """

try:

    conexion = sqlite3.connect(bd)

    for id in range(1, 915 + 1):
        movimiento = f"https://pokeapi.co/api/v2/move/{id}"
        info_movimiento = requests.get(movimiento).json()
        
        name = None
        try:
            num_nombres = len(info_movimiento['names'])
            if num_nombres > 5:
                name = info_movimiento['names'][5]['name']
            elif num_nombres > 0:
                name = info_movimiento['names'][0]['name']

        except IndexError:
            conexion.execute(consulta, 
                            (str(id), None, None, None, None, None, None, None, None, None, 
                             None, None, None, None, None, None, None))
            print("Movimiento no encontrado.")
            continue
        
        descripcion = None
        descripcion_efecto = None
        try:
            if len(info_movimiento['flavor_text_entries']) > 0:
                posicion = 0
                descripcion = info_movimiento['flavor_text_entries'][posicion]['flavor_text']

                for desc in info_movimiento['flavor_text_entries']:
                    
                    if desc['language']['name'] == "es":
                        descripcion = info_movimiento['flavor_text_entries'][posicion]['flavor_text']
                        break

                    posicion += 1
                else: # Si el bucle finaliza sin break entonces ejecutara lo siguiente
                    descripcion = info_movimiento['flavor_text_entries'][0]['flavor_text']
            
            if len(info_movimiento['effect_entries']) > 0:
                descripcion_efecto = info_movimiento['effect_entries'][0]['effect']

        except IndexError:
            conexion.execute(consulta, 
                            (name, None, "Sin descripcion", 
                             None, None, None, None, None, None, None, 
                             None, None, None, None, None, None, None))
            print("Descripcion no encontrada.")
            continue
        
        tipo = info_movimiento['type']['name']
        tipo = str(tipo).title()
        pp = info_movimiento['pp']
        poder_ataque = info_movimiento['power']
        precision = info_movimiento['accuracy']
        prioridad = info_movimiento['priority']
        prob_efecto_secundario = info_movimiento['effect_chance']
        prob_golpe_critico = num_golpes_min = num_golpes_max = duracion_min = duracion_max = poder_drenaje = None
        try:
            prob_golpe_critico = info_movimiento['meta']['crit_rate']
            num_golpes_min = info_movimiento['meta']['min_hits']
            num_golpes_max = info_movimiento['meta']['max_hits']
            duracion_min = info_movimiento['meta']['min_turns']
            duracion_max = info_movimiento['meta']['max_turns']
            poder_drenaje = info_movimiento['meta']['drain']
        except TypeError:
            pass
        objetivo = info_movimiento['target']['name']

        print("-" * 32, movimiento, "-" * 32)
        print(name, descripcion, descripcion_efecto, tipo, pp, poder_ataque, 
            prioridad, prob_golpe_critico, prob_efecto_secundario, 
            num_golpes_min, num_golpes_max, duracion_min, duracion_max, 
            poder_drenaje, objetivo, sep=" | ", end=" |")
        print()

        try:
            conexion.execute(consulta, 
                            (name, descripcion, descripcion_efecto,
                            tipo, poder_ataque, pp, precision, prioridad, prob_golpe_critico,
                            prob_efecto_secundario, num_golpes_min, num_golpes_max, duracion_min, duracion_max,
                            poder_drenaje, objetivo))
            print("Fila Insertada")
        except sqlite3.IntegrityError:
            conexion.execute(consulta, 
                            (str(id), None, None, None, None, None, None, None, None, None, 
                             None, None, None, None, None, None))
            print("El movimiento ya esta registrado.")
        
    conexion.commit()
    conexion.close()

except sqlite3.OperationalError as error:
    print("Error al insertar las filas")
    print(error)
# Dentro de los movimientos hay una lista llamada learned_by_pokemon que contiene 
# un listado de los pokemon que pueden aprender un cierto movimiento
    
