# list=[10,20,30,40,50,60,70]
# print(list[1:4])
# print(list[:3])
# print(list[4:])
# print(list[: :2])
# print(list[::-1])

# horsemen = ["war","famine","pestilence","live"]
# k=int(input("jay shree ram"))
# i = 0
# while i < 4:
#     if i == k:
#         print(horsemen[i])
#     i = i+1


# for number in range (20):
#     if number%2==0:
#         print(number)






# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# d = a+b+c
# print(d)


# a = [1,2,3]
# b = 3*a
# print(b)


# list = ['a','b','c','d','e','f','g']
# list[1:3] = ['x','y']
# print(list)



# fruit = ["banana","apple","quince"]
# fruit[0] = "pear"
# fruit[-1] = "orange"
# print(fruit)


# a = ['one','two','three']
# del a[1]
# print(a)

# list = ['a','b','c','d','e']



# c = 'banana'
# d = 'banana'
# print(id(c))
# print(id(d))
# a = [1,2,3,4,5,6]
# b = [1,2,3,4,5,6]
# print(id(a))
# print(id(b))


# def tail(list):
#     return list[11:]
# numbers = [1,2,3]
# rest = tail(numbers)
# print (rest)


# list = ["hello",2.0,5,[10,20]]
# elt = list[3]
# ind = elt[1]
# elt1 = list[3][1]
# print (elt)
# print (ind)
# print (elt1)



# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[1])
# print(matrix[1][1])


# import string
# song ="The rain in Spain..."
# print(song.split())
# print(song.split('ai'))
# print(song.split('',2))


# list = ['The', 'rain', 'in', 'Spain...']
# sent  = "".join(list)
# print(sent); print(type(sent))


# list = ['1', '8', '2', '9...']
# sent1  = "_".join(list)
# print(sent1)


# a=[10,20,30,]
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))
# a.sort()
# print(a)
# a.reverse()
# print(a)



# a=[10,20,30]
# b=a.count(10)
# print(b)
# c=a.index(10)
# print(c)
# a.remove(10)
# print(a)
# a.append(10)
# print(a)
# a.insert(2,30)
# print(a)




# Mlist = [10,20,30]
# tuple_from_list = (Mlist)
# print(tuple_from_list)
# Mstring= "python" #string
# tuple_from_string=tuple(Mstring)
# print(tuple_from_string)


# my_tuple = 1,2,"three"
# print(my_tuple)





# thistuple = ("krishan",)
# print(type(thistuple))



# thistuple = ("krishan")
# print(type(thistuple)




# thistuple = ("apple","banaba","cherry")
# y = ("chandg",)
# thistuple+= y
# print(thistuple)




# Mtuple=("apple","banana","cherry")
# y=list(Mtuple)
# y.remove("apple")
# Mtuple = tuple(y)
# print(Mtuple)

# tuple1= ("a","b","c")
# tuple2 = (1,2,3)
# tuple3=tuple1+tuple2
# print(tuple3)



# thistuple=(1,2,3,4,5,6,7,8,9)
# x=thistuple.count(5)
# y=thistuple.index(8)
# print(x)
# print(y)





# d =  {1:'geeks',2:'for',3:'geeks','age':22}
# key,val = d.popitem()
# print(f"key:{key},Value:{val}");print(d)

# d={1:'geeks',2:'for',3:'geeks','age':22}
# print('age'in d)



# def create_sparse_matrix_dict(matrix):
#     sparse_matrix = {}
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] != 0:
#                 sparse_matrix[(i, j)] = matrix[i][j]
#     return sparse_matrix  

# dense_matrix = [
#     [1, 0, 0, 0],
#     [0, 0, 3, 0],
#     [0, 0, 0, 4]
# ]

# sparse_dict = create_sparse_matrix_dict(dense_matrix)
# print(sparse_dict)



# letter_counts={}
# s="jhgskjHFIVZDFJbkZHJcjh"
# for letter in s:
#     letter_counts[letter]=letter_counts.get(letter,0)+1
# print(letter_counts)
# sorted_by_key_desc=4


# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# print(a.shape)



# import numpy
# a = numpy.array([[1,2,3],[4,5,6]])
# print(a.shape)
# print(a.size)
# print(type(a))




# import numpy as np
# a = np.array([[1,2,3]])
# a.shape = (3,1)
# print (a)



# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(3,2)
# print (b);print (a.itemsize)




