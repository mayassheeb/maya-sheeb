def student_type(age):
	if(age==14):
		return"Y1"
	elif(age==15):
		return"Y2"
	elif(age==16):
		return"Y3"
	elif(age>16):
		return"teacher"
	else:
		return"too young for code Palestine"
print(student_type(16))
