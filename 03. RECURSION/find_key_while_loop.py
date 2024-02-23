def search_for_key(initial_box):
    stack = [initial_box]

    while stack:
        current_box = stack.pop()

        # Check the contents of the current box
        for item in current_box:
            if item == "key":
                print("Found the key! You're done.")
                return
            elif isinstance(item, list):
                # If it's another box, add it to the stack for later examination
                stack.append(item)

    # If the loop completes and the stack is empty, the key was not found
    print("Key not found in any of the boxes.")

# Example usage
grandma_attic = [
    "old clothes",
    ["empty box", "another box", ["key", "photos"]],
    "dusty books",
    ["more boxes", ["socks", "shoes"], "hat"]
]

# Starting the search with the initial box
search_for_key(grandma_attic)
