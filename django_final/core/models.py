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
    name = models.CharField(max_length=50, verbose_name="Nombre")
    private = models.BooleanField(default=False)
    fork = models.BooleanField(default=False)
    html_url = models.URLField(verbose_name="Repo_url")
    description = models.CharField(max_length=200, verbose_name="Descripcion")
    language = models.CharField(max_length=30, verbose_name="Lenguaje")
    forks_count = models.SmallIntegerField(default=0, blank=True, verbose_name="Fork")
    created_at = models.DateTimeField(verbose_name="Fecha de Creacion")
    pushed_at = models.DateTimeField(verbose_name="Ultimo Commit")
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