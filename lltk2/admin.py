from imports import *
from models import Post

# -------------------
# Admin interface
# -------------------

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


route('admin/', admin.site.urls)
