# Generated by Django 4.0 on 2022-02-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_field_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('sub_headline', models.CharField(blank=True, max_length=200, null=True)),
                ('main_image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='recommended')),
                ('go', models.URLField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='field_name',
            new_name='live',
        ),
        migrations.AddField(
            model_name='post',
            name='recommend',
            field=models.ManyToManyField(null=True, to='home.Recommended'),
        ),
    ]
