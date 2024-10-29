# Dictionary
# list [], tuple (), dictionary {}
student = {"name": "Gloria Atieno", "id": 1234, "age": 23, "gender": "F"}

print(student["name"]) # key
print(student)

student["weight"] = 63
print(student)

# set -- only one existence per item, unordered, mutable
people = {"Gloria", "Don", "Rose", "Mike", "Job", "Gloria"}
print(people)
people.add("Gilo")
print(people)
people.remove("Gloria")
print(people)
people.discard("Gloria")
