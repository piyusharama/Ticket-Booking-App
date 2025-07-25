FROM node:18-alpine
WORKDIR /app
COPY package.json ./
COPY next.config.js ./
RUN npm install
COPY pages ./pages
COPY lib ./lib
EXPOSE 3000
CMD ["npm", "run", "dev"]
