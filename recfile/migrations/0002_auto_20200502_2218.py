# Generated by Django 3.0.5 on 2020-05-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recfile',
            name='prog_channel',
            field=models.CharField(blank=True, max_length=30, verbose_name='放送局'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_desc',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_hastag',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitterハッシュタグ'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_id',
            field=models.CharField(blank=True, max_length=100, verbose_name='Radiko番組ID'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_img',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='画像URL'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_info',
            field=models.TextField(blank=True, null=True, verbose_name='information'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_pfm',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='パーソナリティ'),
        ),
        migrations.AlterField(
            model_name='recfile',
            name='prog_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='番組URL'),
        ),
    ]
