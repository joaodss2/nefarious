# Generated by Django 2.1.5 on 2019-06-09 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nefarious', '0028_auto_20190530_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchTVSeasonRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_number', models.IntegerField()),
                ('quality_profile_custom', models.CharField(blank=True, choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-720p-1080p', 'hd-720p-1080p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd')], max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watch_tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nefarious.WatchTVShow')),
            ],
        ),
    ]