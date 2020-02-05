from celery import shared_task
# from saas_vbp.celery import app
from django.db import connection
from django.core import mail
from django.core.mail.backends.smtp import EmailBackend
# from coreconfig.models import SmtpEmailSettings
from django.conf import settings

@shared_task
def sending_mail(subject, message, contact_list):

    try:
        con = mail.get_connection()
        con.open()
        print('Django connected to the SMTP server')

        if settings.EMAIL_PORT == 1025 and settings.EMAIL_HOST == "127.0.0.1":
          mail_setting = '' #models.SmtpEmailSettings.objects.last()
          host = settings.EMAIL_HOST #mail_setting.smtp_email_host
          print(host)
          host_user = ''#mail_setting.smtp_email_host_user
          host_pass = ''#mail_setting.smtp_email_host_password
          host_port = settings.EMAIL_PORT #mail_setting.smtp_email_host_port
          print(host_port)
          host_sender_email = 'ajibolaolayanju@gmail.com' #mail_setting.smtp_email_host_sender_address
          host_tls = ''#mail_setting.smtp_use_tls
          host_ssl = ''#mail_setting.smtp_use_ssl
          host_timeout = 10 #mail_setting.smtp_timeout
        else:
          mail_setting = models.SmtpEmailSettings.objects.last()
          host = mail_setting.smtp_email_host
          host_user = mail_setting.smtp_email_host_user
          host_pass = mail_setting.smtp_email_host_password
          host_port = mail_setting.smtp_email_host_port
          host_sender_email = mail_setting.smtp_email_host_sender_address
          host_tls = mail_setting.smtp_use_tls
          host_ssl = mail_setting.smtp_use_ssl
          host_timeout = mail_setting.smtp_timeout

        mail_obj = EmailBackend(
            host=host,
            port=host_port,
            password=host_pass,
            username=host_user,
            use_tls=host_tls,
            use_ssl=host_ssl,
            timeout=host_timeout
        )

        msg = mail.EmailMessage(
            subject=subject,
            body=message,
            from_email=host_sender_email,
            to=[contact_list],
            connection=con,
        )

        msg.content_subtype = "html"
        mail_obj.send_messages([msg])
        print('Message has been sent.')

        mail_obj.close()
        print('SMTP server closed')
        return True

    except Exception as _error:
        print('Error in sending mail >> {}'.format(_error))
        return False