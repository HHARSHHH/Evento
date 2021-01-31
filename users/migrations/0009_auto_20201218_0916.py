# Generated by Django 3.0.5 on 2020-12-18 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201218_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='branch',
            field=models.CharField(blank=True, choices=[('CSE', 'Computer Science'), ('ISE', 'Information Science'), ('ECE', 'Electronics')], default='', max_length=3, verbose_name='subject'),
        ),
    ]