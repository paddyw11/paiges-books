# Generated by Django 3.2.25 on 2024-05-16 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_description', models.TextField()),
                ('number_of_pages', models.IntegerField()),
                ('release_date', models.DateField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('offer', models.BooleanField(default=False)),
                ('genre_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.genre')),
            ],
        ),
    ]
