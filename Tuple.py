T1=()
#tuple(iterable)
T2=tuple()
T3=('String',1,2,[1,2])
#T4='String',1,2[1,2]
T5=('String'),

T6=(1)
T7=([1,2])
T8=('String')
T9='String',
T10=(1,)
T11=1,
T12=([1,2],)
T13=[1,2],
#t14=tuple(1)
L=[T1,T2,T3,T5,T6,T7,T8,T9,T10,T11,T12,T13]
for i in range (len(L)):
    print('T'+str(i)+':{},Type:{}'.format(L[i],type(L[i])))

'''#operators:
#+,*,[],[:],[::],in,not in
T1=(1,2,3,4)
T2=('String',1,2,[1,2])
print('T1 id:',id(T1))
print('T2 id:',id(T2))
T3=T1+T2
print('T3:',T3)
#print('S'+T3)
print('T1 id:',id(T1))
print('T2 id:',id(T2))
print('T3 id:',id(T3))
T4=T1*3
print('T4:',T4)
print('T1 id:',id(T1))
print('T4 id:',id(T4))
for i in T2:
    print(i)'''
'''#Tuple Slicing:
T=(1,2,3,4,'a','b',['c','d'],'e')
print('Tuple id:',id(T))
print('1',T[0],'id:',id(T[0]))
print('2',T[-1],'id:',id(T[-1]))
print('3',T[:],'id:',id(T[:]))
print('4',T[1:],'id:',id(T[1:]))
print('5',T[1:6],'id:',id(T[1:6]))
print('6',T[1:6:2],'id:',id(T[1:6:2]))
print('7',T[:6],'id:',id(T[:6]))
print('8',T[8:],'id:',id(T[8:]))
print('9',T[-7:],'id:',id(T[-7:]))
print('10',T[-7:-2],'id:',id(T[-7:-2]))
print('11',T[:-2],'id:',id(T[:-2]))
print('12',T[-7:-8],'id:',id(T[-7:-8]))
print('13',T[-7:6],'id:',id(T[-7:6]))
print('14',T[::-1],'id:',id(T[::-1]))
print('15',T[-1:-len(T):-1],'id:',id(T[-1:-len(T):-1]))
print('16',T[-7::-1],'id:',id(T[-7::-1]))
print('17',T[-7:2:-1],'id:',id(T[-7:2:-1]))
print('18',T[-7:-2:1],'id:',id(T[-7:-2:1]))
print('19',T[:-2:-1],'id:',id(T[:-2:-1]))
print('Tuple id:',id(T))'''
'''#Tuples are immutable:
T=('String',1,2,['a','b'])
print(id(T))
#modifying changing elements
#T[0]='a'
#T[0][0]='a'
#T[1]='c'
#T[2]='c'
#T[3]='s'
T[3][0]='s'
print(T)
#adding new elements
#T[4:]=(1,2)
#del T[0]
#del T[3]
del T[3][0]
print(T)
print(id(T))'''
'''#Built in methods
#len(),max(),min(),del
T1=1,2,3,4
T2='a','b','c'
T3=1,2,3,4,'a','b','c'
print('T1 len:',len(T1))
print('T2 len:',len(T2))
print('T3 len:',len(T3))
print('T1 max:',max(T1))
print('T2 max:',max(T2))
#print(max(T3))
print('T1 min:',min(T1))
print('T2 min:',min(T2))
#print(min(Tuple3))
#del(Tuple1[2])
#del(Tuple[1:4])
del(T1)
del(T2)'''
'''#count:
#Tuple methods
Tuple=('String',(1,2),[1,2],(1,2),1,2,1)
element=1
element=(1,2)
print(Tuple.count(element))
print(Tuple.count())'''
'''#index:
Tuple=('String',(1,2),[1,2],(1,2),1,2,1)
element=1
element=(1,2)
print(Tuple.index(element))
print(Tuple.index(element,2,len(Tuple)))'''
