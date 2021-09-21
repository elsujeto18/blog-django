from django.db import models

class FavoritesManagaer(models.Manager):

    def favorito_user(self, usuario):
        return self.filter(
            entry__public = True,
            user=usuario

        ).order_by('-created')

