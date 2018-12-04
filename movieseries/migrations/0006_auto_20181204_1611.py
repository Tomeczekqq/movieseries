# Generated by Django 2.1.3 on 2018-12-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieseries', '0005_auto_20181122_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added',
            field=models.DateField(auto_now_add=True, verbose_name='Added'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, to='movieseries.Categories', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(blank=True, max_length=150, verbose_name='Director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_year',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.TextField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_translated',
            field=models.TextField(blank=True, max_length=200, verbose_name='Translated Title'),
        ),
    ]