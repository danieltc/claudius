# Generated by Django 2.0 on 2018-03-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0038_auto_20180313_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipogrupo',
            options={'ordering': ['nome']},
        ),
        migrations.AlterField(
            model_name='turmafrequencia',
            name='lideranca',
            field=models.ManyToManyField(related_name='turmas_lider', to='rol.Pessoa'),
        ),
        migrations.AlterField(
            model_name='turmafrequencia',
            name='participantes',
            field=models.ManyToManyField(related_name='turmas_membro', to='rol.Pessoa'),
        ),
    ]
