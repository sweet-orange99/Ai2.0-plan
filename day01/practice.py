name = 'John'
age = 30
city = 'New York'

print(f"My name is {name}, I am {age} years old, and I live in {city}.")


foods = ['Pizza', 'Burger', 'Pasta', 'Salad']
print("My favorite foods are:")
for food in foods:
    print(f"- {food}")

students = {
    "name": "Alice",
    "score": 95
}
print(f"{students['name']} scored {students['score']} on the test.")
print(f"{students.get('name')} scored {students.get('score')} on the test.")