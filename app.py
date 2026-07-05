import this
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
#learnt one hour