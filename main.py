def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    numb = input("Digite o número a verificar, sem espaços:")
    if numb == numb[::-1]:
        print("True")
    else:
        print("False")


def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    """
    #Dado um numeral romano, converta-o para um número inteiro
    user = input("")
    romanos = [1,5,10,50,100,500,1000]
    I,V,X,L,C,D,M = romanos
    b = 0
    for i in user:
        b +=(romanos[i])
    print(b)
    #Rasnho

def q3():
    numb = int(input("Digite um número:"))
    contador = 1

    while contador / numb:
        print(f"Contador: {contador}")
        contador += 1
    #Rascunho

def q4():
    n1 = int(float(input("Digite um número:")))
    n2 = int(float(input("Digite um número:")))
    soma = 0
    for i in range(n1, n2):
        print(i)
        #Rascunho

    

