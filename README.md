## Mon projet en ligne : https://djangotamimstore.onrender.com

Ce projet Django est hébergé sur Render et est déployé à partir de mon dépôt privé (DjangoTamimStore). J'ai créé ce dépôt public (DjangotamimStorePublic) car je ne pouvais pas partager mes informations sensibles (credentials SMTP, super utilisateur de la base de données) publiquement.

## Installation

Assurez-vous d'avoir Django installé : 
    ```
    pip install Django
    ```
Installez les dépendances :
    ```
    pip install -r requirements.txt
    ```
Effectuez les migrations :   
    ```
    python manage.py makemigrations 
    python manage.py migrate
    ```
Ajoutez vos propres paramètres SMTP dans settings.py
Ajustez les STATIC_URL et générez les fichiers statiques si nécessaire.

## Fonctionnalités

**Boutique en ligne**: Intégration d'une API pour la gestion des produits.
**Blog**: Système CRUD pour créer, lire, mettre à jour et supprimer des articles.
**Authentification**: Les super utilisateurs peuvent gérer les utilisateurs et les articles.
**Sécurité**: Envoi de mails de vérification lors de l'inscription et de la réinitialisation de mot de passe pour prévenir les abus.


#Ce projet est un terrain d'expérimentation pour mes compétences en Django, notamment l'intégration d'API, le CRUD et l'authentification surtout de deployer une application django full stack.







## Live Project

You can access the live project at [https://djangotamimstore.onrender.com](https://djangotamimstore.onrender.com)

This Django project is deployed on Render from my private repository (DjangoTamimStore). I created this public repository (DjangotamimStorePublic) because I couldn't share my sensitive information (SMTP credentials, database superuser) publicly.

## Installation

 Make sure you have Django installed: 
    ```
    pip install Django
    ```
 Install the dependencies: 
    ```
    pip install -r requirements.txt
    ```
 Run the migrations: 
    ```
    python manage.py makemigrations 
    python manage.py migrate
    ```
 Add your own SMTP settings in `settings.py`
 Adjust the `STATIC_URL` and generate the static files if needed.

## Features

- **Online Store**: API integration for product management.
- **Blog**: CRUD system to create, read, update, and delete posts.
- **Authentication**: Superusers can manage users and posts.
- **Security**: Verification emails sent upon signup and password reset to prevent abuse.

## About

This project is a playground for my Django skills, especially API integration, CRUD, and authentication specifically deploying a full stack django app.
