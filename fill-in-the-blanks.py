quiz_1="__1__ is the capital of Iowa. The __2__ is it's state bird,\n the __3__ , it's state rock.\n Iowa's slogan: Iowa __4__"
quiz_2="In the year __1__ , Prohibition was enacted in the US.\n __2__ was the President during this time.\n Prohibition outlawed __3__ . This led to an influx of secret bars, otherwise known as __4__ ."
quiz_3="Yellow is to lemon as __1__ is to apple.\nCheetah is to fast as tortoise is to __2__ .\nBook is to __3__ as music is to listen.\nSnow is to cold as sun is to __4__ .\n"


fill_in=["__1__","__2__", "__3__","__4__"]


answer_1=["Des Moines", "goldfinch", "geode","Nice"]
answer_2=["1919", "Woodrow Wilson", "alcohol","speakeasies"]
answer_3=["red", "slow", "read", "hot"]


def quiz_level():
    # user will pick what quiz they want to take and this returns the appropriate quiz and answers
    # with input from user, the selected quiz from above as well as it's answers will be returned
  user_choice=raw_input("Pick your choice of quiz by typing 1, 2, or 3 and hitting ENTER\n")
  if user_choice=="1":
    print"Great! This quiz is about Iowa state history. Capitalization counts! Fill in the answer as prompted!\n"
    return quiz_1, answer_1, fill_in
  elif user_choice=="2":
    print"This quiz goes over a little history during the early 1900's in America.\nFill in the blank as prompted!\n"
    return quiz_2, answer_2, fill_in
  else:
    print"This quiz is comparing one thing to another. Use those as clues to see what is the comparison between.\n Fill in the blank as prompted!"
    return quiz_3, answer_3, fill_in


def show_quiz(paragraph, answers, fill_in):
    # this will sort through the respective paragraph and identify the blanks that need to be filled with answers
    # this uses the paragraph and answers returned from above function and then finds where in the paragraph the blanks (Which are in the Fill_in list)
  print paragraph
  paragraph=paragraph.split()
  for blanks in paragraph:
    if blanks in fill_in:
      return blanks
  return None


def fill_in_blank(answers, commence, key):
    # This function asks for user input to answer the blank identified above.
    # The user's answer will be compared to the answers for the quiz. If they match, the user answer is returned
    # Else, the user has two more guesses and if they still can't come up with correct answer, they get a "__X__"
  user_answer=raw_input("\nWhat's your answer for" + commence + "?\n")
  if user_answer==answers[key]:
    return user_answer
  else:
    max_guesses=2
    while max_guesses>0:
      user_reattempt=raw_input("Try again..you have "+str(max_guesses)+ " more guess(es).\n")
      if user_reattempt==answers[key]:
        return user_reattempt
      else:
        max_guesses-=1
  return "__X__"


def correct_answer(request_input, fill_in, answers, paragraph, find_replace):
    # This function first sees if the answer was correct or user ran out of guesses. It then fills in the blank with the right answer or an "X" to show that it was incorrectly answered after 3 attempts
  if request_input !="__X__":
    print "\nYou got it!\n"
    paragraph=paragraph.split()
    for word in paragraph:
      if word in fill_in:
        return paragraph.index(fill_in[find_replace]) #this returns the spot in the paragraph the blank is located
  else:
    if request_input=="__X__":
      print "You're out of chances! Let's move on\n"
      paragraph=paragraph.split()
      for word in paragraph:
        if word in fill_in:
          return paragraph.index(fill_in[find_replace])


def answer_for_blank(paragraph, replaced, request_input):
    # this takes the information returned above and replaces the blank with the correct answer or "__X__"
  paragraph=paragraph.split()
  paragraph.pop(replaced)
  paragraph.insert(replaced, request_input)
  paragraph=" ".join(paragraph)
  return paragraph


def take_quiz():
    # The user begins the quiz here, with the first function being called to request them to choose which one to take
  print "Welcome!"
  paragraph, answers, fill_in=quiz_level()
  key=0
  find_replace=0
  for num_blanks in fill_in:    # this loop iterates over the number of blanks to be filled in and prompts the user to answer them and fills in the blank as they go
    commence=show_quiz(paragraph, answers, fill_in) # each return of a function is given a name (e.g. commence) so that information can be easily used in the next function
    request_input=fill_in_blank(answers, commence, key)
    replaced=correct_answer(request_input, fill_in, answers, paragraph, find_replace)
    fill_blanks=answer_for_blank(paragraph, replaced, request_input)
    paragraph=fill_blanks
    key +=1
    find_replace +=1
  return paragraph


print take_quiz() + "\n"    # the ending paragraph is returned filled in with correct answers and/or "__X__"


play_again=raw_input("If you would like to play again, type Yes .\n")    #player asked if they'd like to play again
if play_again=="Yes":
  take_quiz()   # calls the take_quiz function and the beginning of the quiz populates
else:
  print"Thanks for playing!"
