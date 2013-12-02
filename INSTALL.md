
## Installation

For the commands below `/home/ubuntu/web/gradame/` is used as location of the project. Edit before executing commands
if your locaiton is different.

### OS Requirements
 - nginx server
 - uwsgi server
 - uwsgi python plugin
 - pip (python package manager)
 - django
 - virtualenvwrapper
 - mongodb 2.4+

### Virtual environment

Guarantee and switch to a clean virtual environment
```
mkvirtualenv grada.me --no-site-packages
workon grada.me
```
### App dependencies

Install app dependencies
```
pip install -r requirements.txt
```

### Local settings

Make sure you edit:

 - Domain name for your website in `gradame.dev.nginx` and `gradame.nginx`.
 - Paths in `gradame.dev.nginx`, `gradame.nginx` and `gradame.uwsgi`

### Nginx server

Enable "gradame" in `nginx` server:
```sh
# in development:
sudo ln -s /home/ubuntu/web/gradame/gradame.dev.nginx /etc/nginx/sites-enabled/
# in production
sudo ln -s /home/ubuntu/web/gradame/gradame.nginx /etc/nginx/sites-enabled/
```

And then to activate:
```sh
sudo service nginx restart
```
### UWSGI server

Enable & activate "gradame" in the `uwsgi` server:
```sh
sudo ln -s /home/ubuntu/web/gradame/gradame.uwsgi /etc/uwsgi/apps-enabled/gradame.ini
sudo service uwsgi restart
```

### Database
Login to mongo shell (example uses a local server)

```
mongo localhost:27017/gradame
```

Make sure indexes are set correctly
```
db.signals.ensureIndex( { location : "2dsphere" } )
