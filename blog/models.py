from django.conf import settings 
from django.db import models 
from django.utils import timezone 

#siccome c'è scritto model.Models django capisce che è un model da scrivere nel db
class Post(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #chiave primaria legata ad altri modelli
     title = models.CharField(max_length=200) #testo con un numero limitato di lettere
     text = models.TextField() #testo senza un limite
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)

     def publish(self): 
         self.published_date = timezone.now()
         self.save()
#è il metodo pubblicare. def significa che questa è una funzione/metodo e publish è il nome del metodo

     def __str__(self):
         return self.title
    #questo metodo restituisce una stringa?

#Post è l'oggetto, con proprietà e metodi (è comunque OOP)