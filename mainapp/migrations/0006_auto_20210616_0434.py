# Generated by Django 3.2.1 on 2021-06-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210616_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]