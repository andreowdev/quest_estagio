def fibonacci(number):
    if number == 0 or number == 1:
        return True

    a, b = 0, 1
    while b < number:
        a, b = b, a + b

    return b == number

# Número para verificar
numero = int(input("Informe um número para verificar se está na sequência de Fibonacci: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

