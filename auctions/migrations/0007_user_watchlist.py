# Generated by Django 2.0 on 2020-10-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_watchlist_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='auctions.Listing'),
        ),
    ]
