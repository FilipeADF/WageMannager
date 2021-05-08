from SalarioLiquido import calcularsalarioliquido
def calculardecimoterceiro ():

    try:

        salarioliquido = (calcularsalarioliquido())
        mesestrabalhados = int(input('Digite aqui a quantidade de meses trabalhado:'))

        if mesestrabalhados >12:
            print ('\nO tempo trabalhado deve ser entre os 12 meses!')
        elif mesestrabalhados <1:
            print ('\nO tempo trabalhado deve ser entre os 12 meses!')
        else:
            decimoterceiro = (mesestrabalhados * (salarioliquido / 12))
            print (f'\nO décimo terceiro bruto é R${decimoterceiro:.2f}')

    except (ValueError):
        print('O valor deve ser numérico!')
        calculardecimoterceiro()


