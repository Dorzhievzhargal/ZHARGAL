students = ['john', 'mark', 'aziz', 'feruza', 105]
print(students)
# todo:accessing the element in the list
# list hold values by index, index with 0
# varname assign[0, 1,   2, 3 ]
print(students[0])  # printed first student from student list
print(students[2:])

# Data structures: list tuple, dictinary
print(f"Hello {students[1].title()} ! Thank you for coming")
print(f"Hello {students[4]} ! Thank you for coming")
print("Hello " + str(students[4]) + "! Thank you for coming")

# TIY 3-3 creat cars list, print different
cars = ['bmw', 'nissan', 'mazda', 'honda']
print(f"I would traval on {cars[1]}")
print(f"I would traval on {cars[1]} or {cars[2]}")

cars = ['bmw', 'nissan', 'mazda', 'honda']
print(f"I would like to own a " + str(cars[2]))

cars = ['bmw', 'nissan', 'mazda', 'honda']
print(students)
print(f" This is cars b4 changes {cars}")
cars[2] = "tesla"
print(f" This is cars after changes " + str(cars))

# Adding element
# appending
cars.append('lexus')
print(cars[2].title())

# insert
cars.insert(2, 'toyota')
print(f"after add toyota {cars}")
cars.remove('lexus')
print(f"after remove lexus {cars}")
del cars[2]
print(cars)
cars.pop()
print(cars)
