'''
Percentage Calculator for kids :-
'''

# The total number of subjects is taken in from below prompt.

try:
  how_many_subjects = int(input('Please enter the number of subjects : '))
  print('')
except:
  print('Error : Please enter a whole value number, for the number of subjects!')
  exit()

 # The below two counter varibales are for totalling the number of obtained marks
 # and, the number of total marks. 

total_obtained_marks = 0
total_total_marks = 0

# The below loop is iterated the number of subjects we have.

while how_many_subjects != 0: 

  subject_name = input('Please enter your subject name : ')
  
  # The below block of code asks for the obtained marks and takes care for error if
  # encountered. (i.e. wrong input value)
  try:
    obtained_marks = float(input('Please enter your obtained marks : '))
    total_obtained_marks = total_obtained_marks + obtained_marks
  except:
    print('Please enter an integral or fractional value for obtained marks!')
    exit()


  # The below block of code prompts for the total marks and counts for any error 
  # if it occurs. (i.e. wrong value of input.)
  try:
    total_marks = float(input('Please enter the total marks in the subject : '))

    if total_marks < obtained_marks:
      print('Error : Obtained marks cannot be greater than Total marks!')
      exit()

    total_total_marks = total_total_marks + total_marks
    print('')

  except:
    print('Please enter a valid entry for total marks (i.e. either an integral or a fractional value)!')
    exit()
  
  # Finite loop constraint :-
  how_many_subjects -= 1


# Final answer :-
print('Your total percentage is : ', (total_obtained_marks/total_total_marks)*100, "%")
