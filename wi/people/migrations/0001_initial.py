# Generated by Django 2.1.2 on 2018-10-28 18:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('BACHILLER', (('primero', 'Primero'), ('segundo', 'Segundo'))), ('ESO', (('tercero', 'Tercero'), ('cuarto', 'Cuarto')))], max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('active_user', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('junior', 'Junior'), ('senior', 'Senior')], max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('active_user', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Teacher'),
        ),
    ]
