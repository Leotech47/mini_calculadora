import math

while True:
    print("\nOperações disponíveis:")
    print(" + : Soma")
    print(" - : Subtração")
    print(" * : Multiplicação")
    print(" / : Divisão")
    print(" ^ : Potência")
    print(" % : Módulo")
    print(" r : Raiz quadrada")
    print(" sair : Encerrar a calculadora")
    
    operacao = input("\nEscolha a operação: ").lower()
    
    if operacao == "sair":
        print("Encerrando a calculadora. Até mais!")
        break
    
    # Para raiz quadrada, só é necessário um número
    if operacao == "r":
        a = float(input("Digite o número para calcular a raiz quadrada: "))
        if a >= 0:
            resultado = math.sqrt(a)
        else:
            resultado = "Erro: número negativo não tem raiz quadrada real"
    
    else:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        if operacao == "+":
            resultado = a + b
        elif operacao == "-":
            resultado = a - b
        elif operacao == "*":
            resultado = a * b
        elif operacao == "/":
            resultado = a / b if b != 0 else "Erro: divisão por zero"
        elif operacao == "^":
            resultado = a ** b
        elif operacao == "%":
            resultado = a % b
        else:
            resultado = "Operação inválida"
    
    print("Resultado:", resultado)
