# Generated by Django 4.1.2 on 2022-11-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_db', '0007_currency_familymembers_section_alter_budget_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='members',
            field=models.CharField(max_length=100),
        ),
    ]