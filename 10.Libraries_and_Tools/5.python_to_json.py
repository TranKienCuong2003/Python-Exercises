import json

def python_to_json(data):
    return json.dumps(data)

data = {"name": "Alice", "age": 25, "city": "Hanoi"}
json_data = python_to_json(data)
print("Chuoi JSON:", json_data)
