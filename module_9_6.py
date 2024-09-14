# Генераторы

def all_variants(text):
    res = len(text)
    for i in range(1, res + 1):
        for start in range(res - i + 1):
            yield text[start: start + i]

a = all_variants("abc")
for i in a:
    print(i)

