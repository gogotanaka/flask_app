Pakopako
========

## Setup environment and launch neo4j and flask server
```
$ chmod +x init.sh
# required password in processes.
$ sh init.sh
```

## Setup envirionment (old)

```
$ brew bundle
$ sudo pip install -r requirements.txt
```

## Create local SQLite3 database
```
$ cat apps/db/schema.sql | sqlite3 apps/db/pakopako.sqlite3
```

## Start server

`$ sh apps/script/server.sh`

## Directory structure

```
.
|
 -- apps (main directory)
|   |
|   |-- controllers
|       |
|        -- __init__.py (import all controllers in this directory)
|       |
|        -- prototype.py (angularjs test files)
|       |
|        -- user_controller.py (user login and registration controller)
|   |-- models
|       |
|        -- __init__.py (import all models in this directory)
|       |
|        -- user.py (user model)
|   |-- static
|       |
|       |-- css
|           |
|            -- application.scss
|       |-- js
|           |
|            -- angular.min.js
|           |
|            -- application.coffee
|   |-- tempaltes
|       |
|       |-- layouts
|           |
|            -- layout.html (header and footer template; import static files in this)
|       |-- prototype
|           |
|            -- index.html (example angularjs view)
|       |-- users
|           |
|            -- index.html
|           |
|            -- show.html
|           |
|            -- login.html
|           |
|            -- registration.html
|    -- __init__.py
 -- Procfile (setup commands on deploying to heroku production server)
|
 -- requirements.txt (required modules)
|
 -- server.py (script for up server)
```
