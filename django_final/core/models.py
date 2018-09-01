from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(blank=False, max_length=50)
    avatar_url = models.URLField()
    html_url = models.URLField()
    tipo = (('users', 'Usuario'),('orgs', 'Organizacion'))
    _type = models.CharField(choices=tipo, max_length=5, default='users')
    total_repos = models.PositiveSmallIntegerField(default=0, editable=False)
    ultima_consulta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.login
    
    class Meta:
        ordering = ['ultima_consulta','login']
        indexes = [
            models.Index(fields=['login'])
        ]
        verbose_name = 'owner'
        verbose_name_plural = 'owners'

    

class Repos(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    private = models.BooleanField(default=False)
    fork = models.BooleanField(default=False)
    html_url = models.URLField()
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['pushed_at','created_at','name']
        indexes = [
            models.Index(fields=['owner','name'])
        ]
    verbose_name = "repository"
    verbose_name_plural = "repositories"