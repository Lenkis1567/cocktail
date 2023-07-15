# Generated by Django 4.2 on 2023-04-28 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idIngredient', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('alcohol', models.BooleanField(default=False)),
                ('abv', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ownbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('ingradient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cockteil.ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cockteil.ingredientstype'),
        ),
    ]
