print('''
1.add
2.sub
3.multiply
4.divide
''')

 
num1=int(input("enter your value num1"))
num2=int(input("enter your value num2"))
print("""Select the optiion 1.add
2.sub
3.multiply
4.divide
""")
opr=input("enter the opr...")
if opr== "1":
    
    print(num1+num2)
elif opr== "2":
      print(num1-num2)
elif opr== "3":
      print(num1*num2)
elif opr== "4":
      print(num1/num2)
else:
    ("invalid opr")
               
