'''Faça um programa de calculadora simples com as seguintes operações
possíveis: adição, subtração, multiplicação e divisão. O programa inicia
apresentando ao usuário um menu de opções como mostrado abaixo:

**********************************************************************
* Calculadora. Opções possíveis:
* 1. Adição
* 2. Subtração
* 3. Multiplicação
* 4. Divisão
* 5. Sair do programa
*********************************************************************
Informe a opção desejada:


A opção informada é então analisada e o programa executa a operação apropriada,
se a opção for inválida, informe ao usuário e peça a ele para entrar com uma
opção válida.
Após a execução da operação o programa volta a apresentar o menu inicial até
que o usuário encerre o programa com a opção 5.'''

while True:
    print("**********************************************************")
    print("* Calculadora. Opções possíveis:                         *")
    print("* [1]. Adição                                            *")
    print("* [2]. Subtração                                         *")
    print("* [3]. Multiplicação                                     *")
    print("* [4]. Divisão                                           *")
    print("* [5]. Sair do programa                                  *")
    print("**********************************************************")

    opcao = input("Informe a opção desejada(com 1,2,3,4 ou 5 para sair do programa): ") 
    
    if opcao == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado da adição:{resultado}\n")
    elif opcao == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado da subtração:{resultado}\n")
    elif opcao == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"Resultado da multuplicação:{resultado}\n")
    elif opcao == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão:{resultado}\n")
        else:
            print("Erro: Divisão por zero!\n")
    elif opcao == '5':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.\n")