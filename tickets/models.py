import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

def validate_file(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
       raise ValidationError(f'Max size of file is {limit_mb} MB')

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Priority(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    code = models.CharField(max_length=30, unique=True, db_index=True)
    order = models.PositiveSmallIntegerField(unique=True)
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


class Ticket(models.Model):
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, 
                                related_name='ticket_priority')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                related_name='ticket_category')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, 
                                related_name='ticket_color')
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    middle_name = models.CharField(max_length=48, null=True, blank=True)
    subject = models.CharField(max_length=150)
    description = RichTextField()
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'


class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='attachments/%Y/%m/%d', null=True,
                                    blank=True, validators=[validate_file])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ticket.subject} - {self.file.name}'

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'

