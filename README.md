yaACL
=====

Yet another access control list (ACL) per view for Django


## Installation
* Clone this repo to your PC
* Run ``pip install yaACL``
* Put ``yaacl`` in INSTALLED_APPS, after auth and admin apps
* Put ``import yaacl`` at the end of your current settings file
* Run ``./manage.py syncdb`` or ``./manage.py migrate``


## Configuration
* This app get information about your auth user model form settings
  (``AUTH_USER_MODEL``)
* If you also have custom group model, then define it in
  ``settings.ACL_GROUP_USER_MODEL`` (ie: ``cms_user.group``)


## Usage
In views, import ``acl_register_view`` or ``acl_register_class``, then
decorate views you want under control access. After all views are decorated,
run command ``./manage.py sync_acl``, so all views will be registered in
database.

```python
from yaacl.decorators import acl_register_view
from django.contrib.auth.decorators import login_required


@login_required
@acl_register_view('short_resource_name', 'Short description about this view')
def index(request):
    pass
```

First parameter is ``display_name`` the short name for this view (resource).
Second parameter is ``resource_name``, and isn't required. If
``display_name=None, ``resource_name`` not supplied, the name for resource will
be generated by joining module name and function/class name

It's up to you how you name those resources, but I recommend (and use in
project I made this app) to name them as ``<app_label>.<view_name>``, so
later in templates you can check if user has access to all resources
in ``<app_label>.``

Let's say, you have a typical CRUD view in you news application, so code
would be like this:

```python
from yaacl.decorators import acl_register_view
from django.contrib.auth.decorators import login_required


#decorationg standard function based views
@login_required
@acl_register_view('News list', 'news.create)
def index(request):
    ...

@login_required
@acl_register_view('Update news entry')
def update(request):
    ...

@login_required
@acl_register_view('Delete news entry')
def delete(request):
    ...

#decoration class-based views
@acl_register_class(u"Create news")
class Create(FormView):
        ...


```

So, your resources list will be like this:


* ``news.views.index`` News list
* ``news.create`` Create new news
* ``news.views.update`` Update news entry
* ``news.views.delete`` Delete news entry

Now if you want to check if current user has access to news.index, then in
templates you can check them by using code like:

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
* Test in ``has_access`` template tag just check if resource name starts with
  given name
* This app uses monkey-patch to inject new field (the acl field) into user and
  group model
* **Big fat warning:** while ``./manage.py migrate`` will create many-to-many
  relations for yaACL, those table are still not registered in any migration,
  so if you create migration for auth by using ``./manage.py makemigrations``
  you will have to fake them by running ``./manage.py migrate --fake auth 0002``


## Todo
* ``.travis.yml``
* A flag, to indicates a resources that staff members has full access
* Extend this documentation with information about two monkey-patches I've
  been using and information about admin
