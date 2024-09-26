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