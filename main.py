import random
print ("welcome to r p s")
i=(input("1 for rock, 2 for peaper, 3 for seasor  "))
lis=[1,2,3]
lista=["rock","peaper","seasor"]
k=(random.randint(1,3))
ok=lista[k]
print(f"comp chose {ok}")
print(f"{i}+{k}")
if(i==k):
  print("its a draws")
elif(i==1 and k==3):
  print("comp won")
elif(i==1 and k==2):
  print("you win")
elif(i==2 and k==3):
  print("u win")
elif(i==2 and k==1):
 print("comp wins")
elif(i==3 and k==1):
  print("u win")
elif(i==3 and k==2):
 print("comp wins")
else:
  print("u loose")
1
