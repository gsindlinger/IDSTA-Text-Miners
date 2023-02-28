FROM node:18-alpine3.17


WORKDIR /webapp
COPY package.json package-lock.json ./
RUN npm ci

# Copy all local files into the image.
COPY . .

RUN npm run build

EXPOSE 3000
CMD ["node", "build"]