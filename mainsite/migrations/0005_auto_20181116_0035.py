# Generated by Django 2.0.4 on 2018-11-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20181116_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(choices=[('red', 'red'), ('green', 'green'), ('light-green', 'light-green'), ('blue', 'blue'), ('light-blue', 'light-blue'), ('brown', 'brown'), ('tan', 'tan'), ('white', 'white'), ('cream', 'cream'), ('orange', 'orange'), ('purple', 'purple'), ('mixed', 'mixed')], max_length=40),
        ),
        migrations.AlterField(
            model_name='product_type',
            name='name',
            field=models.CharField(choices=[('cinnamon roll votive', 'cinnamon roll votive'), ('cinnamon roll', 'cinnamon roll'), ('cinnamon roll with burn dish', 'cinnamon roll with burn dish'), ('full pie', 'full pie'), ('pie slice', 'pie slice'), ('candle in jar', 'candle in jar'), ('candle melts', 'candle melts')], max_length=60),
        ),
    ]
