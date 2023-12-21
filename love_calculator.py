name1 = input("Enter your name: ")
name2 = input("Enter name of your lover: ")
combine_string = name1 + name2

lower1 = combine_string.lower()

t = lower1.count('t')
r = lower1.count('r')
u = lower1.count('u')
e = lower1.count('e')

true = t + r + u + e

l = lower1.count('l')
o = lower1.count('o')
v = lower1.count('v')
e = lower1.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))
#int(love_score)
if love_score < 10 or love_score > 90:
    print(f"your love score is {love_score} and you can go like coke and matone so strong love wishes")
elif love_score >= 40 or love_score <= 50:
    print(f"your love score is {love_score} and you are alright together")
else:
    print(f"your love score is {love_scor} and so strong love wishes")
