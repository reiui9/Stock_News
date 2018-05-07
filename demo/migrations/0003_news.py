# Generated by Django 2.0.4 on 2018-05-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20180208_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200)),
                ('pubDate', models.DateTimeField(blank=True, null=True)),
                ('saveDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]