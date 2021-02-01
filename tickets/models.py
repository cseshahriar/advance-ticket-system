from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Priority(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'priority'
        verbose_name_plural = 'priorities'

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, 
                                blank=True, editable=False, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ticket_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Color(models.Model):
    """ ticket color """
    name = models.CharField(max_length=50, unique=True, db_index=True)
    code = models.CharField(max_length=50, unique=True, db_index=True)
    hex_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'