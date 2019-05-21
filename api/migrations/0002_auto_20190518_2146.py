# Generated by Django 2.2.1 on 2019-05-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='age_group',
            field=models.CharField(choices=[('children', 'Children'), ('middle-grade', 'Middle Grade'), ('young-adult', 'Young Adult'), ('adult', 'Adult')], default='adult', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('comics', 'Comics'), ('contemporary-fiction', 'Contemporary Fiction'), ('fantasy', 'Fantasy'), ('fiction', 'Fiction'), ('horror', 'Horror'), ('humor', 'Humor'), ('manga', 'Manga'), ('memoir', 'Memoir'), ('mystery', 'Mystery'), ('reference', 'Reference'), ('science-fiction', 'Science Fiction'), ('theology', 'Theology')], default='fiction', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='series_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
