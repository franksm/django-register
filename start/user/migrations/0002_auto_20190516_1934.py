# Generated by Django 2.2 on 2019-05-16 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'permissions': (('can_view', 'Can see doctor'), ('can_add', 'Can add doctor'), ('can_edit', 'Can edit doctor'), ('can_delete', 'can delete doctor'))},
        ),
    ]