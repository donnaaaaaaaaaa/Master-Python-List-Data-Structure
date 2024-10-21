

# List of employee dictionaries
employees = [
    {"name": "John Doe","department": "Sales"},
    {"name": "Jane Smith","department": "Human Resources"},
    {"name": "Mark Johnson","department": "IT"},
    {"name": "Lisa Wong", "department": "Marketing"},
    {"name": "Paul McDonald","department": "Finance"}
]

print("\nEmployees:")
for employee in employees:
    print(f"Name: {employee['name']}, Department: {employee['department']}")