# Generated by Django 3.2.12 on 2022-11-22 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_issuebook_rdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebook',
            name='rdate',
        ),
    ]
