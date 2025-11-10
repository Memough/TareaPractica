def rotar_derecha(nums, k):
    """
    Rota el arreglo nums hacia la derecha k posiciones.
    Usa el método de las tres inversiones.
    Complejidad: O(n) tiempo, O(1).
    """
    n = len(nums)
    if n == 0:
        return nums

    k %= n

    # Función para invertir parte del arreglo
    def invertir(lista, inicio, fin):
        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1

    # invertir todo
    invertir(nums, 0, n - 1)
    # invertir primeros k elementos
    invertir(nums, 0, k - 1)
    # invertir los restantes
    invertir(nums, k, n - 1)
    return nums

if __name__ == "__main__":
    arreglo = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", arreglo)
    rotar_derecha(arreglo, k)
    print("Rotado  :", arreglo)
