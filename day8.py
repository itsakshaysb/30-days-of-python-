Dog = {
	"name": "Buddy",
	"color": "Brown",
	"breed": "Labrador",
	"legs": 4,
	"age": 5,
}

student = {
	"first_name": "John",
	"last_name": "Doe",
	"gender": "Male",
	"age": 20,
	"marital_status": "Single",
	"skills": ["Python", "Data Analysis", "Machine Learning"],
	"country": "USA",
	"city": "New York",
	"address": "123 Main Street",
}

print(len(student))
print(student["skills"])
student["skills"].append('html')
print(student["skills"])
print(student.keys())
print(student.values())
print(student.items())
student.popitem()
print(student)
del student
print(student)
