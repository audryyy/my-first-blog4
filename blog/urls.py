from django.urls import path
from . import views

urlpatterns = [
    # Exemple d'une vue pour afficher tous les articles
    path('', views.all_articles, name='all_articles'),
    
    # Exemple d'une vue pour afficher un article individuel
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    
    # Ajoutez d'autres URL ici selon les besoins de votre application
]
