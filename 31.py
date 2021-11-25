#Пробный Вариант
n=int(input("Сколько всего юношей/девушек?"))
p=[str(input("Введите имя юноши: ")) for i in range(n)]
d=[str(input("Введите имя девушки: ")) for i in range(n)]
#Заполнение вспомогательного массива
ind=[]
for i in range(n):
    ind.append(i)

print("1-ый способ")
g=[[0]*2 for i in range(n)]
for i in range(0,n):
    g[i][0]=p[i]
for j in range(0,n):
    g[j][1]=d[j]
print(g)

count=1
n_f=1
for i in range(2,n+1):
    n_f=n_f*i

while count<n_f:
    print(count+1,"-ый способ")
    #следующая
    k=n-2
    while ind[k]>ind[k+1]:
        k=k-1
    t=n-1
    while ind[t]<ind[k]:
        t=t-1
    #Обмен
    vspom=ind[k]
    ind[k]=ind[t]
    ind[t]=vspom
    #Конец Обмен
    le=k+1
    pr=n-1
    while le<pr:
        #Обмен
        vspom=ind[le]
        ind[le]=ind[pr]
        ind[pr]=vspom
        #Конец Обмен
        le+=1
        pr-=1
    #конец следующая

    #Печать
    g=[[0]*2 for i in range(n)]
    for i in range(0,n):
        g[i][0]=p[i]
    for j in range(0,n):
        g[j][1]=d[ind[j]]
    print(g)
    #конец Печать
    count+=1

