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
    não foi dessa vez
    """



def q3():
    numb = int(input("Digite um número:"))
    divisores = 0

    for i in range(1,numb+1):
        if numb % i == 0 and i % 3 == 0:
            divisores += 1

        
    if divisores == 0:
        print("O número não possui divisores multiplos de 3")
    else:
        print(f"Quantidade de divisores divisiveis por 3: {divisores}")





def q4():
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite um número:"))
    soma = 0

    if n1 < n2:
        for i in range(n1, n2+1):
            if i > 0:
                soma += i
    else:
        for i in range(n2, n1+1):
            if i > 0:
                soma += i

    print(soma)

    

