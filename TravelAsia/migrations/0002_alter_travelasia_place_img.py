# Generated by Django 4.1.7 on 2023-06-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelAsia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelasia',
            name='Place_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='Blog/'),
        ),
    ]
