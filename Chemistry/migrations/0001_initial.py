# Generated by Django 4.1.7 on 2023-06-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemistry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic_name', models.CharField(max_length=50)),
                ('Topic_desc', models.TextField()),
                ('Topic_img', models.FileField(default=None, max_length=250, null=True, upload_to='Blog/')),
            ],
        ),
    ]