# Generated by Django 4.1.7 on 2023-03-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_scope_is_main_alter_scope_article_alter_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
