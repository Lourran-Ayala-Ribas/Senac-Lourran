'''Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Exponenciação
* 6. Raiz quadrada
* 7. Porcentagem
* 8. Resto da divisão
* 9. Divisão de inteiro
* 0. Sair do programa
*********************************************************************
Informe a opção desejada:

** Instruções**

- A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
- Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 0.
- Utilize funções para realizar os cálculos, inclusive para o menu.
- Utilize a estrutura de comparação que melhor se adeque ao problema.
- Mantenha o código fonte organizado.
- Não será aceito utilização de bibliotecas.
'''

def calculadora():
    while True:
        print("**********************************************************")
        print("*                     CALCULADORA                        *")
        print("**********************************************************")
        print("* [1]. Adição                                            *")
        print("* [2]. Subtração                                         *")
        print("* [3]. Multiplicação                                     *")
        print("* [4]. Divisão                                           *")
        print("* [5]. Exponenciação                                     *")
        print("* [6]. Raiz quadrada                                     *")
        print("* [7]. Porcentagem                                       *")
        print("* [8]. Resto da divisão                                  *")
        print("* [9]. Divisão de inteiro                                *")
        print("* [0]. Sair do programa                                  *")
        print("**********************************************************")

        opcao = input("Informe a opção desejada (com 1, 2, 3, 4, 5, 6, 7, 8, 9 ou 0 para sair do programa): ")

        if opcao == '1':
            print(adicao())
        elif opcao == '2':
            print(subtracao())
        elif opcao == '3':
            print(multiplicacao())
        elif opcao == '4':
            print(divisao())
        elif opcao == '5':
            print(exponenciação())
        elif opcao == '6':
            print(raiz_quadrada())
        elif opcao == '7':
            print(porcentagem())
        elif opcao == '8':
            print(resto_da_divisao())
        elif opcao == '9':
            print(divisao_de_inteiro())
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

def adicao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    return f"Resultado da adição: {resultado}\n"

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    return f"Resultado da subtração: {resultado}\n"


def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    return f"Resultado da multiplicação: {resultado}\n"


def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        return f"Resultado da divisão: {resultado}\n"
        
    else:
        return "Erro: Divisão por zero!"


def exponenciação():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 ** num2
    return f"Resultado da Exponenciação: {resultado}\n"


def raiz_quadrada():
    num = float(input("Digite o número para calcular a raiz quadrada: "))
    resultado = num ** 0.5
    return f"Resultado da Raiz Quadrada: {resultado}\n"


def porcentagem():
    num1 = float(input("Digite o valor total: "))
    num2 = float(input("Digite a porcentagem desejada (em %): "))
    resultado = (num1 * num2) / 100
    return f"A porcentagem de {num2}% de {num1} é: {resultado}\n"


def resto_da_divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 % num2
    return f"O resto da divisão de {num1} por {num2} é: {resultado}\n"


def divisao_de_inteiro():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 // num2
    return f"A divisão de inteiros de {num1} por {num2} é: {resultado}\n"
calculadora()
