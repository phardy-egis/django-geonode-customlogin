# django-geonode-customlogin
## About customlogin
This Django app overrides several Geonode's default templates to provide customized redirection to users.

It is released under GNU-GPL licence version 3.

Detailed documentation is in the "docs" directory.

## Add Django app. to Geonode setup
### Manual install
Here below are listed the instruction for install:

1. If you are using `docker`, stop services

    ```console
    docker-compose down
    ```

2. Add "customlogin" to your INSTALLED_APPS by adding the following lines at the end of `./geonode/settings.py` file:

    ```python
    # Addition of customlogin app
    INSTALLED_APPS += ('geonode.customlogin',)
    ```

3. Include the customlogin URLconf in `./geonode/urls.py` file like this:

    ```python
    if "geonode.customlogin" in settings.INSTALLED_APPS:
        urlpatterns += [  # '',
            url(r'^customlogin/', include('geonode.customlogin.urls')),
        ]
    ```

4. Move `customlogin` folder inside `./geonode` django project folder:


5. If you are using `docker`, rebuild geonode and restart services (this may stop the web site for a while):

    ```console
    docker-compose down && docker-compose build && docker-compose up -d
    ```

6. Once geonode has restarted, authneticated users with admins permissions can reach the endpoints under `/customlogin/api` to search for datasets.

7. `customlogin` comes with [customlogin-frontend](https://github.com/phardy-egis/django-geonode-customlogin-frontend). A [customlogin-frontend](https://github.com/phardy-egis/django-geonode-customlogin-frontend) production build should be served to make the interface available for users.

### Example setup

You can find an example of geonode setup with customlogin app in this repo: [django-geonode-dev](https://github.com/phardy-egis/django-geonode-dev.git). 