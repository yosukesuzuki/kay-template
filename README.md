[![Circle CI](https://circleci.com/gh/yosukesuzuki/kay-template.svg?style=svg)](https://circleci.com/gh/yosukesuzuki/kay-template)

# What's this?
This is the template for Kay-framework application.
Built-in tox

# Setup
## Setup Google Cloud SDK
install Google Cloud SDK


## make symlink 
```
sudo ln -s /some/whare/google_appengine /usr/local/google_appengine
```

## run tox
```
$ tox
```

# add application folder
```
$ cd project
$ python manage.py startapp appname
```

# e2e
```
$ npm install --save-dev gulp gulp-protractor gulp-webserver run-sequence
$ node_modules/gulp-protractor/node_modules/protractor/bin/webdriver-manager update
$ gulp test:e2e
```
