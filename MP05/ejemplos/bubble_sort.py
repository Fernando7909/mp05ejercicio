import random
import time
import heapq


def bubble_sort(lista):
    """
    Implementación básica del algoritmo Bubble Sort.
    Recorre repetidamente la lista, intercambiando
    los elementos adyacentes si están en el orden equivocado.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def main():
    # 1. Generar la lista de 10,000 números aleatorios
    numeros = [random.randint(1, 100000) for _ in range(10000)]

    # --------------------------------------------------------------------
    # A) Ordenar con Bubble Sort
    # --------------------------------------------------------------------
    # Copiamos la lista para no afectar la original
    numeros_bubble = numeros[:]

    inicio_bs = time.time()
    bubble_sorted = bubble_sort(numeros_bubble)
    fin_bs = time.time()

    tiempo_bubble = fin_bs - inicio_bs
    print(f"Tiempo de ejecución con Bubble Sort: {tiempo_bubble:.6f} segundos")

    # --------------------------------------------------------------------
    # B) Ordenar con Heap (heapq)
    # --------------------------------------------------------------------
    # Copiamos la lista para no afectar la original
    numeros_heap = numeros[:]

    inicio_heap = time.time()
    # 1. Convertir la lista en un heap
    heapq.heapify(numeros_heap)  # O(n)
    # 2. Extraer todos los elementos en orden (menor a mayor)
    heap_sorted = [heapq.heappop(numeros_heap) for _ in range(len(numeros_heap))]  # O(n log n)
    fin_heap = time.time()

    tiempo_heap = fin_heap - inicio_heap
    print(f"Tiempo de ejecución con Heap (heapq): {tiempo_heap:.6f} segundos")

    # --------------------------------------------------------------------
    # (Opcional) Verificación de correcto ordenamiento
    # --------------------------------------------------------------------
    # Imprimimos los primeros 10 elementos para verificar
    # print("Bubble Sort (primeros 10):", bubble_sorted[:10])
    # print("Heap Sort   (primeros 10):", heap_sorted[:10])


if __name__ == "__main__":
    main()