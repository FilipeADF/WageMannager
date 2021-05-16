def faixa1():
    desconto = (0.075 * 1100.0)
    return desconto
def faixa2():
    desconto = (0.09 * 1103.60)
    return desconto
def faixa3():
    desconto = (0.12 * 1101.80)
    return desconto


def calcularsalarioliquido(salarioBruto):

        descontoINSS = 0.0
        descontoIRRF = 0.0

        if(salarioBruto >= 1100.00):
            if(salarioBruto == 1100.00):
                calculoTotal = salarioBruto - faixa1()
                print(F"Desconto INSS: R${faixa1():.2f}" + " ({0:.2f}%)".format(descontoINSS/calculoTotal * 100))
                return calculoTotal

            elif(salarioBruto > 1100.00 and salarioBruto <2203.45):
                descontoINSS = faixa1() + (0.09 * (salarioBruto - 1100.0))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 1903.99):
                    descontoIRRF = (0.075 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = salarioDescontadoINSS - descontoIRRF


                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto >= 2203.49 and salarioBruto <= 3305.22):
                descontoINSS = faixa1() + faixa2() + (0.12 * (salarioBruto - 2203.49))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 2826.66):
                    descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80
                else:
                    descontoIRRF = (0.075 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = salarioDescontadoINSS - descontoIRRF

                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto >= 3305.23 and salarioBruto <6433.57):
                descontoINSS = faixa1() + faixa2() + faixa3() + (0.14 * (salarioBruto - 3305.23))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 3751.06 and salarioDescontadoINSS <= 4664.68):
                    descontoIRRF = (0.225 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 636.13
                elif(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80


                calculoTotal = salarioDescontadoINSS - descontoIRRF

                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto > 6433.57):
                descontoINSS =  751.99
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80

            calculoTotal = salarioDescontadoINSS - descontoIRRF

            print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
            print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
            return calculoTotal


def calcularDescontos(salarioBruto):

    descontoINSS = 0.0
    descontoIRRF = 0.0

    if(salarioBruto >= 1100.00):
        if(salarioBruto == 1100.00):
            calculoTotal = salarioBruto - faixa1()

            return faixa1(), descontoIRRF

        elif(salarioBruto > 1100.00 and salarioBruto <2203.45):
            descontoINSS = faixa1() + (0.09 * (salarioBruto - 1100.0))
            salarioDescontadoINSS = salarioBruto - descontoINSS

            if(salarioDescontadoINSS >= 1903.99):
                descontoIRRF = (0.075 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 142.80

            calculoTotal = salarioDescontadoINSS - descontoIRRF


            return descontoINSS, descontoIRRF

        elif(salarioBruto >= 2203.49 and salarioBruto <= 3305.22):
            descontoINSS = faixa1() + faixa2() + (0.12 * (salarioBruto - 2203.49))
            salarioDescontadoINSS = salarioBruto - descontoINSS

            if(salarioDescontadoINSS >= 2826.66):
                descontoIRRF = (0.15 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 354.80
            else:
                descontoIRRF = (0.075 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 142.80

            calculoTotal = salarioDescontadoINSS - descontoIRRF

            return descontoINSS, descontoIRRF


        elif(salarioBruto >= 3305.23 and salarioBruto <6433.57):
                descontoINSS = faixa1() + faixa2() + faixa3() + (0.14 * (salarioBruto - 3305.23))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 3751.06 and salarioDescontadoINSS <= 4664.68):
                    descontoIRRF = (0.225 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 636.13
                elif(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80


                calculoTotal = salarioDescontadoINSS - descontoIRRF

                return descontoINSS, descontoIRRF


        elif(salarioBruto > 6433.57):
                descontoINSS =  751.99
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80

                calculoTotal = salarioDescontadoINSS - descontoIRRF


                return descontoINSS, descontoIRRF


def calculaPrintaSalarioLiquido():
    salarioBruto = float(input("Digite o salario bruto: "))
    if (salarioBruto >= 1100):
        print(f"\n--- O valor do salario liquido é: "
              f"R${calcularsalarioliquido(salarioBruto):.2f} ---\n")
    else:
        print("O salário minimo é R$1100,00")
        calculaPrintaSalarioLiquido()





