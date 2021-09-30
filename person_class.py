error_message = 'Please give me a valid input\n'
error_message2 = "The number is out of range.Please choose according to numbers given\n"



class Person:
   
   '''Super class Person.This is the parent Class for Student and Trainer.'''
   
   def __init__(self,name,surname):
      self.name = name
      self.surname = surname
      
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          

class Student(Person):
  

   '''Subclass Student IS A Child Class of Person Class.Student HAS A course and ctype
      from Course Class.(Coursecourse_language and Coursecourse_type with composition)'''
   
   form = {'name' : 'First name\n','surname' : 'Last name\n','birthdate' : 'Date of birth\n', 
           'identification' : 'ID(Identification)\n',                                         
           'course' : 'Course Title\n',
           'tuition_fees' : 'Tuition fees\n'
           }

   specify_course = ('course')        
   
   def __init__(self,name,surname,birthdate,identification,course,tuition_fees):
      super().__init__(name,surname)                            
      self.birthdate = birthdate
      self.id = identification
      self.email = self.name + '.' + self.surname + '@private_school.org'
      self.course = course  
      self.tfees = tuition_fees
      self.__index = name + surname + identification  
                                                     
   @classmethod
   def from_input(cls , courses_board):  
                                                     
      student_form = {}                               
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
                              student_form[key] = (courses_board[i - 1].course_title)
                        break

                     else:
                        print(error_message2.center(75),'\n')
                                           
               except ValueError:
                  print(error_message.center(75),'\n')
                  
         else:
            student_form[key] = input(value)
            if not student_form[key]:                                  
               student_form[key] = 'Test data'          
      
      return cls(**student_form)                      
                                                     
                                                     
   def __str__(self):                                    
      return (f'->>Full Name      : {self.name} {self.surname}\n'
                 f'   Date of birth  : {self.birthdate}\n'
                 f'   ID             : {self.id}\n'
                 f'   Email          : {self.email}\n'
                 f'   Course and type: {self.course}\n'
                 f'   Tuition fees   : {self.tfees}\n')

                                 
   def pv_only(self):                               
      return self.__index                            
      
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
            
class Trainer(Person):
   
   
   '''Subclass Trainer IS A Child Class of Person Class.Student HAS A course(named Subject here)
      from Course Class.(Coursecourse_language with composition)'''
   
   form = {'name' : 'First name\n','surname' : 'Last name\n','identification' : 'ID(Identification)\n',
           'course':'Course Title\n'}

   specify_course = ('course')       
   
   def __init__(self,name,surname,identification,course):
      super().__init__(name,surname)
      self.id = identification
      self.email = 'tr' + self.name + '.' + self.surname + '@private_school.org'
      self.course = course


   @classmethod
   def from_input(cls , courses_board):
      
      trainer_form = {}
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
                              trainer_form[key] = (courses_board[i - 1].course_title)
                        break

                     else:
                        print(error_message2.center(75),'\n') 

               except ValueError:
                  print(error_message.center(75),'\n')
                                
         else:
            trainer_form[key] = input(value)
            if not trainer_form[key]:                                 
               trainer_form[key] = 'Test data'          
            
      return cls(**trainer_form)


   def __str__(self):                               
      return (f'->>Full name: {self.name} {self.surname}\n'
              f'      ID       : {self.id}\n'
              f'      Email    : {self.email}\n'
              f'      Subject  : {self.course}\n')
      
 
