# Generated by Django 4.0.3 on 2022-03-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro1', '0002_recipe_ingridients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=25),
        ),
    ]
