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

## Étape 3 : Création de notre première vue

Avant de s'attaquer à la création de la vue nous allons d'abord la mettre dans une application.

En effet, avec Django ton projet peut-être composé de plusieurs applications, les tiennes comme celles partagées sur Internet.

Nous allons créer notre application et l'appeler _news_ :

`python manage.py startapp news`

Voici son arborescence :

```
news/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Tu remarqueras qu'il apparaît maintenant à l'intérieur un fichier nommé `views.py`. C'est à l'intérieur de celle-ci que nous ajouterons nos vues.

Éditons le ainsi :

```python
from django.http import HttpResponse


def ma_vue(request):
    return HttpResponse("Oh pète sa mère ! Ma vue marche !")
```

Maintenant que la vue a été créée il faut maintenant la connecter à une URL.

Créons un fichier `urls.py` à l'intérieur du dossier `news` et dedans ajoute ça :

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
]
```

_Le premier paramètre de la fonction `path()` sert à définir la route. Laisser des guillements vides (`path('')`) équivaut à la route `/`_

Bien ! L'URL existe dans les routes de l'application `news` mais pas dans les routes du projet. Il nous reste donc une dernière chose à faire cette fois-ci dans le `urls.py` à l'intérieur du dossier `<le-nom-de-ton-projet>` :

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

## Etape 4 : Pages de connexion

Il se trouve que Django nous donne d'office un modèle de `User`. Et comme nous avons besoin d'un profile `User`
pour se connecter, créer des posts, en liker, en commenter, c'est pile ce qu'il nous faut !

Il ne nous reste plus qu'à créer les vues `login` et `register`. Dans `views.py`, écris :

```python
def login(request):
    if request.method == "POST":
        # Check credentials from form and log in
        ...
    elif request.method == "GET":
        # return form
        ...


def register(request):
    if request.method == "POST":
        # Create User, and log in
        ...
    elif request.method == "GET":
        # return form
        ...
```

> :bulb: Plus d'informations sur les requêtes `GET` et `POST` [ici](https://lazaroibanez.com/difference-between-the-http-requests-post-and-get-3b4ed40164c1)

Les commentaires mentionnent un `form`. En effet, pour se connecter ou créer un compte, il faut remplir des champs utilisateurs. 
Django nous donne accès à deux forms pour faire cela : `AuthenticationForm` et `UserCreationForm`.

- [ ] Compléter la vue login
- [ ] Compléter la vue register

N'oublie pas d'appliquer `python3 manage.py makemigrations` et `python3 manage.py migrate` pour enregistrer tes utilisateurs
de test dans la base de donnée !

> :bulb: Si tu galères trop, va jeter un oeil à [ce tutoriel](https://www.askpython.com/django/django-user-authentication)

## Etape 5 - Création de Posts et de commentaires

Maintenant que notre utilisateur peut se créer un compte et se connecter, il serait temps qu'il puisse créer un post!
Ces posts doivent être ensuite enregistrés dans la base de données, comme nos `User`.
Django ne contient pas de builtin `Post` malheureusement, nous allons devoir le faire nous-mêmes.

- [ ] Créer le modèle `Post` dans `models.py` avec les fields suivants:
    - Author : User, relation One to Many
    - Content : TextField, le contenu écrit du post
    - Likes: User, relation Many to Many
- [ ] Créer le modèle `Comment` dans `models.py` avec les fields suivants:
    - Author : User, relation One to Many
    - Content, Text Field, contenu du commentaire
    - Likes: User, relation Many to Many
    - Post_parent: Post, relation One to Many
- [ ] Créer un fichier `forms.py` dans le même dossier que `views.py`.
- [ ] Rédiger les forms : `PostCreationForm` et `CommentCreationForm` dans `forms.py`
- [ ] Et enfin, rédiger les vues `create_post` et `comment` dans `views.py`. Attention, n'oublie pas de faire attention 
à ce que l'utilisateur soit bien connecté avant d'effectuer une telle action !

### Petite astuce pour vérifier
Django nous met à disposition un shell où l'on peut ajouter des éléments, les lires, tout ça en python sans passer par du langage SQL !
```python
python3 manage.py shell
>>> from models import Post, Comment
>>> Post.objets.all() # Devrait afficher tous les posts présents dans la DB, pareil pour Comment
```

*Besoin d'aide ?*
- [Relations dans les bases de données](https://docs.djangoproject.com/fr/4.0/topics/db/examples/)
- [Les modèles en Django](https://docs.djangoproject.com/fr/4.0/topics/db/models/)
- [Les forms en Django](https://docs.djangoproject.com/fr/4.0/topics/forms/)