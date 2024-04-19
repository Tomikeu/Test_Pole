#Serad cisla od nejmensiho k nejvetsimu

a = [3,2,1,5,4]

i=0
while i<len(a):
    key=i
    j=i+1
    while j<len(a):
        if a[key]>a[j]:
            key=j
        j+=1
    a[i],a[key]=a[key],a[i]
    i+=1
print(a)