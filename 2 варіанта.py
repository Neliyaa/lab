english_letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    text = input("Введіть текст: ").lower()
    runtype = input("Виберіть як запустити програму(*1*/2): ")

    chars = ""

    if runtype in "1 ":
        
        chardict = dict()

        main()

        print(f"\nКількість символів: {len(text)}\n")

        for char in chars.lower():
            chardict[char] = 0

        for char in text:
            if char in chars:
                chardict[char] += 1

        for key, value in chardict.items():
            print(f"Кількість букв '{key}': {value}")

    elif runtype == "2":
        words = text.split(" ")

        dictlist = [word.lower() for word in words if len(word) > 3]
        dictlist = sorted(set(dictlist))

        for word in dictlist:
            print(word)

    else:
        print("Не правильний режим!")
        main()
