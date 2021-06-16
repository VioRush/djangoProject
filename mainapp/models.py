from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ('prywatny', 'Prywatny'),
        ('publiczny', 'Publiczny'),
    )
    title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=250,
    #                       unique_for_date='publish', default=title)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publiczny')

    def get_absolute_url(self):
        return reverse('mainapp:post_detail',
                       args=[self.id])

    class Meta:
        ordering = ('-publish',)  # nowe posty wyświetlają się jako pierwsze

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_CHOICES = (
        ('prywatny', 'Prywatny'),
        ('publiczny', 'Publiczny'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publiczny')

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagies')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.image

# Create your models here.
