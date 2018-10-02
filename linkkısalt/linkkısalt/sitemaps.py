from django.contrib.sitemaps import Sitemap
from linkler.models import link

class linksitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return link.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return '/'
