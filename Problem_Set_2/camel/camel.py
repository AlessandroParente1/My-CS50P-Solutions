camel=input("camelCase: ")
position=[]

for i,c in enumerate(camel):
    if c.isupper():
        position.append(i)

result=[]
last_index=0

for i in position:
   result.append(camel[last_index:i])
   result.append("_"+camel[i].lower())
   last_index=i+1

result.append(camel[last_index:])
camel="".join(result)

print(camel)
