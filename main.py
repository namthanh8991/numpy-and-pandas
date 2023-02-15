# Series([data, index, dtype, name, copy, . . . ])
#khong truyen index
import pandas as pd
s = pd.Series([0,1,2,3])
print(s)

#truyen index
import pandas as pd
s = pd.Series([0,1,2,3], index =["a","b","c","d"])
print(s)

#tao series tu dict
data = {'a': -1.3 , 'b':1.5 , 'd':2.0 , 'f':10, 'g':5}
ser = pd.Series(data,index=['a','b','c','d','f','g'])
print(ser)

#truy cap du lieu tu Sreies voi index va vi tri
data = {'a': -1.3 , 'b':1.5 , 'd':2.0 , 'f':10, 'g':5}
ser = pd.Series(data,index=['a','b','c','d','f','g'])
print(ser['c'])
print(ser['d'])

# lay du lieu tu dau den index cu the
data = {'a': -1.3 , 'b':1.5 , 'd':2.0 , 'f':10, 'g':5}
ser = pd.Series(data,index=['a','b','c','d','f','g'])
print(ser[:'d'])

#lay 3 du lieu cuoi
data = {'a': -1.3 , 'b':1.5 , 'd':2.0 , 'f':10, 'g':5}
ser = pd.Series(data,index=['a','b','c','d','f','g'])
print(ser[-3:])

#DataFrame([data, index, columns, dtype, copy])
#tao DataFrame tu dict cac Series1:
#phan1 : tao dict tu cac series1
s = {'mot': pd.Series([1.,2.,3.,5.], index=['a','b','c','e']),
    'hai': pd.Series([1.,2.,3.,4.] , index=['a','b','c','d'])
}
  #tao Dataframe tu dict series1
df = pd.DataFrame(s)
print(df)

#tao DataFrame tu dict cac series 2
s = {'mot':pd.Series([1.,2.,3.,4.], index=['a', 'b','c', 'e']),
     'hai': pd.Series([1.,2.,4.,6.] , index=['a' ,'b' , 'c', 'd'])}
#tao DataFrame tu cac dict da duoc chon
df = pd.DataFrame(s, index=['a','c','d'])
print(df)

# cac thao tac chon them xoa cot
#vd 1 chon cot
s = {'mot': pd.Series([1,2,4,5] , index=['a', 'b','c', 'd']),
    'hai': pd.Series([1,4,6,7] , index=['a', 'c', 'e', 'f']),
    'ba': pd.Series([5,8,9,0] , index=['c', 'd', 'g', 'f'])}
df = pd.DataFrame(s)
#chon cot 1
df_mot  = df['mot']
print(df_mot)

#mot so cach them cot
s = {'mot': pd.Series([1,2,4,5] , index=['a', 'b','c', 'd']),
    'hai': pd.Series([1,4,6,7] , index=['a', 'c', 'e', 'f']),
    'ba': pd.Series([5,8,9,0] , index=['c', 'd', 'g', 'f'])}
df = pd.DataFrame(s)
#them cot bon voi gia tri moi o theo cong thuc
df['bon']= df['hai'] - df['mot']

# them cot voi gia tri vo huobg
df['chuan'] = 'Ok baby'

# them cot khong cung so luong index voi DataFrame
df['khac'] = df['ba'][:9]

# THEM COT TRUE FALSE THEO DIEU KIEN
df['kiem tra'] = df['mot'] == 5.0

#dùng hàm insert. Cột "chèn" bên dưới sẽ ở vị trí 2 (tính từ 0), có giá trị bằng cột một
df.insert(2, 'chen' , df['mot'])

# xoa cot
del df['hai']

