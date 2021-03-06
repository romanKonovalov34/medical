# Generated by Django 3.0.6 on 2020-06-01 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ancket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100, verbose_name='date form')),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_card', models.IntegerField(verbose_name='card')),
                ('FIO', models.CharField(max_length=100, verbose_name='last first middle name')),
                ('date_birth', models.CharField(max_length=100, verbose_name='birthday')),
                ('sex', models.CharField(max_length=50, verbose_name='sex')),
                ('nationality', models.CharField(max_length=50, verbose_name='nationality')),
                ('education', models.CharField(max_length=100, verbose_name='education')),
                ('address', models.CharField(max_length=100, verbose_name='adress')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('job', models.CharField(max_length=100, verbose_name='place work')),
                ('position', models.CharField(max_length=100, verbose_name='position')),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='question')),
            ],
            options={
                'verbose_name': 'question',
                'verbose_name_plural': 'qestions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200, verbose_name='login')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
                ('isAdmin', models.BooleanField(verbose_name='is admin')),
                ('FIO', models.CharField(default='', max_length=50, verbose_name='last first middle name')),
                ('Postion', models.CharField(default='', max_length=50, verbose_name='position')),
                ('Department', models.CharField(default='', max_length=50, verbose_name='department')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Epicriz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invalid', models.BooleanField(default=False)),
                ('lechenie', models.CharField(default='', max_length=500, null=True, verbose_name='Лечение')),
                ('date_gospit', models.DateField(default='1999-01-01', null=True)),
                ('date_vipisky', models.DateField(default='1999-01-01', null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Disease')),
                ('epicriz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Epicriz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.TextField()),
                ('conviction', models.IntegerField(default=0)),
                ('ancket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ancket')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Question')),
            ],
        ),
        migrations.AddField(
            model_name='ancket',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient', verbose_name='patient'),
        ),
    ]
