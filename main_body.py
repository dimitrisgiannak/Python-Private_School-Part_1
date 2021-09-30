from random import *
import sys
from person_class import Trainer as T
from person_class import Student as S
from CA_class import Course as C
from CA_class import Assignment as A
import menu





def dummy():

    word_len = randint(5 , 10)
    random_word = sample((dummy_list) , word_len)
    joined_word = "".join(random_word).capitalize()

    return joined_word





def relate_func(course , defined_STA_list , assignment_list = None):

   relation_defined = []

   if assignment_list:
      for relation_per_course in defined_STA_list:
         if course == relation_per_course.course:
            relation_defined.append(relation_per_course)
      for relation in relation_defined:
         for asgmnt in assignment_list:
            if course == asgmnt.course:
               print(asgmnt ,'\n')
         print(relation,'\n')
   else:
      for relation_per_course in defined_STA_list:
         if course == relation_per_course.course:
            print(relation_per_course,'\n')







def multiple_courses_func(stud_list):

   copied_stud_list = stud_list.copy()
   multi_list = []


   for student in (stud_list):
      for copied_student in copied_stud_list:
         if student.pv_only() == copied_student.pv_only() and student.course != copied_student.course:
            multi_list.append(student)
   multi_set = set(multi_list)

   for multi_stud_course in multi_set:
      print(multi_stud_course)






def main():

   print('Welcome to the main input menu\n\nHere you will input all the data you need')

   while True:
      print('1: Courses\n2: Trainers\n3: Students\n4: Assignments\n5: Exit Inupt Menu\n6: Exit System')
      choice = input('What would you like to choose\n')
      if choice == '5':
         if courses_board and students_board and trainers_board and assignments_board:
            print('You will now exit the main input menu and go to Output Menu\n')
            output()
         else:
            print("You need to input data in all categories at least once\n")

      elif choice == "6":
         print('\n'*3)
         print('-'*10,exiting_program_message,'-'*10)
         sys.exit()

      elif choice == '1':

         while True:
            print("1: User input\n2: Dummy data")
            in_choice = input("Do you want to input data or use dummy?\n")
            if in_choice == "1":
               crs = C.from_input()
               courses_board.append(crs)
               print(crs)
               print(success_message.center(75))
               break
            elif in_choice == "2":
               crs = C(dummy() , dummy() , dummy() , dummy())
               courses_board.append(crs)
               print(crs)
               print(success_message.center(75))
               break
            else:
               print(error_message.center(70))

      elif choice == '2':
         while True:
            print("1: User input\n2: Dummy data")
            in_choice = input("Do you want to input data or use dummy?\n")
            if in_choice == "1":
               trnrs = T.from_input(courses_board)
               trainers_board.append(trnrs)
               print(trnrs)
               print(success_message.center(75))
               break
            elif in_choice == "2":
               trnrs = T(dummy() , dummy() , dummy() , dummy())
               trainers_board.append(trnrs)
               print(trnrs)
               print(success_message.center(75))
               break
            else:
               print(error_message.center(70))

      elif choice == '3':
          while True:
            print("1: User input\n2: Dummy data")
            in_choice = input("Do you want to input data or use dummy?\n")
            if in_choice == "1":
               sdnt = S.from_input(courses_board)
               students_board.append(sdnt)
               print(sdnt)
               print(success_message.center(75))
               break
            elif in_choice == "2":
               sdnt = S(dummy() , dummy() , dummy() , dummy() , dummy() , dummy())
               students_board.append(sdnt)
               print(sdnt)
               print(success_message.center(75))
               break
            else:
               print(error_message.center(70))


      elif choice == '4':
         while True:
            print("1: User input\n2: Dummy data")
            in_choice = input("Do you want to input data or use dummy?\n")
            if in_choice == "1":
               assgn = A.from_input(courses_board)
               assignments_board.append(assgn)
               print(assgn)
               print(success_message.center(75))
               break
            elif in_choice == "2":
               assgn = A(dummy() , dummy() , dummy() , dummy() , dummy() , dummy())
               assignments_board.append(assgn)
               print(assgn)
               print(success_message.center(75))
               break
            else:
               print(error_message.center(70))


      else:
         print(error_message.center(70))







