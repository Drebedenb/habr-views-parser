# Generated by Django 5.1.7 on 2025-03-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewsData',
            fields=[
                ('url', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('datetime', models.DateTimeField()),
                ('views', models.IntegerField()),
            ],
            options={
                'db_table': 'views_data',
            },
        ),
    ]
