# IDSTA-Text-Miners: Hate, Discrimination & Racism in German Rap - A Text Analytics Approach

[![Download Report](https://img.shields.io/badge/Download--PDF-Report-orange)](https://github.com/gsindlinger/IDSTA-Text-Miners/raw/main/Report/report.pdf)

[![Download Proposal](https://img.shields.io/badge/Download--PDF-Proposal-green)](https://github.com/gsindlinger/IDSTA-Text-Miners/raw/main/Proposal/project-proposal.pdf)

[![Open Webpage](https://img.shields.io/badge/Open-Webpage-blue)](https://gsindlinger.github.io/IDSTA-Text-Miners/)


<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/gsindlinger/IDSTA-Text-Miners/main/title.png" alt="Project title"/>
</p>

Team Members:
- Gal Lebel (galbalandroid@gmail.com) - Bachelor of Science, Computer Science, Heidelberg University
- Johannes Gabriel Sindlinger (johannes.sindlinger@stud.uni-heidelberg.de) - Master of Science, Data and Computer Science, Heidelberg University

Previous Team Member:
- Mara-Eliana Popescu
- Simon Körner

Below you find all information about this repository and the project we have implemented in the context of the lecture Data Science for Text Analytics in the winter semester 2022/23 at the University of Heidelberg. The folder Assignments contains contents which are accompanying material to the lecture. Proposal, Milestone and Report represent specific parts of the Project, the Report is the final documentation for the project. All the relevant source code about the Project can be found in the corresponding subdirectory, as well as the configuration for running the project on Docker.

All data which contains the dictionary used for checking occurrences of words within lyrics, the results of occurrences check and the lyrics data itself [can be found in the data folder within the project folder](https://github.com/gsindlinger/IDSTA-Text-Miners/tree/main/Project/Server/data).

## Project Information

### Getting Started
All three components are dockerized, i.e. you just need to start the docker containers defined in the [compose.yml](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/compose.yml), e.g. using docker-compose functionalities.
Make sure the ports for the three components are available on your machine:
* ElasticSearch: 9200
* FastAPI: 2999
* Webapp: 3000

After launching the containers, you can check out the webapp on [localhost:3000](http://localhost:3000).

Note that it will take a few moments for the database to be initialized and the data to be indexed.

1. Change to the Project folder
```cd Project```
2. Run docker-compose
```docker-compose up --build```

### Technologies / Libraries
* Server / Backend: Fastapi, Spotipy, 
Obtaining Data / Preprocessing / Analysis: Lyricsgenius, Beatifulsoup, Spacy, Gensim, Huggingface-Transformers, German-Sentiment-Bert 
* Data Store: Elasticsearch
* Frontend: SvelteKit, Axios, Tailwind-CSS, D3, SvelteTypewriter

### Code Fragments / Where to find which part of the project?

![Project Pipeline](https://raw.githubusercontent.com/gsindlinger/IDSTA-Text-Miners/main/project_pipeline_final.png)

This picture describes the different parts of this project. Details on the respective parts can be found in the report and the associated code. The following table lists the respective functionalities and the associated folders in the project.

| Part of the project | Functionality |
| --- | --- |
| [Client](https://github.com/gsindlinger/IDSTA-Text-Miners/tree/main/Project/Client) | Displaying research results | 
| [Elasticsearch](https://github.com/gsindlinger/IDSTA-Text-Miners/tree/main/Project/Elastic) | Data storage for Webapp |
| [Server / Fastapi](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/Server/api.py) | Restful service incl. creating Elasticsearch index |

**Pipeline**
| Part of the project | Functionality |
| --- | --- |
| [Artist Generation](https://github.com/gsindlinger/IDSTA-Text-Miners/tree/main/Project/Server/Pipeline/Artist_Generation) | Extracting relevant artists via Spotify API | 
| [Lyrics Extraction](https://github.com/gsindlinger/IDSTA-Text-Miners/tree/main/Project/Server/Pipeline/Lyrics_Scraping) | Extract lyrics from preselected artists via GeniusAPI and HTTP scraping |
| [Preprocessing](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/Server/Pipeline/Preprocessing/zero_shot_classification.ipynb) | Cleaning the dataset, removing songs containing non-german text |
| [Auto-Punctuating and further preprocessing](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/Server/Pipeline/Preprocessing/zero_shot_classification.ipynb) | Punctuating the dataset to split songs into sentences, lemmatization and stopwords removal via spacy |
| [Zero-Shot Classification](https://github.com/gsindlinger/IDSTA-Text-Miners/blob/main/Project/Server/Pipeline/Preprocessing/zero_shot_classification.ipynb) | Using a Zero-Shot classifier to classify songs |


## Project Log

| Date   | Who?                | What?                                                                   | 
|--------|---------------------|-------------------------------------------------------------------------|
| Oct 28 | Johannes Sindlinger | Design pipeline graphics                                                |
| Oct 28 | Johannes Sindlinger | Write motivation, research topic (partly), project description (partly) |
| Oct 30 | Mara-Eliana Popescu | Extend project description                                              |
| Oct 31 | Gal Lebel           | Extend research topic, finish proposal                                  |
| Nov 18 | Johannes Sindlinger | Setup issues for project start                                          |
| Nov 25 | Johannes Sindlinger | Create artist list via Spotify API                                      |
| Dec 10 | Gal Lebel           | Genius Lyrics Scraper                                                   |
| Dec 10 | Gal Lebel           | Milestone Editing                                                              |
| Dec 27/28 | Johannes Sindlinger           | Elasticsearch Connection                                                             |
| Jan 2  | Gal Lebel           | Preprocessing - cleaning up dataset    |
| Jan 2 | Gal Lebel | Filtering out non-German songs (polyglot) |
| Jan 12/13 | Johannes Sindlinger           | Discrimination Dictionary via Word2Vec                                                             |
| Jan 13 | Johannes Sindlinger           | Counting Occurrences via Word2Vec and Lemmatization                                                          |
| Jan 17 | Gal Lebel  | Auto-Punctuation for meaningful splitting into sentences  |
| Jan 29 | Gal Lebel  | Zero-Shot classification        |
| Feb  | Johannes Sindlinger           | Frontend Design                                                          |
| Mar 01 | Johannes Sindlinger & Gal Lebel | Manual Labeling & Evaluation |






## Assignment Log


| Date   | Who?                | What?                     | 
|--------|---------------------|---------------------------|
| Nov 12 | Johannes Sindlinger | Assignment 1 - Exercise 1 |
| Nov 12 | Mara Popescu        | Assignment 1 - Exercise 3 |
| Nov 13 | Simon Körner        | Assignment 1 - Exercise 2 |
| Nov 13 | Gal Lebel           | Assignment 1 - Exercise 2 |
| Dec 09 | Johannes Sindlinger | Assignment 2 - Exercise 2 |
| Dec 10 | Gal Lebel           | Assignment 2 - Exercise 1 |
| Dec 11 | Simon Körner        | Assignment 2 - Exercise 3 |
| Jan 16 | Johannes Sindlinger | Assignment 3 - Exercise 3 |
| Jan 15 | Gal Lebel           | Assignment 3 - Exercise 1 |
| Jan 19 | Johannes Sindlinger | Assignment 3 - Exercise 4 |
| Jan 22 | Simon Körner        | Assignment 3 - Exercise 2 |
| Jan 31 | Johannes Sindlinger | Assignment 4 - Exercise 1 |
| Jan 31 | Johannes Sindlinger | Assignment 4 - Exercise 2 |
| Feb 02 | Johannes Sindlinger | Assignment 4 - Exercise 3 |




