# Generated by Django 2.1.2 on 2019-08-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='lesson',
            field=models.IntegerField(choices=[(1, '※基礎程式設計：使用Scratch3.X')], default=2, verbose_name='課程名稱'),
        ),
    ]
