# Generated by Django 4.1.7 on 2023-03-09 16:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_rename_reserve_id_reserve_reserve_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='head',
        ),
        migrations.AddField(
            model_name='reviews',
            name='book',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Main.book'),
            preserve_default=False,
        ),
    ]
