import tkinter as tk  
from functools import partial
import math
       
       
def call_result(label_result, n1, n2,n3):
	num1 = (n1.get())
	num2 = (n2.get())
	num3 = (n3.get())
	e=2.718281828459045
	fun1=num1.replace('sqrt','math.sqrt')

	fun2=fun1.replace('sin','math.sin')

	fun3=fun2.replace('cos','math.cos')

	fun4=fun3.replace('tan','math.tan')

	fun5=fun4.replace('cot','math.cot')

	fun6=fun5.replace('sec','math.sec')

	fun7=fun6.replace('cosec','math.cosec')

	fun8=fun7.replace('log','math.log')
        
	
	delx=(float(num2)-float(num3))/100000
	n=0
	x=float(num3)
	n=n+eval(fun8)
	n=0.5*n
	for i in range(1,100000):
		x=x+delx
		n=n+eval(fun8)
	x=float(num2)
	g=eval(fun8)
	g=0.5*g
	t=n+g
	res=delx*t
	print(res)
	result = res  
	label_result.config(text="Result = %f" % result)  
	return  
       
root = tk.Tk()  
root.geometry('500x300+200+300')  
      
root.title('Calculator')  
       
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()
      
labelNum1 = tk.Label(root, text="Expression").grid(row=1, column=0)  
      
labelNum2 = tk.Label(root, text="Upper limit").grid(row=2, column=0)

labelNum3 = tk.Label(root, text="Lower limit").grid(row=3, column=0)
      
labelResult = tk.Label(root)  
      
labelResult.grid(row=9, column=2)  
      
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
      
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

entryNum2 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
      
call_result = partial(call_result, labelResult, number1, number2, number3)  
      
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=4, column=2)  
      
root.mainloop()  
