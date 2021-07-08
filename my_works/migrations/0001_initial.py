# Generated by Django 3.2.3 on 2021-05-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('main_photo', models.ImageField(upload_to='work/', verbose_name='Главное фото')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
            ],
            options={
                'verbose_name': 'Моя работа',
                'verbose_name_plural': 'Мои работы',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='WorkShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='work_shots/', verbose_name='Изображение')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_works.work', verbose_name='работа')),
            ],
            options={
                'verbose_name': 'Кадр',
                'verbose_name_plural': 'Кадры',
            },
        ),
        migrations.CreateModel(
            name='WorkFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('file', models.FileField(upload_to='work_files/', verbose_name='Файл')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_works.work', verbose_name='работа')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
