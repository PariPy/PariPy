print("calculator")
op= input("enter operator(+,-,*,/):")
a=float(input("a="))
B=float(input("B="))
C=float(input("C="))
if op=='+':
    print('Result=',a+B+C)
elif op=='-':
    print('Result=',a-B-C)
elif op=='*':
    print('Result=',a*B*C)
elif op=='/' :
    print('Result=',a/B/C)   
else:
    print("invalid operator")
        
