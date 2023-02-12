name1=input("enter first name\n").lower()
name2=input("enter second name\n").lower()
total=name1.count("t")+name2.count("t")+name1.count("r")+name2.count("r")+name1.count("u")+name2.count("u")+name1.count("e")+name2.count("e")
total2=name1.count("l")+name2.count("l")+name1.count("o")+name2.count("o")+name1.count("v")+name2.count("v")+name1.count("e")+name2.count("e")
score=int(str(total)+str(total2))

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")