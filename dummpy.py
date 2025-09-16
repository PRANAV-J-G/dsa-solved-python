
def canBeTypedWords(text: str, brokenLetters: str) -> int:
    count = 0
    for word in text.split():
        for c in word:
            if c in brokenLetters:
                break
        else:
            count += 1
    return count
str = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(str,brokenLetters))

