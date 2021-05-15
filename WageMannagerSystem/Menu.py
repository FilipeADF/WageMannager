from SalarioLiquido import calculaPrintaSalarioLiquido
from FeriasLiquido import calculaEprintaFeriasLiquido
from DecimoTerceiro import calculaEprintaDecimoTerceiro

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
                print("Selecione uma opção valida")


            elif resp == 1:
                calculaPrintaSalarioLiquido()

            elif resp == 2:
                calculaEprintaFeriasLiquido()

            elif resp == 3:
                calculaEprintaDecimoTerceiro()

            elif resp == 0:
                break

        except ValueError:
            print("Apenas números são validos")


