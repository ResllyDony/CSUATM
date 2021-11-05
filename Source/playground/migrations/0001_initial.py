# Generated by Django 3.2.9 on 2021-11-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.IntegerField(max_length=10)),
                ('account_num', models.IntegerField(max_length=10)),
                ('pin', models.IntegerField(max_length=10)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('card_status', models.CharField(max_length=10)),
            ],
        ),
    ]