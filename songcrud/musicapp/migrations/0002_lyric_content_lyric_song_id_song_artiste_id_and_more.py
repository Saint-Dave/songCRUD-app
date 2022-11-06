# Generated by Django 4.1.3 on 2022-11-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyric',
            name='content',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lyric',
            name='song_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='date_released',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artiste',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artiste',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]