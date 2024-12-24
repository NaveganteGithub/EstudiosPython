import sqlite3 as db
import requests as r

bd = "Librerias\\SRC\\Pokemon\\Extracion_Pokemon.sqlite"

try:
    
    conexion = db.connect(bd)
    cursor = conexion.cursor()

    # for id in 14, 349:
    for id in range(1, 915 + 1):
        movimiento = f"https://pokeapi.co/api/v2/move/{id}"
        info_movimiento = r.get(movimiento).json()
        estadisticas = info_movimiento['stat_changes']
        
        name = None
        try:
            num_nombres = len(info_movimiento['names'])
            if num_nombres > 5:
                name = info_movimiento['names'][5]['name']
            elif num_nombres > 0:
                name = info_movimiento['names'][0]['name']
            
            print(id, name)
        except IndexError | KeyboardInterrupt:
            continue
        
        if len(estadisticas) <= 0:
            continue

        for caracteristica in estadisticas:
            caracteristica_actual = caracteristica['stat']['name']
            cantidad = caracteristica['change']
            stats_actuales = None

            if cantidad < 0:
                stats_actuales = {'hp': 'Bajada_Vida', 'attack': 'Bajada_Ataque', 'defense': 'Bajada_Defensa', 
                    'special-attack': 'Bajada_Ataque_Especial', 'special-defense': 'Bajada_Defensa_Especial', 
                    'speed': 'Bajada_Velocidad', 'accuracy': 'Bajada_Precision', 
                    'evasion': 'Bajada_Evasion'}
                cantidad = abs(cantidad)
            else:
                stats_actuales = {'hp': 'Subida_Vida', 'attack': 'Subida_Ataque', 'defense': 'Subida_Defensa', 
                    'special-attack': 'Subida_Ataque_Especial', 'special-defense': 'Subida_Defensa_Especial', 
                    'speed': 'Subida_Velocidad', 'accuracy': 'Subida_Precision', 
                    'evasion': 'Subida_Evasion'}
        
        actualizacion = f"UPDATE Movimiento set {stats_actuales[caracteristica_actual]} = ? where Nombre = ?"
        cursor.execute(actualizacion, (cantidad, name))
        # print(stats_actuales[caracteristica_actual], cantidad)
    
    conexion.commit()
    cursor.close()
    conexion.close()

except db.OperationalError as error_op:
    print(error_op)
except KeyboardInterrupt:
    print("Programa detenido.")