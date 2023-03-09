# Generated by Django 4.1.7 on 2023-03-09 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publicationdate', models.DateField()),
                ('bookdescription', models.CharField(max_length=200)),
                ('checkout', models.BooleanField()),
                ('checkedoutuser', models.CharField(default='none', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=256)),
                ('body', models.TextField(max_length=1000)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='Main.book')),
            ],
        ),
    ]
