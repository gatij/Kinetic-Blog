from django.contrib import admin

# Register your models here.
from posts.models import Post,Author,Category,Tag

class PostModelAdmin(admin.ModelAdmin):
	list_display=["title","updated","timestamp"]
	list_display_links=["updated"]
	list_editable=["title"]
	list_filter=["updated","timestamp"]
	search_fields=["title","content"]
	readonly_fields=['slug']
	class Meta:
		model=Post

class AuthorModelAdmin(admin.ModelAdmin):

	
	class Meta:
		model=Author

class CategoryModelAdmin(admin.ModelAdmin):


	class Meta:
		model=Category

class TagModelAdmin(admin.ModelAdmin):

	class Meta:
		model=Tag



admin.site.register(Post,PostModelAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)