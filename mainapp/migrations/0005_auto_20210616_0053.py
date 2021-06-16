# Generated by Django 3.2.1 on 2021-06-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_post_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]