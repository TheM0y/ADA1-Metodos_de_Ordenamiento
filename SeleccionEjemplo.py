import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Intercambio en posición {i} y {min_idx}: {arr}")
            time.sleep(1)

entrada = input("Ingresa palabras separadas por espacios: ")
lista = entrada.split()
selection_sort(lista)
print("Lista ordenada:", lista)
