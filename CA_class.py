error_message = 'Please give me a valid input\n'
error_message2 = "The number is out of range.Please choose according to numbers given\n"


class Course:
   
   '''Class Course.Follows the same routine as Students class '''
   
   form = {'course_title' : 'Course Title\n' , 'course_description' : 'Course Description\n'}

   specify_course = ('course_title',)
   
   def __init__(self , course_title , course_language , course_description , course_type):
      self.course_title = course_title
      self.course_language = course_language
      self.course_description = course_description               
      self.course_type = course_type

   @classmethod
   def from_input(cls):
      course_form = {}
      for key,value in cls.form.items():

         if key in cls.specify_course:
            while True:
               print('1: FTPY\n2: PTPY\n3: FTJV\n4: PTJV\n5: FTJVS\n6: PTJVS\n7: FTC#\n8: PTC#\n')
               ch_course = input('Please choose the course title accoring to the NUMBER!This will be the second half of the full title.\nAfter that you are going to give a specific code for it.( ..code..FTPY)\n')
               
               if ch_course:
                  if ch_course == '1':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'FTPY'
                     course_form['course_language'] = 'Python'
                     course_form['course_type'] = 'Full time'
                     break
                  elif ch_course == '2':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'PTPY'
                     course_form['course_language'] = 'Python'
                     course_form['course_type'] = 'Part time'
                     break
                  elif ch_course == '3':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'FTJV'
                     course_form['course_language'] = 'Java'
                     course_form['course_type'] = 'Full time'
                     break
                  elif ch_course == '4':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'PTJV'
                     course_form['course_language'] = 'Java'
                     course_form['course_type'] = 'Part time'
                     break
                  elif ch_course == '5':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'FTJS'
                     course_form['course_language'] = 'Javascript'
                     course_form['course_type'] = 'Full time'
                     break
                  elif ch_course == '6':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'PTJS'
                     course_form['course_language'] = 'Javascript'
                     course_form['course_type'] = 'Part time'
                     break
                  elif ch_course == '7':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'FTC#'
                     course_form['course_language'] = 'C#'
                     course_form['course_type'] = 'Full time'
                     break
                  elif ch_course == '8':
                     specify_title = input('Please edit the code of the title \n')
                     course_form[key] = specify_title + 'PTC#'
                     course_form['course_language'] = 'C#'
                     course_form['course_type'] = 'Part time'
                     break
                  else:
                     print(error_message.center(70))
               
               elif not ch_course:
                  course_form[key] = 'To implement'
                  course_form['course_language'] = 'To implement'
                  course_form['course_type'] = 'To implement'
                  break      
                  
         else:
            course_form[key] = input(value)
            if not course_form[key]:
               course_form[key] = 'To implement'
      return cls(**course_form)
      

   def __str__(self):
      return (f'-->Course Title       : {self.course_title}\n '
              f'  Course Language    : {self.course_language}\n'       
              f'   Course Description : {self.course_description}\n'
              f'   Course Type        : {self.course_type}\n')

              
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Assignment:
   
   '''Class Assignment.Follows the same routine as Students class'''
   
   form = {'course' : 'Course Title\n' ,'title' : 'Assignment Title\n','description' : 'Assignment Description\n',
           'sub_day' : 'Date of Submission\n','total_mark' : 'Total Mark\n','oral_mark' : 'Oral Mark\n'}

   specify_course = ('course',)
   
   def __init__(self,course,title,description,sub_day,total_mark,oral_mark):
      self.course = course
      self.title = title
      self.description = description
      self.sub_day = sub_day
      self.total_mark = total_mark
      self.oral_mark = oral_mark

   @classmethod                                                  
   def from_input(cls , courses_board):
      asgmnt_form = {}
      for key,value in cls.form.items():

         if key in cls.specify_course:  
             while True:
               roll = 0
               for crs in courses_board:
                  roll += 1
                  print(roll,': ' + crs.course_title)
               
               try:
                  ch_course = input('Please choose the course title accoring to the NUMBER! \n')
              
                  if not ch_course:
                     print(error_message.center(75),'\n')
                     

                  elif ch_course:
                     
                     int_ch = int(ch_course)
                     if int_ch and int_ch >= 1 and int_ch <= roll:
                        for i in range(1 , roll + 1):
                           if int_ch == i:
                              asgmnt_form[key] = (courses_board[i - 1].course_title)
                        break

                     else:
                        print(error_message2.center(75),'\n')
                       
                     
               except ValueError:
                  print(error_message.center(75),'\n')
         else:
            asgmnt_form[key] = input(value)
            if not asgmnt_form[key]:                             
               asgmnt_form[key] = 'Test data'                              
      return cls(**asgmnt_form) 


   def __str__(self):
      return (f'-->Course Assignment     : {self.course}\n '
              f'  Assignment Title      : {self.title}\n '
              f'  Assignment Description: {self.description}\n '
              f'  Submission Date       : {self.sub_day}\n'
              f'   Total Mark            : {self.total_mark}\n'
              f'   Oral Mark             : {self.oral_mark}\n')
  
              
   
   
   
              
              
   
