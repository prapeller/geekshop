# Generated by Django 3.2.7 on 2021-10-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='about me'),
        ),
    ]
