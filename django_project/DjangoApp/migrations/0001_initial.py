# Generated by Django 4.0.3 on 2022-03-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock_available', models.IntegerField()),
                ('date_ordered', models.DateField()),
            ],
        ),
    ]
