import time

def suma_objetivo(lista, objetivo):
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == objetivo:
                return True
    return False

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    lista_larga = [i for i in range(10000)]
    objetivo = 9

    resultado = suma_objetivo(lista, objetivo)
    print(f"Lista {lista} - objetivo {objetivo}: {resultado}")

    print("\nProbando con 10,000 numeros...")
    inicio = time.perf_counter()
    suma_objetivo(lista_larga, objetivo)
    final = time.perf_counter()

    print(f"Tiempo de ejecucion: {final - inicio:.6f} segundos")