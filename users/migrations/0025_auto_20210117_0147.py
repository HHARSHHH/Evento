# Generated by Django 2.2.8 on 2021-01-16 20:17

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminreg',
            name='password1',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=10)),
        ),
        migrations.AlterField(
            model_name='adminreg',
            name='password2',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=10)),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password1',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=10)),
        ),
        migrations.AlterField(
            model_name='userreg',
            name='password2',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=10)),
        ),
    ]
