students_height=input("Enter students height: ").split()
s=0
c=0
for i in students_height:
    s+=float(i)
    c+=1
AVG=s/c

print(AVG)