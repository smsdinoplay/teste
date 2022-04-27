"""
Mod JSON
"""

# importar modulo
import json

filename = 'day-5/username.json'

name = ''

# Procura um arquivo de histórico 
try:
    with open(filename, 'r') as r:
        
        # Carrega o nome do usuário do arquivo de histórico 
        name = json.load(r)
        
        #print(name)
    
except IOError:
    print("Primeiro login")

# Se o usuário foi encontrado no arquivo de histórico, dar as boas-vindas de volta 
if name != "": 
    print("Bem-vindo de volta, " + name + "!")
else: 
    # Se o arquivo de histórico não existir, pedir o nome ao usuário 
    name = input("Olá! Qual é o seu nome? ")