import sys

try:
    # Intentar obtener argumentos
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])

    # Validar división por cero
    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        load_per_support = total_load / num_supports
        print(f"Load per support point: {load_per_support:.2f} N")

except (IndexError, ValueError):
    print("Error: Invalid input! Enter numeric values only.")
