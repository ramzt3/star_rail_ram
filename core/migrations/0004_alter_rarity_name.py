# Generated by Django 4.2.7 on 2024-02-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_star_rarity_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rarity',
            name='name',
            field=models.CharField(max_length=1),
        ),
    ]
