# JaSON

### Getting Started on building a web app using Oracle DB with JSON functionality

## An introduction


The JaSON application is a template web application that extends Flask, a lightweight microframework for Python. The demo uses Twitter Bootstrap for style, Oracle DB for the database, and SQL Alchemy for easy DB connectivity.
 
JaSON was built to be a simple demo that showcases how using JSON as a document store with Oracle DB 12c provides a flexible and scalable development environment, even for novice web developers. In this document, we’ll walk you through how to install and setup the demo application, the general file structure, some details about the tech stack, and a summary of the JSON functionality it showcases.

## Installing Dependencies

In order to run the app on your machine you’ll need to follow these quick installation steps:
 1.	Download and configure an Oracle DB 12c.
 2.	If you do not already have python on your machine, you will need to download it from here. If you do not already                have pip installed on your machine, you will need to follow these instructions.
 3.	In your command window, run;         
 
           pip install Flask
           pip install Flask-SQLAlchemy
           pip install Flask-WTF

 4.	Install bootstrap by following these instructions.
 5.	Clone our git repo https://github.com/knordin/JaSON

## Running the DB Setup Script

Once you have successfully installed all the dependencies above, you’ll need to run a SQL setup script. You can run this script however you like, but we recommend installing SQL Developer because it has a GUI interface so you can view the data easily.

## Running the Application

Now you are ready to run the application. All you need to do is open a command window and run:

    python main.py  

## Modules

Although it is possible for a Flask app to be contained entirely within a single Python module, this project splits different functionality into different modules to facilitate maintainability. Below is a description of each module.

-   'init.py' – Constructs the Flask app object and configures it. Imports the other modules to emulate a single-model application.
-   'config.py' – Contains the app configuration and DB connection.
-   'forms.py' – Contains WTForms Form objects for use in views and templates
-   'hooks.py' – Contains Flask and Jinja helper methods.
-   'models.py' – Contains the database model classes for SQLAlchemy.
-   'views.py' – Contains the app views.
-   'startup.sql' – Contains the sql scripts to create users, define privileges and create tables required for the app.

## Tech Stack Details

Here’s a diagram depicting the stack moving from back-end to front-end: 

[url for image]

SQLAlchemy is a database toolkit for python that uses cx_oracle to connect to Oracle DB. This connection allows you to write SQL statements directly into the Python code. Flask is a lightweight web framework for Python with a simple but extensible core. On the front-end we’re using Bootstrap, a framework designed by Twitter for faster and easier web development. 

## Scope and Purpose

The purpose of this app is to help you learn Oracle DB, SQL, and web app building skills in Python. It’s meant to be quick and simple, using popular developer tools to showcase powerful Oracle DB & JSON functionality. The app is a basic social directory template, the “Hello, World!” of web applications. It’s flexible and dynamic based on its use of JSON as a document store as opposed to a rigid schema.
 
JSON functionality
The application showcases several handy JSON functions, both in SQL and Python. In SQL, 
we are utilizing the check constraint “ENSURE_JSON” and utilizing JSON dot notation to access the data.  In Python, we are also using JSON dot notation, as well as using the methods json.dump() and json.loads() to encode data into JSON. 

## Screenshot

![](https://raw.github.com/fogleman/HelloFlask/master/screenshot.png)
![](https://raw.github.com/knordin/JaSON/blob/master/LoginScreenshot.png)
