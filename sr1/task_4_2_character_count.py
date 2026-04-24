text = input("Введіть рядок: ")

character_count = {}

for character in text:
    character_count[character] = character_count.get(character, 0) + 1

print(character_count)
