import random
secret_code=8326
Input1=int(input("Enter Number of Tries: "))
Bulls=0
cows=0
a=0
while a<Input1:
 Input2=int(input("Enter your guess: "))
 if Input2==secret_code:
  print(f"Congrats! the number is: {Input2}")
  break
 else:
  for i in range(len(str(secret_code))):
   if str(Input2)[i]==str(secret_code)[i]:
    Bulls+=1
   elif str(Input2)[i]!=str(secret_code)[i] and str(Input2)[i] in str(secret_code):
    cows+=1
 print(f"{Bulls} bulls, {cows} cows")
 Bulls=0
 cows=0
 a+=1
 if a==Input1:
  if Input2!=secret_code:
   print(f"You ran out of tries.Number was {secret_code}")