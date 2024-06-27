from django.db.models import Manager
from django.utils.timezone import now


class PostManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related(
                'author', 'category', 'location',)
