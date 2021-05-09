from SalarioLiquido import calcularsalarioliquido

def calculardecimoterceiro (salarioBruto, mesesTrabalhados):


    decimoterceiro = (mesesTrabalhados * (salarioBruto / 12))
    salarioliquido = (calcularsalarioliquido(decimoterceiro))

    return (salarioliquido)

def calculaEprintaDecimoTerceiro():
    salarioBruto = float(input("Digite o salario bruto: "))

    if (salarioBruto >= 1100):

        mesesTrabalhados = float(input("Digite a quantidade de meses trabalhado:"))

        if(mesesTrabalhados < 1 or mesesTrabalhados > 12):

            print("O Décimo Terceiro requere no mínimo um mês trabalhado, e no máximo 12")
            calculaEprintaDecimoTerceiro()

        else:
            print(f"\n--- O valor do décimo terceiro salário liquido é: "
                  f"R${calculardecimoterceiro(salarioBruto, mesesTrabalhados):.2f} ---\n")


    else:
        print("O salário minimo é R$1100,00")
        calculaEprintaDecimoTerceiro()



