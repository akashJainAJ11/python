import random

# value = random.random()
value = random.randint(1, 100)
print(value)


colors = ['Red', 'Black', 'Blue', 'Green']

result = random.choices(colors, k=10)
print(result)


deck = list(range(1, 53))

random.shuffle(deck)
print(deck)

hand = random.sample(deck, k=5)
print(hand)
