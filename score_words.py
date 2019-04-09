

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


def ini():
    n = int(input())
    words = input().split()
    print(score_words(words))

if __name__ == "__main__":
    tests = [
        ('hacker book', 4),
        ('programming is awesome', 4),
        ('o papa eh pop', 5),
        ('tv, shh, psst, nth, dr', 10),
        ('hello beauty!', 4),
        ('evenly oddly', 3),
    ]
    for i in tests:
        assert score_words(i[0].split()) == i[1]
