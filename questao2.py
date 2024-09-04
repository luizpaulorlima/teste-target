def sequenciaFibonacci(n):
    fibonacciNumber = [0, 1]
    while True:
        next_value = fibonacciNumber[-1] + fibonacciNumber[-2]
        if next_value > n:
            break
        fibonacciNumber.append(next_value)
    return fibonacciNumber

def ehFibonacci(num):
    fibonacciNumber = sequenciaFibonacci(num)
    return num in fibonacciNumber

numero = int(input("Digite um número inteiro: "))

if ehFibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
