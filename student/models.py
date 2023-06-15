from django.db import models
from school.models import School, Classs

class Student(models.Model):
	GENDER = (
		('Female', 'Female'), 
		('Male', 'Male'), 
		('Other', 'Other'), 
    )
	school = models.ForeignKey(School, related_name='student', on_delete=models.CASCADE)
	classs = models.ForeignKey(Classs, related_name='student', on_delete=models.CASCADE)
	fname = models.CharField(max_length=45)
	mname = models.CharField(max_length=45)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, choices=GENDER)
	phone = models.CharField(max_length=12, blank=True)
	email = models.CharField(max_length=45, blank=True)
	address = models.CharField(max_length=150, blank=True)
	contact_person = models.CharField(max_length=60, blank=True, null=True)
	contact_person_phone = models.CharField(max_length=30, blank=True)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	# logo

"""
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
"""