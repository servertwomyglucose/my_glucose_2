# Generated by Django 4.1.1 on 2023-02-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_alter_predictiondata_dpf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictiondata',
            name='defaultparentAgeDiabetes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='predictiondata',
            name='parentAgeDiabetes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
