from collections import deque

def person_is_seller(name, sells_mangoes):
    return sells_mangoes.get(name, False)

def search_for_mango_seller(owner, friends, sells_mangoes):
    search_queue = deque()
    search_queue += friends[owner]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person, sells_mangoes):
                print(person + " sells mangoes!")
                return True
            else:
                search_queue += friends.get(person, [])
                searched.append(person)
    return False

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

search_for_mango_seller("owner", friends, sells_mangoes)
