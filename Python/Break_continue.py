i=1
while(i<=20):
    if i==5:
        break
    print(i)
    i+=1 #updation
print("OUTSIDING THE LOOP..")


i=1
while(i<=10):
    if i%6==0:
        break
    print(i)
    i+=1
print("outsiding the loop..")





i=1
while(i<=50):
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1
print("outsiding the loop..")



i=1
while(i<=10):
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1