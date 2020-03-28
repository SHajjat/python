from Question import Question

quetion_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are Vapes?\n(a) Red/Green\n(b) Purple\n(c) Blue\n\n"
]

questions = [
    Question(quetion_prompts[0], "a"),
    Question(quetion_prompts[1], "c"),
    Question(quetion_prompts[2], "c")
]


def myexam():
    correct = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            correct += 1
    print({True:"You have passed",False:"You have failed"}[correct >=2])
    print("you Score is "+str(correct)+"/"+str(len(questions)))

myexam()