def factorial(n):
    \"\"\"Calcula factorial de n (iterativo).\"\"\" 
        raise ValueError('n debe ser un entero no negativo') 
    result = 1 
    for i in range(2, n+1): 
        result *= i 
    return result 
