def calculadora(a, b, operacao):
    if operacao  == "+":
        soma = a + b
        print (soma)

    elif operacao == "-":
        sub = a - b
        print(sub)

    elif operacao == "*":
        mult = a * b
        print(mult)

    elif operacao == "/":
        div = a / b 
        print(div)

    else:
        print("Operação inválida")


calculadora(2,2,"+")

calculadora(100,50,"-")

calculadora(40,10,"*")

calculadora(20,2,"/")

calculadora(3,7,"Operação inválida")