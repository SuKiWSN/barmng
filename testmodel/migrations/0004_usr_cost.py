# Generated by Django 2.2.5 on 2022-05-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0003_auto_20220520_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='usr_cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=20)),
                ('cost', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
        ),
    ]
