# Generated by Django 4.1.7 on 2023-06-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TravelAustralia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_name', models.CharField(max_length=50)),
                ('Place_desc', models.TextField()),
                ('Place_img', models.FileField(default=None, max_length=250, null=True, upload_to='Blog/')),
            ],
        ),
    ]
