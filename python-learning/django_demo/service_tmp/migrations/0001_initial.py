# Generated by Django 2.1.7 on 2019-03-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('user', models.CharField(max_length=12)),
                ('passwd', models.CharField(max_length=12)),
            ],
        ),
    ]