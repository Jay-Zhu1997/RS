# Generated by Django 2.2 on 2019-04-29 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
                ('L', models.CharField(max_length=1000)),
                ('S', models.CharField(max_length=1000)),
            ],
        ),
    ]
