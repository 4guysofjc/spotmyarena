from django.db import models
from ratings.models import Ratings

# Create your models here.

class Sport(models.Model):
	sport_id =models.CharField(primary_key=True,max_length=7)
        sport_name = models.CharField(max_length=30)
	sport_description = models.CharField(max_length = 500)
	
	def __unicode__(self):
            return self.sport_name

class Club(models.Model):
	club_id = models.CharField(primary_key=True,max_length=7)
	club_name = models.CharField(max_length=50)
	club_address = models.CharField(max_length=100)
	club_city = models.CharField(max_length=30)
	club_area = models.CharField(max_length=30)
	club_state = models.CharField(max_length=30)
	club_pincode = models.PositiveIntegerField(max_length=6)
	club_country = models.CharField(max_length=30)
	club_mobile1 = models.BigIntegerField()
	club_mobile2 = models.BigIntegerField()
	club_landline = models.BigIntegerField()
	club_longitude = models.DecimalField(max_digits=11,decimal_places=8)
	club_latitude = models.DecimalField(max_digits=10,decimal_places=8)
	club_email = models.EmailField()
	club_pictures = models.URLField(max_length=100)
	club_sport_id = models.ManyToManyField(Sport, through='SportClub')
        club_open_hours_am = models.PositiveBigIntegerField()
        club_open_hours_pm = models.PositiveBigIntegerField()
	club_rating = Ratings()
        def __unicode__(self):
            return self.club_name

class SportClub(models.Model):
	club_id = models.ForeignKey(Club)
	sport_id = models.ForeignKey(Sport)
        sports_type = models.CharField(max_length=7)
        arena_type = models.CharField(max_length=20)
	cost_weekdays = models.PositiveIntegerField()
	cost_weekends = models.PositiveIntegerField()
	slot_duration = models.PositiveSmallIntegerField()
	coaching_available = models.BooleanField()
	membership_available = models.BooleanField()

class Coaching(models.Model):
	coaching_club_id = models.ForeignKey(Club)
	coaching_sport_id = models.ForeignKey(Sport)
	coaching_fee = models.IntegerField()
        coaching_start_time = models.TimeField()
	coaching_end_time = models.TimeField() 
        coaching_start_date = models.DateField()
        coaching_end_date = models.DateField()
	coaching_total_seats = models.PositiveSmallIntegerField()
	coaching_filled_seats = models.PositiveSmallIntegerField()

class Membership(models.Model):
	membership_club_id = models.ForeignKey(Club)
	membership_sport_id = models.ForeignKey(Sport)
	membership_fee = models.IntegerField()
	membership_duration_in_days = models.PositiveSmallIntegerField()

class Availability(models.Model):
	availability_date = models.DateField(primary_key=True)
	availability_club_id = models.ForeignKey(Club)
	availability_sport_id = models.ForeignKey(Sport)
	availability_am = models.PositiveBigIntegerField()
	availability_pm = models.PositiveBigIntegerField()

class Event(models.Model):
	event_club_id = models.ForeignKey(Club)
	event_sport_id = models.ForeignKey(Sport)
	event_name = models.CharField(max_length=50)
	event_price = models.IntegerField()
	event_date = models.DateField()
	event_duration = models.PositiveSmallIntegerField()
	event_men = models.BooleanField()
	event_women = models.BooleanField()
	event_singles_men = models.BooleanField()
	event_singles_women = models.BooleanField()
	event_doubles_men = models.BooleanField()
	event_doubles_women = models.BooleanField()
	event_mixed_doubles = models.BooleanField()

class Booking(models.Model):
	booking_id = models.CharField(primary_key=True,max_length = 7)
	booking_club_id = models.ForeignKey(Club)
	booking_sports_id = models.ForeignKey(Sport)
	booked_slot = models.PositiveBigIntegerField()
	booking_date = models.DateField()
	booking_time = models.TimeField()
	
