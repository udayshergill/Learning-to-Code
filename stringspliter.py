def stringspliter(sentence):
    holder = int(0)
    sentence = str(sentence)
    print(sentence)
    words = sentence.split(" ")
    word_amount = len(words)
    print("Your sentence has " + len + " amount of words")
    while holder != word_amount:
        print(words[holder])
        holder += 1
        
stringspliter(input("Input a sentence that I will break apart\n"))
