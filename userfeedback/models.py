from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
RATING_CHOICES = (
	('1',"1"),
	('2',"2"),
	('3',"3"),
	('4',"4"),
	('5',"5"),
)

NEIGHBOURHOOD_CHOICES = (
		('WESTLANDS', "Westlands"),
		('EASTLEIGH',"Eastleigh"),
		('UPPER HILL', "Upper Hill"),
		('LAVINGTON', "Lavington"),
		('NAIROBI WEST', "Nairobi West"),
	)

class userComments(models.Model):

	name = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500)
	phone_number = PhoneNumberField()
	neighbourhood = models.CharField(max_length=100,choices=NEIGHBOURHOOD_CHOICES)
	rating = models.CharField(max_length=10,choices=RATING_CHOICES)

	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "userComments"