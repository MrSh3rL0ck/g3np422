# instalar pip o pip3 werkzeug
# G3nP422 by: Mr.Sh3rl0ck {R4.Sh3.D3} [OMHE]

# importa librerias
import random
from werkzeug.security import generate_password_hash

print(
    """



  ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗  ██╗██████╗ ██████╗
██╔════╝ ╚════██╗████╗  ██║██╔══██╗██║  ██║╚════██╗╚════██╗
██║  ███╗ █████╔╝██╔██╗ ██║██████╔╝███████║ █████╔╝ █████╔╝
██║   ██║ ╚═══██╗██║╚██╗██║██╔═══╝ ╚════██║██╔═══╝ ██╔═══╝
╚██████╔╝██████╔╝██║ ╚████║██║          ██║███████╗███████╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝          ╚═╝╚══════╝╚══════
                              _|
                              _|
by: Mr.Sh3rl0ck [R4.Sh3.D3] [OMHE]

"""
)

# Variables
# minus = "abcdefghijklmnñopqrstuvwxyz"
# mayus = minus.upper()
# simbolos =
numeros = "123456789"

# define que elementos conformaran contraseña
base = numeros  # +minus+mayus+simbolos
# define longitud de password
longitud = 8

# define cantidad de passwords se generan
for _ in range(5):
   muestra = random.sample(base, longitud)
   password = "".join(muestra)

    #encripta password, comentar si solo se requiere contraseña sin enctiptar
   password_encriptado = generate_password_hash(password)
   print("{} ▬▶{}".format(password, password_encriptado))

   #Descomentar si solo se requieres contraseña sin encriptar
   # print(password)
