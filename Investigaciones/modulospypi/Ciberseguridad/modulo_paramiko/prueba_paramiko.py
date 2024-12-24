import getpass
import paramiko
import sys

class Ssh:
    def __init__(self):
        self.HOST = ''
        self.USERNAME = ''
        self.PASSWORD = ''
        self.CLIENT = None

    def conecta(self):
        try:
            self.HOST = input('Nombre o IP del host: ')
            self.USERNAME = input('Usuario: ')
            self.PASSWORD = getpass.getpass()
        except:
            print('Error al introducir alguno de los datos')
            sys.exit(1)

        try:
            # Conectamos por SSH
            self.CLIENT = paramiko.SSHClient()
            self.CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.CLIENT.load_system_host_keys()
            self.CLIENT.connect(
                hostname=self.HOST,
                username=self.USERNAME,
                password=self.PASSWORD
            )
        except:
            print('Error en la conexión')
            sys.exit(1)

        # Invocamos el shell para ejecutar comandos remotos
        try:
            shell = self.CLIENT.invoke_shell()
            try:
                # Ejecutamos el comando remoto
                stdin, stdout, stderr = self.CLIENT.exec_command(
                    'uname -a',
                    bufsize=-1,
                    timeout=None,
                    get_pty=True,
                    environment=None
                )

                # Mostramos la salida estándar línea por línea
                for line in iter(stdout.readline, ""):
                    print(line, end="")
            except:
                print('Error al ejecutar el comando')
                sys.exit(1)
        except:
            print('Error en la conexión por SSH')
            sys.exit(1)

        # Cerramos el shell
        shell.close()

        # Cerramos la conexión SSH
        self.CLIENT.close()

if __name__ == '__main__':
    ssh = Ssh()
    ssh.conecta()
