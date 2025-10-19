import json

# Python dictionary → JSON
data = {"name": "Tareq", "age": 25, "language": "Python"}

json_data = json.dumps(data)
print(json_data)  

# JSON → Python dictionary
parsed = json.loads(json_data)
print(parsed["age"])  # Tareq