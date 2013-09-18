# Django Angular Blog
A simple single page blog with [django-rest-framework](https://github.com/tomchristie/django-rest-framework) and [AngularJS](https://github.com/angular/angular.js)



## Quick Setup [demo project]:

    $ git clone https://github.com/goldhand/django-angular-blog.git
    $ cd django-angular-blog/django-angular-blog/
    $ pip install -r requirements/requirements.pip
    $ cd django-angular-blog/
    $ python manage.py syncdb
    $ python manage.py runserver

### Create a new blog post:

    $ curl -X POST http://127.0.0.1:8000/api/posts/ -d "title=[post.title]content=[post.content]" -u [username]:[password]

Replace `[post.title]` with your post title. Same for everything between `[ ]` brackets


## Sitemap:

    /                   --angularjs application root

    api/                --"api-root"
        posts/          --"post-list"
        users/          --"user-list"
        categories/     --"category-list"
}

## Models:

![Django AngularJS Blog Models](https://github.com/goldhand/django-angular-blog/raw/master/models.png "Django AngularJS Blog Models")


