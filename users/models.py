from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField
from django_countries.fields import CountryField

''' GENDER CHOICES '''
GENDER_CHOICES = (
  ("", ""),
  ("Male", "Male"),
  ("Female", "Female"),
)
choices = GENDER_CHOICES

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
  location = models.CharField(max_length=200, default='')
  status_word = models.CharField(max_length=30, default='')
  bio = models.TextField(max_length=500, default='')
  position = models.CharField(max_length=50, default='')
  gender = models.CharField(max_length=50, default='', choices = GENDER_CHOICES)
  date_of_birth = models.DateField(verbose_name=_("Birthday"), null=True)
  country = CountryField(blank_label='(select country)')
  address = models.CharField(max_length=300, default='')
  postal_code = models.CharField(max_length=10, default='')
  phone = PhoneField(blank=True, help_text='Enter phone number')
  profile_photo = models.ImageField(_("Profile Photo"), upload_to='media_house', height_field=None, width_field=None, max_length=None, default='')
  email_confirmed = models.BooleanField(default=False)
  def __str__(self):
      return self.user.username

  def __unicode__(self):
      return self.user.username

  @property
  def get_photo_url(self):
      if self.profile_photo and hasattr(self.profile_photo, 'url'):
          return self.profile_photo.url
      else:
          return "/static/images/dummy-avatar.jpg"

''' Signal Fired After  User Created '''
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
        # PricingPerSMSPerUserToPurchase.objects.get_or_create(user=instance)
        # BonusAccount.objects.get_or_create(user=instance)
    # instance.userprofile.save()
    # instance.user_profile.save()
    # instance.smspricingperuser.save()
    # instance.user_bonus.save()