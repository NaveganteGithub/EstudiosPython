import os
import warnings

warnings.filterwarnings('ignore')

operating_system = os.name

if operating_system == "posix": # Linux
        # Creamos una libreria de peticiones propia para Linux, debido a que 
        # linux puede variar en paquetes y no siempre tendremos instalado el 
        # comando que nosotros necesitamos, y puede que el usuario no quiera 
        # instalarlo por cualquier motivo
        import mac_address

        mac = mac_address.get_mac_address("10.10.115.179") # La IP del objetivo
        print(mac)
elif operating_system == "nt": # Windows
        pass