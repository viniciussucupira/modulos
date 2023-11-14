from meus_modulos.numeros.soma import somar
from meus_modulos.numeros.sub import subtrair
from meus_modulos.numeros.divisao import dividir
from meus_modulos.numeros.multiplicacao import multiplicar
def menu():
    while True:
        print("1 - somar")
        print("2 - Subtrair")
        print("3 - dividir")
        print("4 - multiplicar")
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(f"Resultado: {somar(a, b)}")
        elif opcao == "2":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == "3":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(f"Resultado: {dividir(a, b)}")
        elif opcao == "4":
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcao == "5":
            print("Você saiu da calculadora.")
            break
menu()