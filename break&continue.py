


#二重循环中的break与continue
#break和continue只控制本层循环
#break：跳出本层循环，往下运行 continue：


for i in range(5):#表示外层循环要循环五次
    for j in range(1,11):
        if j%2==0:
            break #若为True，跳出循环并往下运行
        print(j)
for i in range(5):#表示外层循环要循环五次
    for j in range(1,11):
        if j%2==0:
            continue #若为True，结束本次循环并回到本层循环开头
        print(j,end='\t')
    print()