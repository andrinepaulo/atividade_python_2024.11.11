n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = int(input("Digite o terceiro número"))

if n1 >= n2 or n1 >= n3:
    print("O maior é ",n1)
elif n2 >= n1 or n2 >= n3:
    print("O maior é ",n2)
else:
    print("O maior é ",n3)