# Generated by Django 4.0.2 on 2022-04-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_image_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_header',
            field=models.URLField(default='https://pbs.twimg.com/profile_banners/1371184742578720768/1647118044/1500x500'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]