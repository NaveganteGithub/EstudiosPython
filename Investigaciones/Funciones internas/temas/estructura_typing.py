# La libreria typing permite usar tipado estatico en Python
from typing import Dict, List, Set, Tuple

ids: Tuple[int] = (3121232, 5234234, 5435635, 7674565)
ids: Set[int] = {3121232, 5234234, 5435635, 7674565}
nombres: List[int] = ("Lucia", "Daniel", "Samuel", "Adrian")

empleados: Dict[int, str] = {
    3121232: "Lucia",
    5234234: "Daniel", 
    5435635: "Samuel", 
    7674565: "Adrian"
}

empresa: List[Dict[int, str]] = [
    {
    3121232: "Lucia",
    5234234: "Daniel", 
    5435635: "Samuel", 
    7674565: "Adrian"
    },
    {
    5164495: "Andres",
    5324452: "Alejandro", 
    4848566: "Carla", 
    8390128: "Rafa"
    },
    {
    4532644: "Alex",
    5326432: "Jose", 
    6556115: "Alfredo", 
    5198819: "Diego"
    }
]


print(ids)
print(nombres)
print(empleados)
print(empresa[0])
print(empresa)