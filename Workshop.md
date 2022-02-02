# Workshop Django : Créer son un réseau social avec Django


## Introduction

Django est un framework web en Python qui existe depuis 2005.
Ce dernier a été et est toujours très utilisé car on peut rapidement developper quelque chose de fonctionnel et avec quelques heures de travail en plus arriver vers un site web parfait.

Django est un framework plutôt orienté server (Back End) et peut-être utilisé nottament pour la création d'API REST et autres


## Étape 1 : Prérequis

Django est un framework Python, il faut donc commencer par installer [Python](https://www.python.org/), si ce n'est pas déjà fait

Pour vérifier si ça a fonctionné tape : `python3 --version` sur ton terminal

Ensuite, nous allons utiliser le **Package Manager** de Python nommé _"pip"_ pour installer ce dont nous avons besoin.

À savoir **Django** : `python3 -m pip install Django`

Pour vérifier si ça a fonctionné : `python3 -m django --version`

## Étape 2 : Démarrer le projet Django

_N.B. : `<___>` signifie que c'est à toi de choisir la variable_

Pour démarrer le projet fait : `django-admin startproject <le-nom-de-ton-projet>`

Suite à ça tu devrais te retrouver avec cette arborescence de fichier :
```
<le-nom-de-ton-projet>/
    manage.py
    <le-nom-de-ton-projet>/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
Voici en très gros à quoi servent les fichiers :

* `manage.py` : Notre interface en ligne de commande qui va nous permettre d'interagir avec ce projet Django.
* `__init__.py` : Un fichier vide qui indique à Python que ce répertoire doit être considéré comme un package Python.
* `settings.py` : Ce fichier contient tous les paramètres de fonctionnement de votre application
* `mysite/urls.py` : Ce fichier contient les déclarations d'URL pour ce projet Django
* `asgi.py` et `wsgi.py` : Ces fichiers ne les calcule pas (c'est pour le déploiement en très gros).

Maintenant que tout est créé, déplace-toi dans le dossier et lance le serveur :

`python3 manage.py runserver`

ou

`python3 manage.py runserver <un-port-specifique>`

Normalement tu devrais avoir quelque chose comme ça :

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

January 17, 2022 - 15:50:53
Django version 4.0, using settings '<le-nom-de-ton-projet>.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Clique maintenant [ici](http://127.0.0.1:8000/) pour ouvrir ton projet !

Voici ce que tu devrais obtenir :

![Rendu du seveur!](https://files.realpython.com/media/Screenshot_2018-12-09_at_17.58.16.20be0c5d3f1e.png)

### Dernières vérifications

Créons deux sous-applications liées à notre projet.
En effet, avec Django ton projet peut-être composé de plusieurs applications, les tiennes comme celles partagées sur Internet.

Nous allons créer nos deux applications que nous allons appeler _posts_ et _users_ :

`python3 manage.py startapp posts`
`python3 manage.pu startapp users`

* Dans `settings.py` du dossier `<le-nom-de-ton-projet>`, abrite la liste globale `INSTALLED_APPS`. En plus des autres,
* ajoute les strings `"posts"` et `"users"`.

* Dans `settings.py` du dossier `<le-nom-de-ton-projet>`, il y'a une variable `ALLOWED_HOST` qui est une liste vide.
  Ajoutons `"*"` comme seul élément de cette liste : ça permettra à localhost (toi) de pouvoir développer tranquillement.

## Étape 3 : Création de notre première vue

Voici l'arborescence de nos deux applications :

```
posts/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
users/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Comme tu l'auras compris, une application sera dédiée aux utilisateurs, le profile, et l'autre plus spécifiquement
au fil d'actualité, aux posts, commentaires, etc.

Tu remarqueras qu'il apparaît maintenant à l'intérieur de chacun des applications un fichier nommé `views.py`.
C'est à l'intérieur de celle-ci que nous ajouterons nos vues.


Éditons celui du dossier `posts/` ainsi :

```python
from django.http import HttpResponse


def ma_vue(request):
    return HttpResponse("Oh pète sa mère ! Ma vue marche !")
```

Maintenant que la vue a été créée il faut maintenant la connecter à une URL.

Créons un fichier `urls.py` à l'intérieur du dossier `posts` et dedans ajoute ça :

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
]
```

_Le premier paramètre de la fonction `path()` sert à définir la route. Laisser des guillements vides (`path('')`) équivaut à la route `/`_

Bien ! L'URL existe dans les routes de l'application `posts` mais pas dans les routes du projet. Il nous reste donc une dernière chose à faire cette fois-ci dans le `urls.py` à l'intérieur du dossier `<le-nom-de-ton-projet>` :

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
]
```

