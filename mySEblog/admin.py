from django.contrib import admin
from mySEblog.models import Post
from reviews.models import Review
from django.contrib.admin.sites import AdminSite
from members.models import Profile

class CustomAdminSite(AdminSite):
    admin.site.site_header = "My Blog Administration"
    admin.site.site_title = "Blog Admin"
    admin.site.index_title = "Welcome to the Blog Admin Panel"
    def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = ['/static/admin/css/custom_admin.css']
        context['extra_js'] = ['/static/admin/js/custom_admin.js']
        return context

custom_admin_site = CustomAdminSite(name='custom_admin')
# Admin Customization for Post
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # Number of empty inline forms

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')  # Fields shown in the admin list view
    list_filter = ('author',)  # Add filtering options
    search_fields = ('title', 'body')  # Add search functionality
    inlines = [ReviewInline]  # Display reviews inline in Post admin

# Admin Customization for Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('post', 'rating', 'created_by', 'created_on')
    list_filter = ('rating', 'created_on')
    search_fields = ('comment',)
