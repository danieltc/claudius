# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-15 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0020_auto_20171215_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='dados_demissao',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='membro',
            name='data_admissao',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='membro',
            name='data_demissao',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='membro',
            name='forma_demissao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ex_membros_demitidos', to='rol.TipoDemissao'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='transferido_para',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ex_membros_transferidos', to='rol.Igreja'),
        ),
    ]
