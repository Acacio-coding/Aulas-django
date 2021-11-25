# Generated by Django 2.2.24 on 2021-11-25 23:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('identifier', models.CharField(max_length=100)),
                ('account', models.DecimalField(decimal_places=2, max_digits=6)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Client')),
            ],
        ),
    ]