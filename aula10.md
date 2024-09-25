# Funções Python - P1

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses podem ou não ter valores padrões.

## Retornando valores

Para retornar um valor, utilizamos a palavra reservada return. Toda função retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

```
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10, 20, 34])
retorna_antecessor_e_sucessor(10)
```
## Argumentos nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

## Args e kwargs

Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

### Exemplo
```
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{,eta_dados}"
    print(mensagem)
```

## Parâmetros especiais

Por padrão, argumentos podem ser passados para uma funcão Python tanto por posição quanto explicitamente pelo nome.

#### Sintaxe
```
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```
