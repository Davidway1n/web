# Generated by Django 2.2.4 on 2020-03-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0091_merge_20200316_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_chat_seen',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_chat_status',
        ),
        migrations.AddField(
            model_name='profile',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, help_text='avg feedback from those who theyve done work with', max_digits=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='earnings_count',
            field=models.IntegerField(db_index=True, default=0, help_text='How many times has user earned crypto with Gitcoin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='follower_count',
            field=models.IntegerField(db_index=True, default=0, help_text='how many users follow them'),
        ),
        migrations.AddField(
            model_name='profile',
            name='following_count',
            field=models.IntegerField(db_index=True, default=0, help_text='how many users are they following'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_org',
            field=models.BooleanField(db_index=True, default=True, help_text='Is this profile an org?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='organizations_fk',
            field=models.ManyToManyField(blank=True, to='dashboard.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='spent_count',
            field=models.IntegerField(db_index=True, default=0, help_text='How many times has user spent crypto with Gitcoin'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hide_profile',
            field=models.BooleanField(db_index=True, default=True, help_text='If this option is chosen, we will remove your profile information all_together'),
        ),
    ]