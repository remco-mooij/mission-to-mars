![alt text](https://github.com/remco-mooij/mission-to-mars/blob/master/static/images/mission-to-mars.png)

This is a simple web app that displays recent data about Mars. It scrapes various websites such as Twitter and the NASA sites, adds the scraped data to a MongoDB database and displays it on a single webpage.

## Instructions
To display the data, make sure to run MongoDB in the background. Instructions on how to install MongoDB can be found [here](https://docs.mongodb.com/manual/installation/). After installation, run the following command in a command prompt or shell:
```
mongod
```
To run the web app, open a new shell and run the following command from the root directory of the repo:
```
python app.py
```
