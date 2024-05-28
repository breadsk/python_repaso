
def sumar(op1,op2):
    print(f"El resultado de la suma es: {op1+op2}")
def restar(op1,op2):
    print(f"El resultado de la resta es: {op1-op2}")
def restar(op1,op2):
    print(f"El resultado de la multiplicacion es: {op1*op2}")
def dividir(op1,op2):
    try:
        print(f"El resultado de la división es: {op1//op2}")
    except ZeroDivisionError:
        print("No se puede dividir por cero")