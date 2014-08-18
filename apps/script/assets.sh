echo 'Compile coffee....'
coffee -c apps/static/js/application.coffee

echo 'Compile sass....'
sass --style compressed apps/static/css/application.scss apps/static/css/application.css
