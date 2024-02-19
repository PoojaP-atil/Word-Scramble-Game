list1 = [['a', 'b', 'e', 't', 'o', 'u'], ['d', 't', 'i', 'r', 's', 'o'], ['a', 'm', 'e', 't', 'n', 'u']]
list2 = [['bat', 'but', 'eat', 'ate', 'out', 'toe', 'bet', 'bot'],
         ['dot', 'dit', 'sit', 'rot', 'sot', 'tos'],
         ['man', 'men', 'ten', 'tan', 'nut', 'mut', 'mat']]
point = 0

for i in range(len(list2)):
    print(list1[i])
    word = False

    for j in list2[i]:
        a = input("Enter a 3 letter word that can be formed using the above list: ")

        if a in j:
            print("Correct guess!!")
            point += 1
            print("Your Score is", point)
        else:
            print("Incorrect answer :(")
            break

print("Game Over! Your final score is:", point)
