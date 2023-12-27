#python basic quiz game


Questions = ("Which of the following are valid ways to create a list in Python?: ",
            "How can you create a virtual environment in Python?: ",
            "What are the ways to define a function in Python?: ",
            "Select the correct ways to open a file in Python for writing?: ",
            "How do you remove an item from a list in Python?: ")
Answers = (("A.my_list=[1, 2, 3]","B.my_list = list(1, 2, 3)","C.my_list = list(range(5))","D. my_list = (1, 2, 3)"),
          ("A.virtualenv myenv","B.python -m venv myenv","C.pipenv install","D. conda create -n myenv"),
          ("A. def my_function():","B. function my_function():","C.define my_function():","D.lambda my_function():"),
          ("A.open('file.txt', 'r')","B.open('file.txt', 'w')","C.open('file.txt', 'a')","D.open('file.txt', 'x')"),
          ("A.list.remove(item)","B. list.pop(index)","C. del list[index]","D.list.discard(item)"))
Options = ("A,C","B,D","A,D","B,C,D","B,C")
Guesses = []
Score = 0  # Initialize Score variable
Question_num = 0

for Question in Questions:
    print("---------------------------------------")
    print(Question)
    for Answer in Answers[Question_num]:
        print(Answer)
    Guess = input("Enter(A,B,C,D):").upper()
    Guesses.append(Guess)
    if Guess == Options[Question_num]:
        Score += 1
        print(" Correct !")
    else:
        print(" Incorrect !")
        print(f"{Options[Question_num]} is the correct answer")
    Question_num += 1

print("---------------------------------------")
print("                Result                 ")
print("----------------------------------------")
print("Answers:", end="")
for Answer in Answers:  # Correct variable name
    print(Answer, end="")
print()
print("Guesses:", end="")
for Guess in Guesses:
    print(Guess, end="")
print()
Score = Score / len(Questions) * 100
print(f"Your Score is:{Score}%")

