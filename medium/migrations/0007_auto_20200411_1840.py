# Generated by Django 3.0.5 on 2020-04-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0006_auto_20200411_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.FileField(blank=True, default='profil/circleblue.png', null=True, upload_to=''),
        ),
    ]
