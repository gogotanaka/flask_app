Pakopako
========

## Command to setup envirionment

```
$ sudo pip install -r path/to/requirements.txt
```

## Start server

`$ python server.py`

or

`$ python3 server.py`

## Directory Structure

```
.
|
 -- apps
|   |
|   |-- controllers
|       |
|        -- __init__.py
|       |
|        -- prototype.py
|       |
|        -- user_controller.py
|   |-- models
|       |
|        -- __init__.py
|       |
|        -- user.py
|   |-- static
|       |
|       |-- css
|           |
|            -- application.css
|       |-- js
|           |
|            -- angular.min.js
|           |
|            -- application.coffee
|   |-- tempaltes
|       |
|       |-- layouts
|           |
|            -- layout.html
|       |-- prototype
|           |
|            -- index.html
|       |-- users
|           |
|            -- index.html
|           |
|            -- show.html
|    -- __init__.py
 -- Procfile
|
 -- requirements.txt
|
 -- server.py
```

## Compile coffee

`coffee -c apps/static/js/application.coffee`

## Compile assets

`sh apps/script/assets.sh`
