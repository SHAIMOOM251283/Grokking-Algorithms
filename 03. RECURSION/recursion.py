def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # Recursion!
        elif item.is_a_key():
            print("Found the key!")
