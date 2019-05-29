# Description 

This is an example repository on using connexion (https://github.com/zalando/connexion) with open api

# Running

## With docker

```bash
docker-compose up
```


The docker image comes with the necessary setup to be able to deploy your api to aws using Zappa (https://github.com/Miserlou/Zappa)

## Without docker

```bash
pip install -r requirements.txt
python main.py
```

## Checking your live doc

Your application will the be running on port **8080**

To see your documentation go to:

**localhost:8080/ui**

# Live example

I have deployed an example where you can test making calls against:

https://hxypd7rwx9.execute-api.us-east-1.amazonaws.com/development/hello-world
