from django.db import models

# Create your models here.

"""
1. SCHOOL
*name
address
*state
phone
email
slogan
logo
*contact_person
*contact_person_phone
*school levels: nurs, prim, jun sec, sen sec
class count: 0-6, 7-15, above 15 e.g. jss1 is one class, jss2 is another class; regardless of A, B, C, D sections within the classes
*primary_color
secondary_color

2. TERM
*name
duration
set_as_current (choices 0, 1)Yes, No
*school (foreignKey)

3. SESSION
*name
duration
set_as_current (choices 0, 1)Yes, No
*school (foreignKey)

4. STUDENT
*fname
mname
*sname
*gender
parent1
*parent1_phone
parent2
parent2_phone
address
email
*school (foreignKey)
curr_classs (foreignKey)
subjects (ManyToMany)
passport

3. CLASSS
*name
level
curr_session (foreignKey)
curr_term (foreignKey)

4. SUBJECT
*name
level
orientation
"""