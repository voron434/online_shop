from django.db import models

class Clothes(models.Model):
    FOR_WHOM_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Child'),
    )
    TYPE_CHOICES = (
        ('C', 'CLOTHING'),
        ('S', 'SHOES'),
        ('A', 'ACCESSORIES'),

        )
    name = models.CharField(max_length=30)
    type = for_whom = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='M',
    )
    for_whom = models.CharField(
        max_length=1,
        choices=FOR_WHOM_CHOICES,
        default='M',
    )
    price = models.PositiveIntegerField()
    picture = models.URLField(max_length=3000)
    description = models.TextField()
    count = models.PositiveIntegerField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User')

    def publish(self):
        self.is_published = True
        self.save()

    def __str__(self):
        return self.name

def approved_products(self):
    return self.products.filter(is_published=True)