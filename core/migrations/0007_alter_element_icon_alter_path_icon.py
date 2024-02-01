# Generated by Django 4.2.7 on 2024-02-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_element_icon_path_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/icons/elements/'),
        ),
        migrations.AlterField(
            model_name='path',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/icons/paths/'),
        ),
    ]