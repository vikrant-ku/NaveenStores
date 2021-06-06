from django.db import models
from django_resized import ResizedImageField


STATUS_CHOICES =(
    ("Draft", "Draft"),
    ("Posted", "Posted"),
  )

class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='Draft')
    head1 = models.CharField(max_length=100)
    body1 = models.TextField()
    head2 = models.CharField(max_length=100,  null=True, blank=True)
    body2 = models.TextField( null=True, blank=True)
    head3 = models.CharField(max_length=100,  null=True, blank=True)
    body3 = models.TextField( null=True, blank=True)
    head4 = models.CharField(max_length=100,  null=True, blank=True)
    body4 = models.TextField( null=True, blank=True)
    head5 = models.CharField(max_length=100,  null=True, blank=True)
    body5 = models.TextField( null=True, blank=True)
    head6 = models.CharField(max_length=100,  null=True, blank=True)
    body6 = models.TextField( null=True, blank=True)
    head7 = models.CharField(max_length=100,  null=True, blank=True)
    body7 = models.TextField( null=True, blank=True)
    head8 = models.CharField(max_length=100,  null=True, blank=True)
    body8 = models.TextField( null=True, blank=True)
    head9 = models.CharField(max_length=100,  null=True, blank=True)
    body9 = models.TextField( null=True, blank=True)
    head10 = models.CharField(max_length=100,  null=True, blank=True)
    body10 = models.TextField( null=True, blank=True)
    fechar_image = ResizedImageField(quality=75, upload_to='uploads/blog/')
    image1 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/')
    image2 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image3 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image4 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image5 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image6 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image7 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image8 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image9 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    image10 = ResizedImageField(size=[720, 405], quality=75, upload_to='uploads/blog/', null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

