# Generated by Django 5.0.3 on 2024-03-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('buy_price', models.FloatField(max_length=100000)),
                ('sell_price', models.FloatField(max_length=100000)),
                ('img_link', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]