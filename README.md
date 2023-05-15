# FastApi Crash Course From <a href="https://www.youtube.com/@Systembound-JustFastApi?view_as=subscriber">Just FastApi</a>
### Watch the tutorial here: <a href="https://youtu.be/D-TqTLoFybo">Python FastApi Crash Course</a>
## Setting Up Development
move `.env.example` file to `.env`
```
mv .env.example .env
mv docker-compose.dev.yaml docker-compose.yaml
```

## Production Deployment
move `.env.example` file to `.env`. However, make sure to fill `SENTRY_DSN` for production 
```
mv .env.example .env
mv docker-compose.prod.yaml docker-compose.yaml
```
# Dot Env file configuration
Edit the `DB_URL` with your database url such as `sqlite://` or `postgres://`.
### Run the application in production
After when you are done editing. Run the container in the background (daemon mode).
```
docker-compose up -d
```
