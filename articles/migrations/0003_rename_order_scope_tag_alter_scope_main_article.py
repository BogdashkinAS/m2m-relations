# Generated by Django 4.1.7 on 2023-03-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='order',
            new_name='tag',
        ),
        migrations.AlterField(
            model_name='scope',
            name='main_article',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]