# import numpy as np
# array_3d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# reshaped_array_3d = array_3d.reshape((2, 2, 2))
# print("Reshaped 3D array by vivek yadav:\n", reshaped_array_3d)



# import numpy as np
# x = np.arange(10,20,2)
# y = np.arange(10,130,70,dtype=np.int32)
# print( x)
# print( y)



# import numpy as np
# a = np.arange(11)
# print (a)




# import numpy as np
# a = np.arange(24)
# print(a.ndim)
# 1
# #now reshape it
# b = a.reshape(2,2,2,3)
# print( b)
# print(b.ndim)






# import numpy as np
# x = np.array([1,2,3,4,5], dtype = np.int8)
# y = np.array([1,2,3,4,5], dtype = np.int16)
# print( x.itemsize)
# print( y.itemsize)






# import numpy as np
# x = np.array([1,2,3,4,5])
# print(x.itemsize)




# import numpy as np
# x = np.empty([3,2])
# print (x)
# print(x.itemsize)


# import numpy as np
# x = np.zeros(3)
# print (x)


# import numpy as np
# x = np.zeros(5, dtype = np.int_)
# print (x)


# import numpy as np
# x = np.zeros((3,2), dtype = np.int_)
# print (x)




# import numpy as np
# x = np.linspace(10,20,5)
# print (x)
# y = np.linspace(10,20,5, retstep=True)
# print (y)
# y = np.linspace(10,20,5, endpoint=False)
# print (y)




# import numpy as np
# a = np.array([[3,7,5],[8,4,3],[2,4,9]])
# print(np.ptp(a))
# print(np.ptp(a,axis=1))
# print(np.ptp(a,axis=0))




# import numpy as np
# data = np.array([3, 5, 8, 6])
# weights = np.array([0.5, 0.3, 0.2, 0.5])
# weighted_avg = np.average(data, weights=weights)
# print(weighted_avg)



# import numpy as np
# data = np.array([3,5,8,6])
# deviation = np.std(data)
# print(deviation)




# import numpy as np
# data = np.array([3,4 ,8,6])
# variance = np.var(data)
# print(variance)




# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([1,2,3])
# c = a + b
# print(c)




# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1],[2]])
# c = a + b
# print(c)



# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([1,2,3])
# c = a * b
# print(c)



# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1],[2]])
# c = a * b
# print(c)


# import pandas as pd
# import numpy as np
# data = np.array(['a','b','c','d'])
# s1=pd.Series(data) 
# print(s1)
# s2 = pd.Series(data,index=[11,12,13, 14]) 
# print( s2)




# import pandas as pd
# data = {'a':0,'b':1,'c':2}
# s = pd.Series(data)
# print( s)

# import pandas as pd
# data = {'a':0,'b':1,'c':2,'f':3}
# s = pd.Series(data,index=['b','c','d','a','e'])
# print( s)




# import pandas as pd
# import numpy as np
# data=np.array([1, 2, 3, 4])
# s=pd.Series(data,index=['a', 'b', 'c','d'])
# print(s[0]);
# print(s[:3]); print(s[2:4])



# import pandas as pd
# data=[1,2,3,4,5]
# d1=pd.DataFrame(data)
# print(d1)


# import pandas as pd
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'])
# print (df)


# import pandas as pd
# data={'Name': ['milkha', 'sukho', 'ram','radha'], 'Age': [49,39,55,45]}
# d1=pd.DataFrame(data,index=['Student1', 'Student2', 'Student3','student4'])
# print(d1)



# import pandas as pd
# data=[{'a': 1, 'b': 2}, {'a': 5, 'b': 1020, 'c':4}]
# d1=pd.DataFrame(data)
# print(d1)


# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d)
# print (df ['one'])



# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d) ;
# df['three']=pd.Series([10,20,30],index=['a','b','c']); print(df)
# del df['one'] # deletion using del function
# print(df)
# df.pop('two') # using pop function
# print (df)




# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d) ; print(df)
# print( df.iloc[2])





# import pandas as pd
# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = pd.DataFrame(d) ; print(df)
# print( df[:2])
# print( df[2:4])



# import pandas as pd
# df1 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
# df3 = pd.concat([df1, df2])
# print (df1); print (df2); print (df3)



# import pandas as pd
# data = [['Akshit', 17, 'Delhi', 20000 ],['Dhruv',15, 'Mathura', 15000],['Jhalak',20, 'Delhi', 80000]]
# df = pd.DataFrame(data,columns=['Name','Age', 'City', 'Salary'])
# print(df)
# df.to_csv ( 'DataFrame.csv')