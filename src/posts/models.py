from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
# Create your models here.
class Author(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(unique=True)
	active=models.BooleanField(default=False)
	created_on=models.DateTimeField(auto_now_add=True)
	last_logged_in=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
    	return self.name

    class Meta:
    	verbose_name_plural='Categories'
    	


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
    	return reverse('posts:tag_detail',kwargs={'tag_slug':self.slug})
		

		



def upload_location(instance,filename):
	return '%s/%s' %(instance.pk,filename)

class Post(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField()
	slug=models.SlugField(unique=True)
	image=models.ImageField(upload_to=upload_location,height_field='height_field',width_field='width_field')
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	updated=models.DateTimeField(auto_now=False,auto_now_add=True)
	timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)
	draft=models.BooleanField(default=False)
	publish=models.DateField(auto_now=False,auto_now_add=False)
	author=models.ForeignKey(Author,on_delete=models.CASCADE)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	tags=models.ManyToManyField(Tag)

	def __str__(self):
		return self.title
		

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"obj_slug":self.slug})

	class Meta:
		ordering=["-timestamp","-updated"]
		

def create_slug(instance,new_slug=None):
	slug=slugify(instance.title)
	if new_slug is not None:
		slug=new_slug
	qs=Post.objects.filter(slug=slug).order_by('-id')
	exists=qs.exists()	
	if exists:
		new_slug="%s-%s" %(slug,qs.first().id)
		return create_slug(instance,new_slug=new_slug)
	return slug
	
def pre_save_post_receiver(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

pre_save.connect(pre_save_post_receiver,sender=Post)		













