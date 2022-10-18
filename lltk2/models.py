from imports import *
# -------------------
# Models
# -------------------

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = get_app_label()
        ordering = ('-create_date',)