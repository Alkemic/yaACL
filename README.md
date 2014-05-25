yaACL
=====

Yet another access control list (ACL) per view for Django


## Installation
* Clone this repo to your PC
* Run ``pip install yaACL``
* Put ``yaacl`` in INSTALLED_APPS, after auth and admin apps
* Run ``./manage.py syncdb``


## Configuration
* This app get information about
* If you also have


## Usage
In views, import ``acl_register_view``, then decorate views you want under control access.

```python
from yaacl.decorators import acl_register_view

@acl_register_view('short_resource_name', 'Short description about this view')
def index(request):
    pass
```

First parameter is the short name for this view (resource). Second parameter is a description, and isn't required.

It's up to you how you name those resources, but I recommend (and use in project I made this app) to name them as
``<app_label>.<view_name>``, so later in templates you can check if user has access to all resources in ``<app_label>.``

Let's say, you have a typical CRUD view in you news application, so code would be like this:

```python
from yaacl.decorators import acl_register_view

@acl_register_view('news.index', 'News list')
def index(request):
    ...

@acl_register_view('news.create', 'Create new news')
def create(request):
    ...

@acl_register_view('news.update', 'Update news entry')
def update(request):
    ...

@acl_register_view('news.delete', 'Delete news entry')
def delete(request):
    ...
```

So, your resources list will be like this:

| pk | resource    | description       |
| -- | ----------- | ----------------- |
| 1  | news.index  | News list         |
| 2  | news.create | Create new news   |
| 3  | news.update | Update news entry |
| 4  | news.delete | Delete news entry |

Now if you want to check if current user has access to news.index, then in templates

```html
{% load acl %}

...

{% if request.user|has_access:'news.index' %}
Yes it has access to news.index view.
{% else %}
No, it has not.
{% endif %}

```

But if you want to check if user has access to


```html
{% if request.user|have_access:'news.' %}
Yes it has access to all resources in news.
{% else %}
No, it has not.
{% endif %}

```

## Information
* If flag ``is_superuser`` is ``True``, then always access is granted
* No-access page template is located in ``yaacl/no_access.html`` file
* Test in ``has_access`` template tag just check if resource name starts with given name
* This app uses monkey-patch to inject new field (the acl field) into user and group model


## Todo
* Per group access
* ``.travis.yml``
* A flag, to indicates a resources that staff members has full access
* Extend this documentation with information about two monkey-patches I've been using and information about admin
