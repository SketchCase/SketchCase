# SketchCase

## Installation/run locally

With Docker & docker-compose installed and setup:

```
docker-compose up
```

Go to http://[your docker machines ip]:8080 and create new database with the name `sketchcase`.

Run:

```
docker-compose run web python sync_db.py
```

And you should be good to go!