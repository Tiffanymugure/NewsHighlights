# NEWS HIGHLIGHTS
Built by Amira Mugure

## Description
A news site showing news articles from various publishers; with users being able to select a publisher, view articles from them along with their image, description and time of creation.

## User Requirements
* Your users should be able to see various news sources and select the ones they prefer
* Your users should be able to see all the news articles from that news source
* The user should see the image description and time the news article was created.
* The user should also be able to click on an article and read it fully from the news source.

## Features
-[x] List multiple news sources 
-[ ] Listing of articles from the selected news source 
-[x] Categorisation of news networks 
-[ ] Using flask sessions to save users article snippet 
-[ ] Using of browser cookies to store favourite news sources 
-[ ] Redirection of user to articles

## Installation
### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
Python 3.6.4

## Cloning of the respository
In terminal:
* $ git clone https://eleza.herokuapp.com/

## Creating the Virtual Environment
* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate

## Install Dependencies
* pip3 install -r requirements

## Required Libraries
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6
* gunicorn==19.7.1

## Running Tests
* python3 manage.py test

## Running the web app
* python3 manage.py server
* open app in browser by default on 127.0.0.1:5000

## Technology Used
Python3.6

Flask

Heroku

## License Information
MIT License

Copyright(c) 2018 Tiffany Mugure

