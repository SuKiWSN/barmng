# Generated by Django 2.2.5 on 2022-05-20 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0002_recharge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recharge',
            old_name='data',
            new_name='date',
        ),
    ]
