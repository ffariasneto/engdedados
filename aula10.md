# Listas
Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizandoo o contrutor list, a função range ou colocando valores separados por vírgula dentro de colchetes; Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

## Acesso direto
A lista é uma sequência, portando podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

## Índices negativos
Sequências suportam indexação negativa. A contagem começa em -1.

## Listas aninhadas
Listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

## Fatiamento
Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

## Iterar listas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.

## Função enumerate
Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

### Exemplo
```
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```
## Compreensão de listas
A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

### Filtro versão 1
```
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
    pares.append(numero)
```
### Filtro versão 2
```
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
```
## Métodos da classe list
[].append - adicionar item no fim da lista
[].clear - limpar uma lista
[].copy - copiar uma lista
[].count - contar obejtos numa lista
[].extend - 
[].index
[].pop - remove item no fim da lista, caso não informe um índice
[].remove
[].reverse
[].sort - lista em ordem alfabética
[].sort(reverse=True) - reverte a ordem da lista
[].sort(key=lambda x: len(x)) - lista em ordem crescente
[].sort(key=lambda x: len(x), reverse=True)
len() - quantidade de objetos numa lista

# Tuplas
Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses.

## Acesso a tupla
Praticamente igual a listas.

# Conjuntos
## Criando sets
Um set é uma coleção que não possui objetos repetidos, usamos set para representar conjunots matemáticos ou eliminar itens duplicados de um iterável.

## Acessando os  dados
Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

## Função enumerate
Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

## Métodos da classe set
{}.union
{}.intersection
{}.difference
{}.symmetric_difference
{}.issubset
{}.issuperset
{}.isdisjoint
{}.add
{}.clear
{}.copy
{}.discard
{}.pop
{}.remove
len
in

# Dicionários
## Criação e acesso aos dados
Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.
```
pessoa = {"nome": "Francisco", "idade": 38}

pessoa = dict(nome="Francisco", idade=38)

pessoa["telefone"] = "3333-1234"
```
## Acesso aos dados
## Dicionários aninhados
Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números).
## Iterar dicionários
A forma mais comum para percorrer os dados de um dicionário é utilziando o comando for.
## Métodos da classe dict
{}.clear
{}.copy
{}.fromkeys
{}.get
{}.items
{}.keys
{}.pop
{}.popitem
{}.setdefault
{}.update
{}.values
in
del
