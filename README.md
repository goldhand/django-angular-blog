# django angular blog
a simple single page blog with django-rest-framework and angularjs


## quick setup [demo project]:

    $ git clone https://github.com/goldhand/django-angular-blog.git
    $ cd django-angular-blog/django-angular-blog/
    $ pip install -r requirements/requirements.pip
    $ cd django-angular-blog/
    $ python manage.py syncdb
    $ python manage.py runserver


## sitemap:

    /                   --angularjs application root

    api/                --"api-root"
        posts/          --"post-list"
        users/          --"user-list"
        categories/     --"category-list"
}
