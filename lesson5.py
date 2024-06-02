a = input("enter the first input:  ")
operator = input("enter the operator(+,-,*,/,%): ")
b= input("enter the second input:  ")
a = int(a)
b = int(b)
if operator == '+':
   print(a+b)
elif operator =='-':
       print(a-b)
elif operator =='*':
       print(a*b)
elif operator =='/':
       print(a/b)
elif operator =='%':
       print(a%b)
else :
      print("invalid operator")                 