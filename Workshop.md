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
* `settings.py` : Ce fichier contient toute les paramètres de fonctionnement de votre application
* `mysite/urls.py` : Ce fichier contient les déclarations d'URL pour ce projet Django
* `asgi.py` et `wsgi.py` : Ces fichiers ne ne les calcule pas (c'est pour le déploiement en très gros).

Maintenant que tout est créé, déplace toi dans le dossier et lance le serveur :

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

```
from django.http import HttpResponse


def ma_vue(request):
    return HttpResponse("Oh pète sa mère ! Ma vue marche !")
```

Maintenant que la vue a été créée il faut maintenant la connecter à une URL.

Créons un fichier `urls.py` à l'intérieur du dossier `news` et dedans ajoute ça :

```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
]
```

_Le premier paramètre de la fonction `path()` sert à définir la route. Laisser des guillements vides (`path('')`) équivaut à la route `/`_

Bien ! L'URL existe dans les routes de l'application `news` mais pas dans les routes du projet. Il nous reste donc une dernière chose à faire cette fois-ci dans le `urls.py` à l'intérieur du dossier `<le-nom-de-ton-projet>` :

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
]
```

Maintenant il est temps de voir cette vue de nos propres yeux.

Relance le serveur et si tout s'affiche alors tu peux continuer !
