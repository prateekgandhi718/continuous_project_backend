# Generated by Django 4.1 on 2022-08-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_factory_created_remove_factory_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]