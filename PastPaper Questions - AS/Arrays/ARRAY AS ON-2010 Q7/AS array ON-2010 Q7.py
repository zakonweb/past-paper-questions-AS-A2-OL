total = 0
YearTemp = []
YearTemp.append(0)

for i in range(11):
    yt = int(input())
    YearTemp.append(yt)
    total = total + yt

M = total / 11
total = 0
yt = 0

while not 1<=yt<=11:
    yt = int(input())

for i in range(yt, (yt+4)):
    total = total + YearTemp[i]

Avg = total / 4

Dif = Avg - M

if Dif > 4:
    print("HOT")
else:
    print("COLD")