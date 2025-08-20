def evaluate_functions(x):
    f = math.cos(2 * x)        
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)  
    return f, f_prime, f_double_prime
x_value = math.pi
results = evaluate_functions(x_value)
print("f(pi) =", results[0])
print("f'(pi) =", results[1])
print("f''(pi) =", results[2])