# KLBlog

A multi-user blog system written with django.

[![Build Status](https://travis-ci.com/kaleid-liner/KLBlog.svg?branch=master)](https://travis-ci.com/kaleid-liner/KLBlog)

## Features

- Post with **Markdown** support and code highlight
- Awesome Django access control with [django-rules](https://github.com/dfunckt/django-rules)
- Comment on comments and Comment on posts (*also support markdown*)
- UI beautified with Bootstrap

## Installation

To install dependencies, run

```shell
pip -r requirements.txt
```

## Settings

Provide a file named `local_settings.py`, you can check `local_settings.py.example` for reference. If the file isn't provided, it will fall back on `default_settings.py`.

## Set up the database

```shell
python manage.py migrate
```

## Running

### Run on a development server

Set `DEBUG` to `True`, and enter:

```shell
python manage.py runserver
```

### Run on a deployment server

Set `DEBUG` to `False`. You can use uwsgi/nginx or anything you like to deploy it. 
Then enter:

```shell
python manage.py collectstatic
```

Please notice you should set `STATIC_ROOT`/`MEDIA_ROOT` and config your web server to serve static files and media files.
