data = response.json()
print(data["name"]) # prints "Alice"
print(data["friends"][0]["name"]) # prints "Bob"
