# Generated by Django 3.2.3 on 2021-05-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arch_works', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='architecture',
            options={'ordering': ['-pk'], 'verbose_name': 'Архитектурный шедевр', 'verbose_name_plural': 'Архитектурные шедевры'},
        ),
        migrations.AddField(
            model_name='style',
            name='image',
            field=models.ImageField(default='architecture_styles_images/default.jpg', upload_to='architecture_styles_images/', verbose_name='Изображение'),
        ),
    ]
