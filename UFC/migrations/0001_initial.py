# Generated by Django 5.0.1 on 2024-01-28 16:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('country', models.CharField(choices=[('USA', 'United States'), ('CAN', 'Canada'), ('RUS', 'Russia'), ('UK', 'United Kingdom')], max_length=3)),
                ('age', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('record', models.CharField(max_length=8)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='FighterBelt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belt', models.CharField(choices=[('Master', 'Master'), ('Champ', 'Champ'), ('Grapler', 'Grapler')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FightningStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='')),
                ('mark', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(limit_value=10)])),
                ('fighter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UFC.fighter')),
            ],
        ),
        migrations.AddField(
            model_name='fighter',
            name='belt',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UFC.fighterbelt'),
        ),
    ]
