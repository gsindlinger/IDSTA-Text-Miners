FROM node:18-alpine3.17


WORKDIR /usr/src/webapp
RUN echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf

COPY ./svelte.config.js ./
COPY ./vite.config.js ./
COPY ./package*.json ./

RUN npm install
RUN npm update

USER root
COPY ./ ./

EXPOSE 5173

ENV HOST=0.0.0.0

CMD npm run dev