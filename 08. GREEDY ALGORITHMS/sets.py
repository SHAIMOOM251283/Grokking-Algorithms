fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])

# Set Union
union_result = fruits | vegetables
print("Union of fruits and vegetables:", union_result)

# Set Intersection
intersection_result = fruits & vegetables
print("Intersection of fruits and vegetables:", intersection_result)

# Set Difference (fruits - vegetables)
difference_result_fruits = fruits - vegetables
print("Difference (fruits - vegetables):", difference_result_fruits)

# Set Difference (vegetables - fruits)
difference_result_vegetables = vegetables - fruits
print("Difference (vegetables - fruits):", difference_result_vegetables)
