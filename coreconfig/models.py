from django.db import models

# Create your models here.

class DashboardConfig(models.Model):
	site_name = models.CharField(max_length=20, default='VBP')
	# keywords = models.TextField(max_length=2000, default='VBP')
	# content_field = models.TextField(max_length=2000, default='VBP - Best VTU site', name="Site Description")
	# gradient_background_color1 = models.CharField(max_length=20, default='#df4ec3')
	# gradient_background_color2 = models.CharField(max_length=20, default='#be22a8')
	# button_color1 = models.CharField(max_length=20, default='#bddf4e')
	# button_color2 = models.CharField(max_length=20, default='#000')
	# menu_color = models.CharField(max_length=20, default='#fff')
	site_logo = models.ImageField(default='', null=True, blank=True)
	# paystack_sk_token = models.CharField(max_length=100, default='', blank=True, null=True)
	# paystack_pk_token = models.CharField(max_length=100, default='', blank=True, null=True)
	# amount_funding_limit_through_paysatack = models.PositiveIntegerField(default=2450)
	# bank_name = models.CharField(max_length=300, default='', blank=True, null=True)
	# bank_account_number = models.CharField(max_length=300, default='', blank=True, null=True)
	# bank_account_name = models.CharField(max_length=300, default='', blank=True, null=True)
	# voucher_prefix = models.CharField(max_length=3, default='', blank=True, null=True)
	# allow_payment_for_apikey = models.BooleanField(default=False, verbose_name='Allow User to Pay to access your API')

	def __str__(self):
		return 'site configuration'

	class Meta:
		verbose_name = 'Site Dashboard Configuration'
		verbose_name_plural = 'Site Dashboard Configurations'

# class SmtpEmailSettings(models.Model):
#   smtp_email_host = models.CharField(max_length=500, default='smtp.example.com')
#   smtp_email_host_user = models.CharField(max_length=500, default='apikey')
#   smtp_email_host_sender_address = models.CharField(max_length=500, default='example@example.com')
#   smtp_email_host_password = models.CharField(max_length=500, default='password')
#   smtp_email_host_port = models.IntegerField(default='587')
#   smtp_use_tls = models.BooleanField(default=False)
#   smtp_use_ssl = models.BooleanField(default=False)
#   smtp_timeout = models.IntegerField(default=10)
  
#   def __str__(self):
#     return 'Email configuration'
  
#   class Meta:
#     verbose_name = 'Email Configuration'
#     verbose_name_plural = 'Email Configurations'