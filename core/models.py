from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Events(models.Model):
    name=models.TextField(max_length=50)
    fee=models.IntegerField(default=100)
    maxteamsize=models.IntegerField(default=1)
    minteamsize=models.IntegerField(default=1)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:detail_of_event",kwargs={"id":self.id})

    def get_register_url(self):
        return reverse("core:register_in_event",kwargs={"id":self.id})
        


	
	
class Team(models.Model):
    name=models.TextField(max_length=25,blank=False)
    teamsize=models.IntegerField(default=1)
    description=models.TextField(help_text='enter name(s) of your team.')
    event=models.ForeignKey(Events,on_delete='models.CASCADE')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=False,help_text='mention your year and course')
    institute=models.CharField(max_length=50,default='myinstitute',blank=False)
    location = models.CharField(max_length=30,blank=False)
    birth_date = models.DateField(null=True,blank=False)
    teams=models.ManyToManyField(Team)
    events=models.ManyToManyField(Events)
    phone_number = PhoneNumberField(default='+44 113 8921113')
    amount=models.IntegerField(default=0)
    paid_status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()        








