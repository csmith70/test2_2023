## Christopher Smith
## September 5,2019
## Grader Assignment, Homework #2


#Enter the total number of grades
TotalGrades = input('Enter the total number of grades:')
#Make sure the variable is a floating point value
TotalGrades = float(TotalGrades)
#Enter the number of points for each letter grade 
PPG = input('Enter the number of points for each letter grade:')
#Make sure the variable is a floating point value 
PPG = float(PPG)
#Start with index 1 for assignment
n = 1
#Set sum = 0 before adding grades from user input
sum = 0.0
#Allow user to input grades for each assignment until # assignment = total grades user input
while n <= TotalGrades:
	print("Assignment", n)
	grade = float(input("Enter a grade: "))
	sum = sum + grade #adds the grades to each other
	n += 1	#Assignments in ascending order
#Calculate the average for the final grade
x = sum/TotalGrades
Text = 'The final grade is {0:7.1f}'.format(x)
print(Text)
#Designate a letter grade based on the # of point for each grade user specified
if x >= (100-PPG):
	print("The final grade is an A")
elif (100 - 2*PPG) <= x < (100 - PPG):
	print("The final grade is a B")
elif (100 -3*PPG) <= x < (100 - 2*PPG):
	print("The final grade is a C")
elif (100 - 4*PPG) <= x <  (100 - 3*PPG):
	print("Then final grade is a D")
else: 
	print("The final grade is a F")








