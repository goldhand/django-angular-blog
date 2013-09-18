from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    owner = models.ForeignKey('auth.user', related_name='posts')
    categories = models.ManyToManyField("Category",
                                        verbose_name=_("Categories"),
                                        blank=True, related_name="posts")
    related_posts = models.ManyToManyField("self",
                                 verbose_name=_("Related posts"), blank=True)

    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def get_display_url(self):
        return '/#/posts/%d' % self.pk


class Category(models.Model):
    """
    A category for grouping blog posts into a series.
    """
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("title",)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})

