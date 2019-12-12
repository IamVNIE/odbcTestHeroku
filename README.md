# odbcTestHeroku
odbcDriver Test on Heroku

# Sequence of Commands run

 
heroku create
heroku config:set FLASK_CONFIG=heroku 
heroku buildpacks:add heroku/python
heroku buildpacks:add --index 1 heroku-community/apt
git push heroku master
