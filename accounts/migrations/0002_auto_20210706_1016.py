# Generated by Django 3.0.5 on 2021-07-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Outoor', 'Outoor'), ('Anywhere', 'Anywhere'), ('Indoor', 'Indoor')], max_length=100),
        ),
    ]
