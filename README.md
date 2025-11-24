Exercice 1 : Créer une application Node.js avec Docker
===============================================
Ce projet contient une simple application Node.js qui répond "Hello, Docker!" sur le port 3000. L'application est conteneurisée à l'aide de Docker.

1 - Créer un Dockerfile

2 - Écrire un Dockerfile pour une application Node.js avec toutes les instructions nécessaires

Builder l'image
```bash
Exécuter docker build -t mon-app . pour créer votre image personnalisée
```

3 - Tester l'application

Lancer le conteneur et vérifier que l'application fonctionne correctement


## Commandes Docker pour l'application Node.js

```bash
# Builder l'image
docker build -t demo-nodejs:1.0 .

# Vérifier que l'image existe
docker images | grep demo-nodejs

# Exécuter le conteneur
docker run -d -p 3000:3000 --name mon-app-node demo-nodejs:1.0

# Tester l'application
curl http://localhost:3000

# Voir les logs
docker logs mon-app-node

# Nettoyer
docker stop mon-app-node
docker rm mon-app-node
docker rmi demo-nodejs:1.0
```