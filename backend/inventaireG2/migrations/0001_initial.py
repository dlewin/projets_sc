# Generated by Django 4.2.7 on 2024-12-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yuze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_yuze', models.CharField(max_length=100, unique=True)),
                ('lieu', models.CharField(choices=[('Bungalow', 'Bungalow'), ('Zone de tests', 'Zone de tests'), ('Prestataire', 'Prestataire'), ('Inconnu', 'Inconnu')], max_length=20)),
                ('etat', models.CharField(choices=[('Neuf', 'Neuf'), ('En test', 'En test'), ('En maintenance', 'En maintenance'), ('Défectueux', 'Défectueux'), ('NC', 'NC')], max_length=20)),
                ('version_sw', models.CharField(max_length=20)),
                ('environnement', models.CharField(choices=[('QA', 'QA'), ('Prod', 'Prod'), ('Dev', 'Dev'), ('Tests', 'Tests'), ('NC', 'NC')], max_length=10)),
                ('version_hw', models.CharField(max_length=10)),
                ('config_hw', models.CharField(choices=[('CM3+', 'CM3+'), ('CM4S', 'CM4S')], max_length=10)),
                ('flashe', models.BooleanField()),
                ('commentaire', models.TextField(blank=True)),
            ],
        ),
    ]
