from SalarioLiquido import calcularsalarioliquido
from FeriasLiquido import feriasLiquido
from DecimoTerceiro import calculardecimoterceiro

def menu():
    cont = 10
    while(cont > 0):
        try:
            print("---WAGE MANNAGER---\n")
            print("Selecione uma opção:\n")
            print("[1] - Calculo de Salário Liquido\n")
            print("[2] - Calculo de Férias Liquido\n")
            print("[3] - Calculo de Décimo Terceiro Liquido\n")
            print("[0] - Sair do Programa\n")

            resp = int(input())

            if resp != 1 and resp != 0 and resp != 2 and resp!= 3:
                print("Digite uma posição correta!")
                menu()

            elif resp == 1:
                   dec = calcularsalarioliquido()
                   print(f"\n--- O valor do salario liquido é: R${dec:.2f}---\n")

            elif resp == 2:
                    feriasLiquido()

            elif resp == 3:
                calculardecimoterceiro()

            elif resp == 0:
                break

        except ValueError:
            print("Apenas numeros")
            menu()