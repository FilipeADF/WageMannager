def feriasLiquido():
    try:
        salarioLiquido = calcularsalarioliquido()
        descontoINSS = 0.0
        descontoIRRF = 0.0

        ferias = salarioLiquido + (salarioLiquido / 3);
        calculoTotal = calculoTotal - descontoIRRF
        return calculoTotal

    except ValueError:
        print("Valor invalido")
        feriasLiquido()


