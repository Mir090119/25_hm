# 1. Запись текста
sentence = input()
with open("text1.txt", "w") as f:
    f.write(sentence)

# 2. Чтение всего файла
with open("text1.txt", "r") as f:
    print("\nСодержимое text1.txt:")
    print(f.read())

# 3. Чтение построчно
i = 1
with open("text2.txt", "r") as f:
    for line in f:
        print(f"{i}: {line.strip()}")
        i += 1

# 4. Подсчёт символов
with open("text3.txt", "r") as f:
    content = f.read()
    print(f"\nКоличество символов в text3.txt: {len(content)}")

# 5. Подсчёт слов
with open("text4.txt", "r") as f:
    words = f.read().split()
    print(f"\nКоличество слов в text4.txt: {len(words)}")

# 6. Поиск строки
search_word = input("\nВведите слово для поиска в text5.txt: ")
with open("text5.txt", "r") as f:
    print("\nСтроки, содержащие слово:")
    for line in f:
        if search_word in line:
            print(line.strip())

# 7. Добавление в файл
line_to_add = input("\nВведите строку для добавления в text6.txt: ")
with open("text6.txt", "a") as f:
    f.write(line_to_add + "\n")

# 8. Копирование
with open("text7.txt", "r") as src, open("text7_copy.txt", "w") as dst:
    dst.write(src.read())

