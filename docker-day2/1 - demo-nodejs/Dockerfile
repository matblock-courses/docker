# 1. Image de base - Alpine est plus légère
FROM node:18-alpine

# 2. Métadonnées (optionnel mais bonne pratique)
LABEL maintainer="votre@email.com"
LABEL description="Application Node.js de démonstration"

# 3. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 4. Copier les fichiers de dépendances AVANT le code
# Cela optimise le cache des layers
COPY package*.json ./

# 5. Installer les dépendances
RUN npm install --production

# 6. Copier le reste du code source
COPY . .

# 7. Exposer le port (documentation, pas de mapping réel)
EXPOSE 3000

# 8. Définir la variable d'environnement
ENV NODE_ENV=production

# 9. Commande par défaut pour démarrer l'app
CMD ["npm", "start"]

# Alternative avec ENTRYPOINT :
# ENTRYPOINT ["node"]
# CMD ["app.js"]