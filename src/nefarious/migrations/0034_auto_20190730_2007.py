# Generated by Django 2.1.5 on 2019-07-30 20:07

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0033_auto_20190730_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nefarioussettings',
            name='keyword_filters',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}, null=True),
        ),
    ]