# Getting started

All three components (Client, Server, Data Store / Elasticsearch) are dockerized, i.e. you just need to start the docker containers defined in the [compose.yml](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/compose.yml), e.g. using docker-compose functionalities.
Make sure the ports for the three components are available on your machine:
* ElasticSearch: 9200
* FastAPI: 2999
* Webapp: 3000

After launching the containers, you can check out the webapp on [localhost:3000](http://localhost:3000).

Note that it will take a few moments for the database to be initialized and the data to be indexed.

1. Run docker-compose
```docker-compose up --build```
