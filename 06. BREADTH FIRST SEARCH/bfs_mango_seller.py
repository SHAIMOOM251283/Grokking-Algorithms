def find_mango_seller(friends, sells_mangoes):
  """
  This function uses breadth-first search to find a mango seller in the owner's network.

  Args:
    friends: A dictionary where keys are people and values are lists of their friends.
    sells_mangoes: A dictionary where keys are people and values are booleans indicating if they sell mangoes.

  Returns:
    The name of the first person in the network who sells mangoes, or None if no one does.
  """
  queue = ["owner"]  # Start with the owner's name
  visited = set()  # Keep track of visited people

  while queue:
    person = queue.pop(0)  # Get the first person in the queue
    visited.add(person)

    if sells_mangoes[person]:  # Check if this person sells mangoes
      return person

    # Add friends who haven't been visited yet to the queue
    for friend in friends[person]:
      if friend not in visited:
        queue.append(friend)

  return None  # No mango seller found

# Example usage
friends = {
  "owner": ["Alice", "Bob", "Charlie"],
  "Alice": ["David", "Emily"],
  "Bob": ["David", "Fiona"],
  "Charlie": ["Emily", "Fiona", "George"],
  "David": [],  # No friends listed
  "Emily": [],
  "Fiona": [],
  "George": ["David"],
}

sells_mangoes = {
  "owner": False,
  "Alice": False,
  "Bob": False,
  "Charlie": False,
  "David": True,
  "Emily": False,
  "Fiona": True,
  "George": False,
}

mango_seller = find_mango_seller(friends, sells_mangoes)

if mango_seller:
  print(f"Found a mango seller: {mango_seller}")
else:
  print("No mango seller found in the network.")
