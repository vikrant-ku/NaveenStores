# Generated by Django 3.1.2 on 2020-11-25 07:32

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Posted', 'Posted')], default='Draft', max_length=7)),
                ('head1', models.CharField(max_length=100)),
                ('body1', models.TextField()),
                ('head2', models.CharField(blank=True, max_length=100, null=True)),
                ('body2', models.TextField(blank=True, null=True)),
                ('head3', models.CharField(blank=True, max_length=100, null=True)),
                ('body3', models.TextField(blank=True, null=True)),
                ('head4', models.CharField(blank=True, max_length=100, null=True)),
                ('body4', models.TextField(blank=True, null=True)),
                ('head5', models.CharField(blank=True, max_length=100, null=True)),
                ('body5', models.TextField(blank=True, null=True)),
                ('head6', models.CharField(blank=True, max_length=100, null=True)),
                ('body6', models.TextField(blank=True, null=True)),
                ('head7', models.CharField(blank=True, max_length=100, null=True)),
                ('body7', models.TextField(blank=True, null=True)),
                ('head8', models.CharField(blank=True, max_length=100, null=True)),
                ('body8', models.TextField(blank=True, null=True)),
                ('head9', models.CharField(blank=True, max_length=100, null=True)),
                ('body9', models.TextField(blank=True, null=True)),
                ('head10', models.CharField(blank=True, max_length=100, null=True)),
                ('body10', models.TextField(blank=True, null=True)),
                ('fechar_image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[1920, 1080], upload_to='uploads/blog/')),
                ('image1', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image5', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image6', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image7', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image8', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image9', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('image10', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, size=[720, 405], upload_to='uploads/blog/')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
