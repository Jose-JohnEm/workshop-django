# Workshop Django : Créer son un réseau social avec Django

Ce Workshop est destiné aux débutants en Django.
Avec ce Workshop, tu apprendras : 

:white_check_mark: Les modèles


:white_check_mark: Les forms faits pour créer des modèles


:white_check_mark: Le système d'authentification de Django


:white_check_mark: L'architecture MVT

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
    path('posts/', include('posts.urls')),
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
  context_object_name = "posts"
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

## Etape 5 : Les utilisateurs

### 5.1 : Modèles
Django nous donne d'emblée un modèle d'utilisateur prédéfini. Cependant, il est tout de même conseillé d'hériter de
ce modèle, au cas où l'on voudrait le customiser plus tard.
C'est donc ce que nous allons faire dans `users/models.py`:
```python
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    pass
```
Dans `<le-nom-de-ton-projet>/settings.py`, il faut préciser que le modèle d'authentification à regarder pour le moteur django
est le nôtre, défini dans `users/models.py`
```python
AUTH_USER_MODEL = 'users.User'
```
### 5.2 Vues

Il faut savoir que Django nous donne d'emblée un set d'urls prédéfini pour les actions basiques d'utilisateurs avec `accounts`.
Néanmoins, nous avons quelques petites choses à ajouter pour signifier au moteur de Django que c'est ce que nous souhaitons utiliser :
```python
# <le-nom-de-ton-projet>/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('users.views'))
]
```
Désormais, nous avons accès à toutes ces urls : 
```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```
> :bulb: les variables `name=` correspondent au nom de notre vue. Par exemple, pour l'url [http://localhost:8000/accounts/login]()
> nous devons définir sa vue correspondante avec le nom `login`. C'est d'ailleurs ce que nous allons faire !

Complètes les vues suivantes :
```python

def register(request):

  if request.user.is_authenticated:
    return redirect('/')

  if request.method == 'POST':
        ... # TODO
        return redirect('/')
  return render(request, 'accounts/register.html', {"form": UserCreationForm}) # Petite indice sur le form built-in à utiliser !


def login(request):

  if request.user.is_authenticated:
    return redirect('/')

  if request.method == 'POST':
    ... # TODO
  return render(request, 'accounts/login.html', {"form": AuthenticationForm})


def logout(request):
  ... # TODO
  return redirect('/')
```
:warning: Merci de garder le même path pour les templates HTML, car c'est comme ça qu'elles sont nommées dans le front.

> :bulb: Les forms `UserCreationForm` et `AuthenticationForm` ne sont pas à codés, mais sont déjà implémentés dans Django !

> :bulb: Si la migration ne fonctionne pas, supprime le fichier `db.sqlite3`, tous les fichiers dans les dossiers `migrations`
> (`users/migrations` et `posts/migrations`) sauf les `__init__.py`, ainsi que les dossiers `__pycache__/`.

### 5.3 Synchroniser

Maintenant que nous avons des utilisateurs, ils seraient temps qu'ils soient maîtres de leurs postes et de leurs
commentaires !
 - [ ] Complète les modèles Post et Comment en leur ajoutant à tous deux un field author, qui est une relation de type
 - `ForeignKey`, liée à notre objet `User` se trouvant dans `users/models.py`.
 - [ ] Dans `posts/templates/post/feed.html` ligne `149`, remplace "Me" par `{{post.author_username}}`
 - [ ] Dans `posts/templates/post/feed.html` ligne `190`, remplace "Jason Bourne" par `{{comment.author_username}}`
 - [ ] Même principe dans le fichier `posts/templates/post/post_detail.html`.

La synchronisation et la majeure partie du Workshop est désormais terminée !

## Bonus

- [ ] Une page profile de l'utilisateur, avec vue et un form pour modifier
- [ ] Un avatar customisé
- [ ] Des likes sous les posts et les commentaires
- [ ] Principe de "follow" "unfollow"
