def faixa1():
    descontoINSS = (0.075 * 1100.0)
    return descontoINSS
def faixa2():
    descontoINSS = (0.09 * 1103.60)
    return descontoINSS
def faixa3():
    descontoINSS = (0.12 * 1101.80)
    return descontoINSS


def calcularsalarioliquido():
    try:
        salarioBruto = float(input("Digite o salario bruto: "))
        descontoINSS = 0.0
        descontoIRRF = 0.0

        if(salarioBruto >= 1100.00):
            if(salarioBruto == 1100.00):
                calculoTotal = salarioBruto - faixa1()
                return calculoTotal

            elif(salarioBruto > 1100.00 and salarioBruto <2203.45):
                descontoINSS = faixa1() + (0.09 * (salarioBruto - 1100.0))
                calculoTotal = salarioBruto - descontoINSS

                if(calculoTotal >= 1903.99):
                    descontoIRRF = (0.075 * calculoTotal)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = calculoTotal - descontoIRRF
                return calculoTotal

            elif(salarioBruto >= 2203.49 and salarioBruto <= 3305.22):
                descontoINSS = faixa1() + faixa2() + (0.12 * (salarioBruto - 2203.49))
                calculoTotal = salarioBruto - descontoINSS

                if(calculoTotal >= 2826.66):
                    descontoIRRF = (0.15 * calculoTotal)
                    descontoIRRF = descontoIRRF - 354.80
                else:
                    descontoIRRF = (0.075 * calculoTotal)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = calculoTotal - descontoIRRF
                return calculoTotal

            elif(salarioBruto >= 3305.23 and salarioBruto <6433.57):
                descontoINSS = faixa1() + faixa2() + faixa3() + (0.14 * (salarioBruto - 3305.23))
                calculoTotal = salarioBruto - descontoINSS

                if(calculoTotal >= 3751.06 and calculoTotal <= 4664.68):
                    descontoIRRF = (0.225 * calculoTotal)
                    descontoIRRF = descontoIRRF - 636.13
                elif(calculoTotal >= 4664.69):
                    descontoIRRF = (0.275 * calculoTotal)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * calculoTotal)
                    descontoIRRF = descontoIRRF - 354.80


                calculoTotal = calculoTotal - descontoIRRF
                return calculoTotal

            elif(salarioBruto > 6433.57):
                descontoINSS =  751.99
                calculoTotal = salarioBruto - descontoINSS

                if(calculoTotal >= 4664.69):
                    descontoIRRF = (0.275 * calculoTotal)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * calculoTotal)
                    descontoIRRF = descontoIRRF - 354.80

            calculoTotal = calculoTotal - descontoIRRF
            return calculoTotal

        else:
             print("Valor invalido, o salário minimo é R$1100.00")
             calcularsalarioliquido()

    except ValueError:
            print("Valor invalido")
            calcularsalarioliquido()


