# Generated by Django 2.2.6 on 2019-10-13 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model1.Model1')),
            ],
        ),
    ]
