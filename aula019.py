'''
DICIONÁRIOS

- estruturas de dados com índices personalizados;
- Tuplas: ()
- Listas: []
- Dicionários: {}

*declaração:
dados = dict()
dados = {'Nome': 'Pedro', 'idade': 25}
print(dados['Nome']) -> Pedro
print(dados['idade']) -> 25

*Para adicionar elemento:
dados['sexo'] = 'M'

*Para excluir elemento:
del dados['idade']

*Exemplo
filme = { 'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
        }

 print(filme.values()) -> exibe os valores
 print(fime.keys()) -> exibe o nome das chaves
 print(filme.items()) -> exibe tudo
'''

'''pessoas = {'nome': 'Felipe', 'sexo': 'M', 'idade': 33}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Siga do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

