# Generated by Django 2.2.5 on 2022-05-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=20)),
                ('money', models.IntegerField()),
                ('data', models.IntegerField()),
            ],
        ),
    ]