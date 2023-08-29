# NBA FaceOff 

This is an app where one can type in the names of two NBA players and the app will return the better player of the two
along with their scores.

## How is the better player determined?

In order to determine who is the better player, the scoreCalculator.py file contains a function that takes into account the statistics of both players which includes hand picked general stats, advanced stats, and accolades to quantify how good of a player 
they are. The stats are retrieved using the nba.com api client, as well as web scraping particular stats not included in the api from nba.com and basketball reference. Utilizng those statistics, I was able to come up with a score.

## Limitations

One major limitation of my app is the fact that NBA players drafted in the 2000 NBA draft and before are not included and this is because the NBA did not track advanced statistics such as true shooting percentage, offensive, and defensive rating before 2000. And in order to come up with the most accurate and non biased scores to compare NBA players, those statistics are necessary.

##
