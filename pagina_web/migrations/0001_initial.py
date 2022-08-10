# Generated by Django 4.0.6 on 2022-08-10 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=240)),
                ('descricao', models.CharField(max_length=500)),
                ('capa', models.URLField(blank=True, max_length=1024, null=True)),
                ('data_atual', models.DateField(auto_now=True)),
                ('link_noticia', models.URLField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('texto', models.CharField(blank=True, max_length=240)),
                ('is_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='pagina_web.posts')),
                ('is_retweet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retweets', to='pagina_web.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='pagina_web.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
