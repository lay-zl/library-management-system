# Generated by Django 3.2.12 on 2022-11-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_issuebook_rdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='idate',
            field=models.DateField(auto_now=True),
        ),
    ]
