import json

# Carrega arquivo JSON #
with open(r'.\dados.json', 'r') as json_file:
    dados = json.load(json_file)

# Mostra resultados #
print(dados)
print('\n')
print('Nome: ' + dados['nome'])
print('Insta: ' + dados['instagram'])
print('Linguagem: ' + dados['linguagem'])