# Generated by Django 3.1.1 on 2020-11-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201108_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_images/default_profile_avatar.jpg', upload_to='profile_pics/'),
        ),
    ]
