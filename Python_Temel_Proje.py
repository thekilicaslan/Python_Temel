# Python_Temel_Proje

# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

def flatten (p):

    for x in p:
        if isinstance(x,list):
            flatten(x)
        else:
            newlist.append(x)


p =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

newlist=[]

flatten(p)

print(newlist)


# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverse (q):
    for i in range(len(q)):
        (q[i])=(q[i])[::-1]

q=[[1, 2], [3, 4], [5, 6, 7]]

print(ters(q))