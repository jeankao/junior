# Generated by Django 2.1.2 on 2019-05-21 11:26

from django.db import migrations, models
import django.utils.timezone
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='班級名稱')),
                ('lesson', models.IntegerField(choices=[(0, '數位學習：SPOC線上課程'), (1, '程式設計輕鬆學：使用Scratch3.X'), (2, '※基礎程式設計：使用Scratch3.X')], default=2, verbose_name='課程名稱')),
                ('password', models.CharField(max_length=30, verbose_name='選課密碼')),
                ('teacher_id', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=0)),
                ('group_show_open', models.BooleanField(default=False)),
                ('group_show_size', models.IntegerField(default=2)),
                ('progress', models.IntegerField(choices=[(0, '個人'), (1, '小組')], default=1, verbose_name='學生進度')),
                ('online', models.BooleanField(choices=[(False, '關閉課程'), (True, '開放修課')], default=True, verbose_name='課程狀態')),
            ],
        ),
        migrations.CreateModel(
            name='ClassroomGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('numbers', models.IntegerField(default=6)),
                ('opening', models.BooleanField(default=True)),
                ('assign', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='測驗主題')),
                ('user_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('domains', models.TextField(default='')),
                ('levels', models.TextField(default='')),
                ('opening', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExamClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.BooleanField(default=False)),
                ('deadline_date', models.DateTimeField(default=teacher.models.get_deadline)),
                ('round_limit', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ExamImportQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('option1', models.CharField(blank=True, max_length=250, null=True)),
                ('option2', models.CharField(blank=True, max_length=250, null=True)),
                ('option3', models.CharField(blank=True, max_length=250, null=True)),
                ('option4', models.CharField(blank=True, max_length=250, null=True)),
                ('answer', models.TextField(default='')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField(default=0)),
                ('types', models.IntegerField(default=0)),
                ('title', models.TextField(default='')),
                ('title_pic', models.FileField(blank=True, null=True, upload_to='')),
                ('title_filename', models.CharField(blank=True, max_length=60, null=True)),
                ('option1', models.CharField(blank=True, max_length=250, null=True)),
                ('option2', models.CharField(blank=True, max_length=250, null=True)),
                ('option3', models.CharField(blank=True, max_length=250, null=True)),
                ('option4', models.CharField(blank=True, max_length=250, null=True)),
                ('answer', models.TextField(default='')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.BooleanField(default=False)),
                ('deadline_date', models.DateTimeField(default=teacher.models.get_deadline)),
            ],
        ),
        migrations.CreateModel(
            name='FContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(default=0)),
                ('types', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('memo', models.TextField(default='')),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube_length', models.IntegerField(default=0)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('filename', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='討論主題')),
                ('teacher_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpeculationAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(default=0)),
                ('kind', models.CharField(blank=True, max_length=250, null=True)),
                ('color', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeculationClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.BooleanField(default=False)),
                ('deadline_date', models.DateTimeField(default=teacher.models.get_deadline)),
                ('group', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SpeculationContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_id', models.IntegerField(default=0)),
                ('types', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('memo', models.TextField(default='')),
                ('text', models.TextField(default='')),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('filename', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeculationWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='思辨主題')),
                ('teacher_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('domains', models.TextField(default='')),
                ('levels', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='TeamClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=0)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.BooleanField(default=False)),
                ('deadline_date', models.DateTimeField(default=teacher.models.get_deadline)),
            ],
        ),
        migrations.CreateModel(
            name='TeamContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField(default=0)),
                ('types', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('memo', models.TextField(default='')),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('filename', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='任務主題')),
                ('teacher_id', models.IntegerField(default=0)),
                ('classroom_id', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('domains', models.TextField(default='')),
                ('levels', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='TWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('classroom_id', models.IntegerField(default=0)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teamclass',
            unique_together={('team_id', 'classroom_id')},
        ),
        migrations.AlterUniqueTogether(
            name='examclass',
            unique_together={('exam_id', 'classroom_id')},
        ),
    ]
