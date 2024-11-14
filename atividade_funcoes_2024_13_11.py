# exercício 1

def soma (s1,s2):
    soma = s1+s2
    return soma
    

# exercício 2

def converter_graus (celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

# exercício 3

def par_impar():
    """essa função vai falar com o usuario se o numero digitado é par ou impar"""
    num = int(input("por favor digite um numero: "))
    if num % 2 == 0:
        print("é um numero par")
    else:
        print("é um numero impar")
       
   
# exercício 4

def Inverter_string():
    '''essa função vai analizar a string digitada e ira invertela'''
    string =  input("por favor digite uma palavra: ")
    # No fatiamento de lista, geralmente há 3 fatores [x:y:z] x é o ponto inicial, y é o ponto final, z é o passo dado de x para y.
    # Um passo regular será 1, que percorre a lista normalmente, mas quando é -1, a lista dá seu passo para trás,
    # resultando em uma lista invertida
    string_invertida = string[::-1]
    print(string_invertida)

# def string_inverter_prof(texto):
#     texto = "quinta"
#     tm = len(texto)
#     # tm = tamanho (porque nao sabemos o tamanho do texto)
#     # len = pega quantidade *apenas quantidade*
#     print(tm)
#     print(texto)
#     print(tm)
#     for i in range(tm-1,-1,-1):
#         print(texto[i],end="")

# exercício 5

def palindromo(palavra):
    palavra = palavra.lower()
    cp_palavra = palavra
    if cp_palavra==inverter(palavra):
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
    
#  exercício 6

def media(lista_numeros):
    resultado = 0
    for i in lista_numeros:
        resultado += i
    return resultado / len(lista_numeros)

#  exercício 7

def lista_pares(lista_numeros):
    lst_pares = []
    for i in lista_numeros:
        if i % 2 ==0:
            lst_pares.append(i)
    return lst_pares



