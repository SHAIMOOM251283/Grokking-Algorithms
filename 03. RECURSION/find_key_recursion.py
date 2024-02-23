def search_for_key(box):
    for item in box:
        if isinstance(item, list):
            # If the item is a box, recursively search through it
            result = search_for_key(item)
            if result == "Key found!":
                return result
        elif item == "key":
            # If the item is a key, return "Key found!"
            return "Key found!"
    # If no key is found in the current box, return "Key not found."
    return "Key not found."

# Example usage
grandma_attic = [
    "old clothes",
    ["empty box", "another box", ["key", "photos"]],
    "dusty books",
    ["more boxes", ["socks", "shoes"], "hat"]
]

result = search_for_key(grandma_attic)
print(result)
