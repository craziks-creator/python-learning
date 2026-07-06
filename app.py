m='\thello?'
x= "\n\tjokuja"
print (m+" "+x.upper())
print (m+" "+x.upper().strip())
v=121/3
print("\t my fav number is:" + " " + str(v))
#learnt one hour
x=['joker','hero']
x[0]='chor'
x.append('police')
x.insert(0,'neta')
print(x)
del x[0]
print (x)
y=x.pop()
print ("last item removed:" + "\t" + str(y))
print("remaining items: " + str(x))
q=[]
for z in x:
    q.append(z)
print (x)
q=[z for z in x ]
print(q[0])
c=[v**3 for v in range(2,11,2)]
print(c)
#learnt one hour full
p=range(1,10,2)
q=[p for p in p]
print(q)

for n in p:
    print(n)

#conditional

if 1 in p:
        print("\n here is 1 found in p:  " + str(p))
elif 3 in p:
        print('\n 3 is in p')
else:
        print('3 is not in p')

#dictionary
d={'name':['Alice','yuvi'],'age':25,'city':'New York'}
for key,value in sorted(d.items()):
    print(str(key)+":"+ str(value))
for name in d['name']:
    if 'Alice' in name:
          print("hi! " + name + " your age is: " + str(d['age']) + " and you live in: " + str(d['city']))

print(d['name'])
print(d['age'])
print(d.keys())
print(d.values())
print(d.items())
print(d)
print(d.pop('age'))
print(d)
print(d.get('name'))
print(d.get('age'))
print(d)
d['age']=30
print(d)    
