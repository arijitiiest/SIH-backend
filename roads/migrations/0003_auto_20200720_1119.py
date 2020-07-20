# Generated by Django 3.0.8 on 2020-07-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0002_auto_20200720_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='predictedImage',
            field=models.FileField(blank=True, upload_to='model'),
        ),
        migrations.AlterField(
            model_name='road',
            name='image',
            field=models.FileField(upload_to='user'),
        ),
    ]
