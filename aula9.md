# Interpolação de variáveis
Em Python temos 3 formas de interpolar variáveis em strings.

## Old style %
```
nome = "Francisco"
idade = 38
profissao = "Administrador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
```
## Método format
```
nome = "Francisco"
idade = 38
profissao = "Administrador"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
```
## f-string
```
nome = "Francisco"
idade = 38
profissao = "Administrador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
```
## Formatar strings com f-string
```
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:10.2f})
```
# Fatiamento de Strings
É uma técnica utilizada para retornar substrings (partes da string original), informando início (start), fim (stop) e passo (step): [start: stop[, step]]

# String Múltiplas linhas
