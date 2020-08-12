# Generated by Django 3.0.8 on 2020-08-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200807_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='return_policy',
            field=models.CharField(default='No return No exchange', max_length=20),
        ),
    ]
