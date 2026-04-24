word = input("Введіть слово: ")

if word:
    most_frequent_letter = max(word, key=word.count)
    count = word.count(most_frequent_letter)

    print("Найчастіше зустрічається буква:", most_frequent_letter)
    print("Кількість входжень:", count)
else:
    print("Слово порожнє")
