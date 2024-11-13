def saudacao(nome=""):
    input(nome)
    print(f"Olá, {nome}! Seja Bem Vindo")

def soma (s1,s2):
    soma = s1+s2
    return soma
    

def converter_graus (celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def par_impar (resto):
    if resto % 2 == 0:
        print("Par")
    else:
        print("Impar")
    return par_impar





print(soma(33,18))
print(converter_graus(1))
par_impar(9)
par_impar(4)

