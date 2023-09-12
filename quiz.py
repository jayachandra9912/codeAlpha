# A LIST OF QUESTIONS STORED IN VARIABLE
questions= ["what is my favourite color",
            "what is my favoute food",
            "what is my favourite place",
            "what is my favourite hobby",
            "what is most important to me"]
# A LIST OF OPTIONS IN A 2D TUPLE STORED IN A VARIABLE
options = [["A.BLUE","B.BLACK","C.RED","D.YELLOW"],
          ["A.ICECREAM","B.CHICKEN","C.BIRYANI","D.PANIPURI"],
           ["A.BEACH","B.DESERT","C.MOUNTAINS","D.TEMPLES"],
           ["A.WATCHING TV","B.LISTENING SONGS","C.DANCE","D.EATING"],
           ["A.INDEPENDENCE","B.MONEY","C.LOVE","D.CAREER"]]
# A LIST OF ANSWERS
answers = ["B","C","C","D","A"]
# A LIST OF GUESSES APPENDED TO THE GUESSES
guesses = []
score = 0
# THIS VARIABLE KEEPS THE TRACK OF WHAT QUESTION NUMBER YOU ARE
question_num = 0
# DISPLAYING QUESTIONS BY ITERATING A LIST OF QUESTIONS
for question in questions:
  print(question)
 # AFTER DISPLAYING OF EVERY QUESTION I NEED TO DISPLAY THE OPTIONS
  for option in options[question_num]:
# options is a 2d list so i kept index of question num for iteration
    print(option)
  guess= input("enter your choice").upper() # here the user gives input
  guesses.append(guess)
    # add the user input in guess to the list of guesses
  if guess == answers[question_num]:
      score +=1
      print("CORRECT!")
  else:
      print("INCORRECT!")
      print(f"{answers[question_num]}is the correct answer")
# if the answer is incorrect it will the correct answer of that question number
  question_num +=1  
#incrementing question_num
print("THE RESULTS ARE:")
print("answers: ",end="")
for answer in answers:
  print(answer,end="")
print()

print("guesses: ",end="")
for guess in guesses:
  print(guess,end="")
print()
score = int(score/len(questions)*100)
print(f"your score is: {score}%")