import os

operating_system = os.name
ip = "10.10.116.178"

if operating_system == "posix": # Linux

        # Creamos una libreria de peticiones propia para Linux, debido a que 
        # linux puede variar en paquetes y no siempre tendremos instalado el 
        # comando que nosotros necesitamos, y puede que el usuario no quiera 
        # instalarlo por cualquier motivo
        import mac_address

        mac = mac_address.get_mac_address(ip) # La IP del objetivo
        print(mac)
        
elif operating_system == "nt": # Windows
        pass