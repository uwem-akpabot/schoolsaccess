from django.contrib.auth.models import User
from django.db import models

class School(models.Model):
	LEVEL = (
		('Primary', 'Primary'), 
		('Secondary', 'Secondary'), 
		('All', 'All'), 
    )
	COUNT = (
		('0-6', '0-6'), 
		('7-15', '7-15'), 
		('Above 15', 'Above 15'), 
    )
    # patient = models.ForeignKey(Patient, related_name='soapnote', on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	address = models.TextField(blank=True, null=True)
	state = models.CharField(max_length=15, blank=True, null=True)
	phone = models.CharField(max_length=12, blank=True, null=True)
	email = models.CharField(max_length=100, blank=True, null=True)
	slogan = models.CharField(max_length=45, blank=True, null=True)
	contact_person = models.CharField(max_length=35)
	contact_person_phone = models.CharField(max_length=24)
	school_level = models.CharField(max_length=10, choices=LEVEL)
	class_count = models.CharField(max_length=10, blank=True, null=True, choices=COUNT)
	school_colours = models.CharField(max_length=45, blank=True, null=True)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
	# logo

class Sesssion(models.Model):
	SESSIONS = (
		('2022/2023', '2022/2023'), 
		('2023/2024', '2023/2024'), 
		('2024/2025', '2024/2025'), 
		('2025/2026', '2025/2026'), 
		('2026/2027', '2026/2027'), 
		('2027/2028', '2027/2028'), 
		('2028/2029', '2028/2029'), 
		('2029/2030', '2029/2030'), 
		('2030/2031', '2030/2031'), 
    )
	school = models.ForeignKey(School, related_name='sesssion', on_delete=models.CASCADE)
	name = models.CharField(max_length=10, choices=SESSIONS)
	is_current = models.BooleanField(default=False)
	duration_start = models.CharField(max_length=20, blank=True, null=True) 
	duration_end = models.CharField(max_length=20, blank=True, null=True)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
class Term(models.Model):
	TERMS = (
		('Primary', 'Primary'), 
		('Secondary', 'Secondary'), 
		('All', 'All'), 
    )
	school = models.ForeignKey(School, related_name='term', on_delete=models.CASCADE)
	name = models.CharField(max_length=10, choices=TERMS)
	is_current = models.BooleanField(default=False)
	duration_start = models.CharField(max_length=20, blank=True, null=True) 
	duration_end = models.CharField(max_length=20, blank=True, null=True)
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

class Classs(models.Model):
	school = models.ForeignKey(School, related_name='classs', on_delete=models.CASCADE)
	sesssion = models.ForeignKey(Sesssion, related_name='classs', on_delete=models.CASCADE)
	term = models.ForeignKey(Term, related_name='classs', on_delete=models.CASCADE)
	name = models.CharField(max_length=25) 
	subclass = models.CharField(max_length=25, blank=True, null=True) 
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

class Subject(models.Model):
	school = models.ForeignKey(School, related_name='subject', on_delete=models.CASCADE)
	classs = models.ForeignKey(Classs, related_name='subject', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	orientation = models.CharField(max_length=15, blank=True, null=True) 
	created_by = models.CharField(max_length=15)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	# date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
