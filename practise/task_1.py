
''' task 1'''
s = input() # apple banana cherry
result = s.split()
print(result) # ['apple', 'banana', 'cherry']
result = ", ".join(result)
print(result) # apple, banana, cherry
result = f"I have {result}."
print(result)


''' task 5 '''
quiz = {"Which is the currency of KZ?" : {"Tenge", "KZT"},
        "Name one of the past/present presidents of Kazakhstan:" : {"Tokayev"},
        " What year Kazakhstan proclaim independence? 1" : {"1991" }}
count = 0
for question, answer in quiz.items:
    my_answer = input(question)
    if my_answer in answer:
        count += 1
percentage = count/len(quiz)*100
user_won = True if percentage > 70 else False
if user_won  == True:
    print(f"Congrats, you won with {percentage:.2f} correctness")
else:
    print(f"You lost! You got only {percentage:.2} correctness")