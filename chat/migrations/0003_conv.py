# Generated by Django 3.1.1 on 2020-11-10 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_delete_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conv', models.TextField()),
                ('user', models.CharField(max_length=20)),
            ],
        ),
    ]
