pyramid_height = int(input("Введіть висоту піраміди: "))

for row in range(1, pyramid_height + 1):
    spaces = " " * (pyramid_height - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)