Maintenant, il est temps de voir cette vue de nos propres yeux.

Relance le serveur et si tout s'affiche alors tu peux continuer !

## Etape 4 : Posts et commentaires

Comme vous pouvez le voir, les dossiers `templates.zip` `static.zip` et `templatetags.zip` vous sont fournis.
Ceux-ci font partie du frontend pour vous faciliter l'apprentissage. Il faut les unzipper et les déplacer dans l'application
_posts_. 

```bash
unzip templates.zip ; mv templates/ <le-nom-de-ton-projet>/posts
unzip static.zip ; mv static/ <le-nom-de-ton-projet>/posts
unzip templatetags.zip ; mv templatetags/ <le-nom-de-ton-projet>/posts
```

### 4.1 Modèles

Dans `models.py`, nous allons définir les modèles `Post` et `Comment` qui seront créés par nos utilisateurs.

- [ ] Créer le modèle `Post` avec les fields suivants : 
  - [ ] `content`, qui est un `TextField` avec `max_length=512`

- [ ] Créer le modèle `Comment` avec les fields suivants :
  - [ ] `comment_content` qui est un `TextField` avec `max_length=512`
  - [ ] `post_parent` qui est une relation de base de donnée ForeignKey liée à l'objet `Post`.

:warning: Attention, merci de garder les mêmes noms de variables car celles-ci sont utilisées dans le front.

> :bulb: En savoir plus sur les [relations dans les bases de données](https://docs.djangoproject.com/fr/4.0/topics/db/examples/)

### Petite astuce pour vérifier
Django nous met à disposition un shell où l'on peut ajouter des éléments, les lires, tout ça en python sans passer par du langage SQL !
```python
python3 manage.py shell
>>> from models import Post, Comment
>>> Post.objets.all() # Devrait afficher tous les posts présents dans la DB, pareil pour Comment
>>> p = Post(content="lol")
>>> p.save()
```

### 4.2 Vues

Maintenant, il s'agirait de pouvoir créer à travers le site nos objets `Post` et `Comment`.
Voici la démarche à suivre.

- [ ] Créer un fichier `forms.py` dans le même dossier que `views.py`.
- [ ] Rédiger les forms : `PostCreationForm` et `CommentCreationForm` dans `forms.py`
- [ ] Et enfin, rédiger les vues `Feed`, `create_comment` et `upload_post` dans `views.py`, avec la signature suivante :
```python

class FeedView(ListView):
  template_name = "post/feed.html"
  ... # TODO

  def get_queryset(self):
    ... # TODO


def create_post(request):
  if request.method == 'POST':
    ... # TODO
  elif request.method == "GET":
    return render(request, "post/upload_post.html", {"post_form": PostCreationForm})


def create_comment(request, pk):
  if request.method == "POST":
    form = ... # TODO
    if form.is_valid():
      return redirect('/')
    else:
      messages.error(request, "An error has occurred. Please submit your comment again.")
  elif request.method == "GET":
    return render(request, "post/post_detail.html", {"post": Post.objects.get(pk=pk),
                                                     "comments": Comments.objects.filter(parent_post_id=pk),
                                                     "comment_form": CommentCreationForm})
```

:warning: Merci de garder le même contexte dans les retours de fonction, car c'est ce qui est utilisé dans le front.

Et enfin, créer le fichier `posts/urls.py` et y ajouter nos vues de la sorte :
```python
from django.urls import path
from. import views

urlpatterns = [
  path('', views.FeedView.as_view(), name="/"),
  path('upload_post/', views.create_post, name="upload_post"),
  path('posts/<int:pk>/', views.create_comment, name="create-comment-view")
]
```

*Besoin d'aide ?*
- [Les modèles en Django](https://docs.djangoproject.com/fr/4.0/topics/db/models/)
- [Les forms en Django](https://docs.djangoproject.com/fr/4.0/topics/forms/)

## Etape 5 : Les utilisateurs et les profiles