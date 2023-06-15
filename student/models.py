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
	mname = models.CharField(max_length=30, blank=True, null=True)
	sname = models.CharField(max_length=30)
	gender = models.CharField(max_length=6, choices=GENDER)
	address = models.TextField(blank=True, null=True)
	parent1 = models.CharField(max_length=25, blank=True, null=True)
	parent1_phone = models.CharField(max_length=12)
	parent2 = models.CharField(max_length=25, blank=True, null=True)
	parent2_phone = models.CharField(max_length=12, blank=True, null=True)
	email = models.CharField(max_length=45, blank=True)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	# passport photo
