def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    
    while pile:  # Corrected syntax for checking if the pile is not empty
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!")  # Corrected syntax for print statement
