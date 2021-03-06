# Generated by Django 2.2.9 on 2020-02-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='VBP', max_length=20)),
                ('site_logo', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Site Dashboard Configuration',
                'verbose_name_plural': 'Site Dashboard Configurations',
            },
        ),
    ]
