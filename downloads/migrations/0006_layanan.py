# Generated by Django 3.2.2 on 2021-05-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0005_auto_20210508_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layanan', models.CharField(max_length=200)),
            ],
        ),
    ]