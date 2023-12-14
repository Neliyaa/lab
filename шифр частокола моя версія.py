word = list("Привіт")
part1 = word[::2]
part2 = word[1::2]
print("".join(part1) + "".join(part2))