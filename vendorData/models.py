from django.db import models

# Create your models here.

class Sport(models.Model):
        name = models.CharField(primary_key=True,max_length=30)
	description = models.CharField(max_length = 500)

class Club(models.Model):
	name = models.CharField(primary_key=True,max_length=50)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	pincode = models.PositiveIntegerField(max_length=6)
	country = models.CharField(max_length=30)
	mobile1 = models.BigIntegerField()
	mobile2 = models.BigIntegerField()
	landline = models.BigIntegerField()
	longitude = models.DecimalField(max_digits=11,decimal_places=8)
	latitude = models.DecimalField(max_digits=10,decimal_places=8)
	email = models.EmailField()
	pictures = models.URLField(max_length=100)
	sports_name = models.ManyToManyField(Sport, through='SportClub')

class SportClub(models.Model):
	club_name = models.ForeignKey(Club)
	sport_name = models.ForeignKey(Sport)
        sports_type = models.CharField(max_length=7)
        arena_type = models.CharField(max_length=20)
        open_hours = models.IntegerField()
	coaching_available = models.BooleanField()
	membership_available = models.BooleanField()

class Coaching(models.Model):
	club_name = models.ForeignKey(Club)
	sports_name = models.ForeignKey(Sport)
	coaching_fee = models.IntegerField()
        coaching_time = models.IntegerField()
        coaching_start_date = models.DateField()
        coaching_end_date = models.DateField()

class Membership(models.Model):
	club_name = models.ForeignKey(Club)
	sports_name = models.ForeignKey(Sport)
	membership_fee = models.IntegerField()
	duration_in_months = models.IntegerField()

class Slot(models.Model):
	club_name = models.ForeignKey(Club)
	sports_name = models.ForeignKey(Sport)
	date = models.DateField()
	slot_duration = models.PositiveSmallIntegerField()
	slot_availability = models.IntegerField()

class Event(models.Model):
	clubName = models.ForeignKey(Club)
	sportsName = models.ForeignKey(Sport)
	eventName = models.CharField(max_length=50)
	eventPrice = models.IntegerField()
	eventDate = models.DateField()
	duration = models.PositiveSmallIntegerField()
	eventMen = models.BooleanField()
	eventWomen = models.BooleanField()
	singlesMen = models.BooleanField()
	singlesWomen = models.BooleanField()
	doublesMen = models.BooleanField()
	doublesWomen = models.BooleanField()
	mixedDoubles = models.BooleanField()

class Booking(models.Model):
	bookingId = models.CharField(max_length = 7)
	clubName = models.ForeignKey(Club)
	sportsName = models.ForeignKey(Sport)
	date = models.DateField()
	time = models.TimeField()
	
