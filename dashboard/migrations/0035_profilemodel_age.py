# Generated by Django 4.1.1 on 2023-02-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_alter_profilemodel_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]