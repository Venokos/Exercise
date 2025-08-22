#创建列表
lst=['hello','world',123,98.6,'world',125,'world']
lst2=list(['hello','world',123,98.6,'world',125,'world'])
print(lst)
print(lst2)

#index函数查找索引

print(lst.index('world')) #查找重复元素，只输出第一个的索引。
print(lst.index(123))
'''print(lst.index('world',2,4))  会出现ValueError: 'world' is not in list
索引2和3均没有world'''

print(lst.index('world',1,4))

#根据索引查找元素
print(lst[3])
print(lst[-4])  #均应输出98.6

'''print(lst[10])报错，列表中没有索引为10的元素
IndexError: list index out of range'''


