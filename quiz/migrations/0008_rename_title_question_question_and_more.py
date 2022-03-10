# Generated by Django 4.0.2 on 2022-03-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_rename_category_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='question',
            name='diffuculty',
            field=models.CharField(choices=[('H', 'High'), ('L', 'Low'), ('M', 'Medium')], max_length=50),
        ),
    ]
