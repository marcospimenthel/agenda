# Generated by Django 5.0.2 on 2024-02-23 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='categoty',
            new_name='category',
        ),
    ]
