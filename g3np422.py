# instalar pip o pip3 werkzeug
# G3nP422 by: Mr.Sh3rl0ck {R4.Sh3.D3} [OMHE]

# importa librerias
from __future__ import print_function, unicode_literals

import random

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

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

## Estilos de la versión interactiva 
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


## Opciones 
questions = [
    {
        'type': 'checkbox',
        'message': 'Que tipo de combinaciones deseas que tenga',
        'name': 'combinations',
        'choices': [
            Separator('=== |||||| ==='),
            {
                'name': 'Alfabeto minusculas'
            },
            {
                'name': 'Alfabeto mayusculas'
            },
            {
                'name': 'Simbolos'
            },
            {
                'name': 'Numeros'
            }
        ],
        'validate': lambda answer: 'Debes elegir almenos una validacion.' \
            if len(answer) == 0 else True
    },{
        'type': 'checkbox',
        'message': 'Como deseas tu contraseña',
        'name': 'combinations',
        'choices': [
            Separator('=== |||||| ==='),
            {
                'name': 'Encriptada'
            },
            {
                'name': 'Plana'
            },
        ],
        'validate': lambda answer: 'Debes elegir almenos una validacion.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)

# Variables, descomentar si se requiere agregar letras y  simbolos.
minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = minus.upper()
# simbolos =
numeros = "123456789"

# define que elementos conformaran la contraseña
base = numeros  # +minus+mayus+simbolos
# define longitud de password
longitud = 8

# define cantidad de passwords se generan
for _ in range(5):
   muestra = random.sample(base, longitud)
   password = "".join(muestra)

    #encripta password, comentar si solo se requiere contraseña sin encriptar
   password_encriptado = generate_password_hash(password)
   print("{} ▬▶{}".format(password, password_encriptado))

   #Descomentar si solo se requiere contraseña sin encriptar
   # print(password)
