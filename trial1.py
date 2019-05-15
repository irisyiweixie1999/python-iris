file=open("mcdata2.csv")
data=file.read()
print(data)

rows=data.split("\n")
print(rows)
print("i'm priting rows[0]",rows[0])

datarows=rows[1:3]
introws=[]
for row in datarows:
    print(row)
    introw=row.split(",")
    print("introw[0]",introw[0])
    arow=[]
    for introwe in introw:
        print(int(introwe))
        arow.append(int(introwe))
    print(arow)
    introws.append(arow)
print(introws)

print(introws[1][1])

print(sum(introws[0]))

xsum=0
for introw in introws:
    for col in introw:
        if col%2==0:
            xsum+=col
print(xsum)
