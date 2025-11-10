def producto_excepto_yo(nums):
    """
    Devuelve una lista donde cada posición contiene
    el producto de todos los elementos menos el propio.
    Complejidad: O(n) tiempo, O(1).
    """
    n = len(nums)
    salida = [1] * n

    # Productos prefix
    prefix = 1
    for i in range(n):
        salida[i] *= prefix
        prefix *= nums[i]

    # Productos suffix
    suffix = 1
    for i in range(n - 1, -1, -1):
        salida[i] *= suffix
        suffix *= nums[i]

    return salida


if __name__ == "__main__":
    arreglo = [2, 3, 4, 5, 1]
    resultado = producto_excepto_yo(arreglo)
    print("Entrada:", arreglo)
    print("Salida:", resultado)
