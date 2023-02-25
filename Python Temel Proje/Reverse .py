#2-Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa
#onların elemanlarını da tersine döndürün. Örnek olarak:

#input: [[1, 2], [3, 4], [5, 6, 7]]
#output: [[[7, 6, 5], [4, 3], [2, 1]]

list2 = [[1, 2], [3, 4], [5, 6, 7]]  

def reverse_list(l):
    l.reverse()
    for sublist in l:
        if type(sublist) == list:
            reverse_list(sublist)

reverse_list(list2)
print(list2)