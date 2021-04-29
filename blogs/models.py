from djongo import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class MetaData(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        abstract = True

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Post(models.Model):
    blog = models.EmbeddedField(model_container=Blog)
    meta_data = models.EmbeddedField(model_container=MetaData)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors = models.ArrayField(model_container=Author)
    n_comments = models.IntegerField()
    objects = models.DjongoManager()


    def __str__(self):
        return self.headline