# Generated by Django 4.1.7 on 2023-06-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEurope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_title', models.CharField(max_length=50)),
                ('Country_desc', models.TextField()),
                ('Country_img', models.FileField(default=None, max_length=50, null=True, upload_to='Blog/')),
            ],
        ),
    ]
