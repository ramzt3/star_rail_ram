# Generated by Django 4.2.7 on 2024-02-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_gender_alter_rarity_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name_plural': 'gender'},
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='core.gender'),
        ),
    ]
