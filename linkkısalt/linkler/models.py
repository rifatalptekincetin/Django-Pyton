from django.db import models
from django.utils import timezone
import datetime

class link(models.Model):
    yayinci=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    tarih=models.DateTimeField(default=timezone.now)
    link=models.TextField()
    ad=models.CharField(max_length=64)
    aciklama=models.TextField()
    def save_path(self, filename):
        now = datetime.datetime.now()
        fn='anasayfa/static/img/link/'+str(self.id)+'.jpg'
        return fn
    resim=models.ImageField(upload_to=save_path, blank=True, null=True)
    def __str__(self):
        return self.ad
