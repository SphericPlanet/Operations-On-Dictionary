students = {"name": "Gauransh Pandey", "roll": 1, "age": 14, "subjects": ["Maths", "Science"]}

print(students)

print("Student name:", students["name"])
print("Student roll:", students["roll"])
print("Student age:", students.get("age"))


students["age"] = 15 
print(students)


students["address"] = "House: 34, Noida"
print(students)

students.clear()
print("Clearing the dictionary:", students)
