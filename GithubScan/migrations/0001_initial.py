# Generated by Django 4.0.1 on 2022-03-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubResult',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(db_column='name', max_length=32, verbose_name='任务名称')),
                ('result', models.TextField(db_column='result', verbose_name='任务结果')),
                ('timestamp', models.DateField(db_column='deadline', verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '任务管理',
                'verbose_name_plural': '任务管理',
            },
        ),
        migrations.CreateModel(
            name='GithubScanTask',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(db_column='name', max_length=32, verbose_name='任务名称')),
                ('keyword', models.CharField(db_column='keyword', max_length=256, verbose_name='关键字')),
                ('domain', models.CharField(blank=True, db_column='domain', max_length=256, null=True, verbose_name='域名')),
                ('timestamp', models.DateField(db_column='deadline', verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '任务管理',
                'verbose_name_plural': '任务管理',
            },
        ),
    ]