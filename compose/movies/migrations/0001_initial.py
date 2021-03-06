# Generated by Django 3.1.6 on 2021-02-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('year', models.CharField(blank=True, max_length=9, null=True, verbose_name='Release date')),
                ('imdb_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='IMDB id')),
                ('kind', models.CharField(blank=True, max_length=50, null=True, verbose_name='Type')),
                ('poster_url', models.URLField(blank=True, null=True, verbose_name='Poster url')),
            ],
        ),
    ]