def output():
   print('Welcome to the output menu\n\nNow you can see all the data and how they relate to each other\n')
   while True:
      print('1: All Courses                 6: All Trainers per Course\n'
         '2: All Trainers                7: All Assignments per Course\n'
         '3: All Students                8: All Assignments per Students per Course\n'
         '4: All Assignments             9: Students in more than one Courses\n'
         '5: All Students per Course    10: Exit Output Menu and go to Input Menu\n'
                                 '11: Exit System\n'
                                 )
      choice = input('What would you like to choose\n')
      if choice == '10':
         print('You will now exit the output menu and go to input menu')

         main()

      elif choice == "11":
         print('\n'*3)
         print('-'*10,exiting_program_message,'-'*10)
         sys.exit()

      elif choice == '1':
         for course in courses_board:
            print(course,'\n')

      elif choice == '2':
         for trainer in trainers_board:
            print(trainer,'\n')

      elif choice == '3':
         for student in students_board:
            print(student,'\n')

      elif choice == '4':
         for assignment in assignments_board:
            print(assignment,'\n')

      elif choice == '5':
         roll = 0
         while True:
            for crs in courses_board:
                  roll += 1
                  print(roll,': ' + crs.course_title)

            choice1 = input('Please choose the course title accoring to the NUMBER! \n')
            if not choice1:
               print(error_message.center(75),'\n')

            else:

               for i in range(1 , roll + 1):
                  if choice1 == str(i):
                     relate_func(courses_board[i - 1].course_title , students_board)
               print('Students per Course :')
               roll = 0
               break

      elif choice == '6':
         roll = 0

         while True:
            for crs in courses_board:
                  roll += 1
                  print(roll,': ' + crs.course_title)

            choice1 = input('Please choose the course title accoring to the NUMBER! \n')
            if not choice1:
               print(error_message.center(75),'\n')
            else:

               for i in range(1 , roll + 1):
                  if choice1 == str(i):
                     relate_func(courses_board[i - 1].course_title , trainers_board)
               print('Trainers per Course :')
               roll = 0
               break

      elif choice == '7':
         roll = 0
         while True:
            for crs in courses_board:
                  roll += 1
                  print(roll,': ' + crs.course_title)

            choice1 = input('Please choose the course title accoring to the NUMBER! \n')
            if not choice1:
               print(error_message.center(75),'\n')
            else:

               for i in range(1 , roll + 1):
                  if choice1 == str(i):
                     relate_func(courses_board[i - 1].course_title , assignments_board)
               print('Assignments per Course :')
               roll = 0
               break

      elif choice == '8':
         roll = 0
         while True:
            for crs in courses_board:
                  roll += 1
                  print(roll,': ' + crs.course_title)

            choice1 = input('Please choose the course title accoring to the NUMBER! \n')
            if not choice1:
               print(error_message.center(75),'\n')
            else:

               for i in range(1 , roll + 1):
                  if choice1 == str(i):
                     relate_func(courses_board[i - 1].course_title , students_board , assignments_board)
               print('Assignments per Student per Course :')
               roll = 0
               break

      elif choice == '9':
         multiple_courses_func(students_board)
      else:
         print(error_message.center(70))



success_message = 'Successfully added\n'
error_message = 'Please give me a valid input\n'
redirection_message = 'The input was invalid.You will be redirected to storage menu\n'
exiting_program_message = 'You will now exit the program.Waiting for your feedback! '


courses_board = list()
trainers_board = list()
students_board = list()
assignments_board = list()


dummy_list = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k',
              'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' ,
              'w' , 'x' , 'y' , 'z']


course1 = C("cb1PTPY" , "Python" , "24 weeks" , "Part time")
course2 = C("cb1PTJV" , "Java" , "24 weeks" , "Part time")
course3 = C("cb1PTJS" , "Javascript" , "24 weeks" , "Part time")
course4 = C("cb1PTC#" , "C#" , "24 weeks" , "Part time")
courses_board = [course1 , course2 , course3 , course4]


if __name__ == "__main__":
   main()












