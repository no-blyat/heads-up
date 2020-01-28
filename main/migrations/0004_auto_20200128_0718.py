# Generated by Django 3.0.1 on 2020-01-28 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20200128_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='id',
        ),
        migrations.AlterField(
            model_name='check',
            name='url',
            field=models.URLField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinputs',
            name='email_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Check')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
