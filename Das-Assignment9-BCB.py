# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 00:45:35 2016

@author: Prerna 

BMI-544; HW-9
"""

## 1. Create a Python script that makes a connection to the Student database

import psycopg2 as pg2

con = pg2.connect(host='localhost', port='5432', user='postgres', 
                       database='StudentDatabase', password='')
                       
print ('Opened database successfully')                     
                       
cur = con.cursor()

## 2. Write a function to select and print student name, course description, 
## and grade (using a JOIN statement).

cur.execute('SELECT first_name, last_name, description, numeric_grade FROM STUDENT s JOIN GRADE g ON s.Student_id  = g.Student_id JOIN SECTION se ON se.Section_id = g.Section_id JOIN Course c ON c.Course_no = se.Course_no')
rows = cur.fetchall()
for row in rows:
    print (row)

## 3. Fill in the input for an SQL injection attack that returns a list of grades
## rather than a list of students

input = '' or 1=1;
query = "SELECT * from student where first_name = '%s'"% (input,)
cursor.execute(query)


## 4. Now modify the query string and cursor.execute() statement to protect against an injection attack

input = '' or 1=1;
query = "SELECT * from student where first_name = '%s'" AND numeric_grade = '%t'% (input1, input2)
cursor.execute(query)

## 5.	Create Python classes for each table in the Student database

class Student():
    def __init__(self, student_id, salutation, first_name, last_name, street_address, ZIP, phone, employer, registration_date, created_by, created_date, modified_by, modified_date):
        self.student_id = student_id 
        self.salutation = salutation
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.ZIP = ZIP
        self.phone = phone
        self.employer = employer
        self.registration_date = registration_date
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date
        
class Grade():
    def __init__(self, student_id, section_id, grade_type_code, grade_code_occurrence, numeric_grade, comments, created_by, created_date, modified_by, modified_date):
        self.student_id = student_id 
        self.section_id = section_id
        self.grade_type_code = grade_type_code
        self.grade_code_occrrence = grade_code_occurrence
        self.numeric_grade = numeric_grade
        self.comments = comments
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date        

class Course():
    def __init__(self, course_no, description, cost, prerequisite, created_by, created_date, modified_by, modified_date):
        self.course_no = course_no 
        self.description = description
        self.cost = cost
        self.prerequisite = prerequisite
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date 
        
class Section():
    def __init__(self, section_id, course_no, section_no, start_date_time, location, instructor_id, capacity, created_by, created_date, modified_by, modified_date):
        self.section_id = section_id
        self.course_no = course_no 
        self.section_no = section_no
        self.start_date_time = start_date_time
        self.location = location
        self.instructor_id = instructor_id
        self.capacity = capacity
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date  
        
class Instructor():
    def __init__(self, instructor_id, salutation, first_name, last_name, street_address, ZIP, phone, created_by, created_date, modified_by, modified_date):
        self.instructor_id = instructor_id
        self.salutation = salutation 
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.ZIP = ZIP
        self.phone = phone
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date        

class Zipcode():
    def __init__(self, ZIP, city, state,created_by, created_date, modified_by, modified_date):
        self.ZIP = ZIP
        self.city = city 
        self.state = state
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date 
        
class Enrollment():
    def __init__(self, student_id, section_id, enroll_date, final_grade, created_by, created_date, modified_by, modified_date):
        self.student_id = student_id
        self.section_id = section_id
        self.enroll_date = enroll_date
        self.final_grade = final_grade
        self.created_by = created_by
        self.created_date = created_date
        self. modified_by = modified_by
        self.modified_date = modified_date 

### 6. Use FOR loops instead of a JOIN statement to populate objects for student, section, course, and grade. Write a function that will print the same information as in #2, this time using the Python objects.

cur.execute('SELECT first_name, last_name, description FROM Student, Course')
results = cur.fetchall()
for r in results:
    print r

## 7. Iterate through the student objects and use a Python regular expression to print out last names starting with the letters "Ma".

import re

cur.execute('SELECT last_name FROM Student')
result7 = cur.fetchall()
last_names = []
for r in result7:
    last_names.append( str(r[0].strip('()')))
    
for l in last_names:
    match = re.search('^Ma.*', l)
    if match:
        print match.group()
    

## 8. Which instructors (first and last name) teach sections with the highest capacities? Use the Python objects to answer this question.

cur.execute('SELECT instructor_id, capacity FROM Section')

result8 = cur.fetchall()

capacity = []
for s in result8:
    capacity.append(s[1])
    
   
 
inst_id = []
for r in result8:
    if r[1] == max(capacity):
        inst_id.append(r[0])
   
    
cur.execute('SELECT first_name, last_name, instructor_id FROM Instructor')
result9 = cur.fetchall()
for r in result9:
    if r[2] in inst_id:
        print r[0], r[1]

 