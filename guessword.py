import random
words = [
    "ant", "ape", "bat", "bear", "cat", "car", "dog", "deer", "egg", "eagle",
    "fig", "frog", "go", "game", "he", "home", "it", "idea", "jet", "juice",
    "kit", "kite", "lap", "lion", "mat", "mouse", "nap", "nest", "ox", "oven",
    "pet", "plane", "quiz", "queen", "rat", "radio", "sit", "sheep", "tap",
    "table", "up", "uncle", "van", "violin", "we", "water", "xi", "x-ray",
    "yak", "yellow", "zoo", "zebra"
]
a=random.choice(words)
print(a)
print("you have only 5 attempts: ")
i=0
print("Press 1 for guessing first letter of word")
print("Press 2 for guess same word like first word")
choice=int(input("Enter Choice: "))

while i<=5:
    if choice==1:
        print("Enter",i,"Attempt")
        Fir_char=(input("Enter First char of Word: "))
        if Fir_char.lower()==a[0]:
            print("You won")
            break
        else:
            print("you lose")
    elif choice==2:
        sec_word=input("enter Second word like begin with First Word First char: ")
        if sec_word.lower() in words:
            print(a,",",sec_word,"both words are starting with same letter '**YOU WON**' ")
            break
        else:
            print("Wrong one")
        
    i+=1

