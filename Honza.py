"""
a = [2,-1,3,5,20,0]
interval = []
min_value = a[0]
i = 0
while True:
    if i == len(a)-1:
        break
    elif a[i] > 2 and a[i] < 11:
        interval.append(a[i])
        if a[i] < min_value:
            min_value = a[i]
        i += 1
    else:
        if a[i] < min_value:
            min_value = a[i]
        i += 1
print(len(interval))
print(min_value)
"""
N = "N50 43' 26.339''"
E = "E15 10' 36.986''"
Ndeg = int(N[1:3]) + int(N[4:6])/60 + float(N[8:14])/3600
Edeg = int(E[1:3]) + int(E[4:6])/60 + float(E[8:14])/3600
print(Ndeg)
print(Edeg)


