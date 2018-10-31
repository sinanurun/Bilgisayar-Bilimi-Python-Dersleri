def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Soldaki çocuk ile root karşılaştırması
    if l < n and data[i] < data[l]:
        largest = l

    # sağdaki çocuk ile root karşılaştırması
    if r < n and data[largest] < data[r]:
        largest = r

    # ihtiyaç halinde root değişimi
    if largest != i:
        data[i], data[largest] = data[largest], data[i]


        heapify(data, n, largest)


# verilen boyuttaki dizinin ana işlemleri
def heapSort(data):
    n = len(data)

    # en büyük değeri bulma işlemi
    for i in range(n, -1, -1):
        heapify(data, n, i)

    # tek tek eleman işlemleri
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        print(data)

# listelenecek liste tanımı
numList = [5, 8, 1, 6, 3, 7, 2, 4, 9]
print('Sıralama öncesi:')
print(numList)

print("\nişlemler\n")
heapSort(numList)
print('\nsıralama sonrası:')
print(numList)