# Generated by Django 3.0.2 on 2020-01-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0012_auto_20200116_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replay',
            new_name='reply',
        ),
    ]