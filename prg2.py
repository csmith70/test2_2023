## Christopher Smith
## Aug 30, 2019
## 2nd Program User Input
import numpy as np
n = 1
end = input('Enter a number between 3 and 10: ')
end = float(end)

while n<end:
	print('Hello World: {0}'.format(n))
	if n%2 == 0:
		print("Even")
	else:
		print("Odd")
	n = n+1

x = 654.98
Text = 'The value of x is {0:3.3f}'.format(x)
print(Text)
