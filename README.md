# Movie-Trailer Website

SYNOPSIS:
This project is a webpage of 10 of my favorite films. For each film, I have included a movie poster, 
YouTube trailer, storyline info, link to Rotten Tomatoes and a link to iTunes to purchase the film. 


TECHNOLOGY STACK:
Python - Data-structure and .html file generation.
jQuery - JavaScript library to generate .html file.
Bootstrap - CSS framework to style page.


DESCRIPTION:
media.py: 
- This file creates the 'Movie' 'class' data structure to store the relevant information for each movie. "Title", "Storyline",
"Poster Image", "YouTube Trailer Link", "Rotten Tomatoes Link", "iTunes Link", "Unique ID". This file also initializes
each of the pieces of information above as variables. 

entertainment_center.py:
- This file creates instances of the 'Movie' class from media.py. Each movie here is assigned its 
own "Title", "Storyline","Poster Image", "YouTube Trailer Link", "Rotten Tomatoes Link", "iTunes Link", "Unique ID".
- The file the places each instance of the 'Movie' class in a list 'movies'
- The file is also used to run the entire program by calling 'open_movies_page()' in fresh_tomatoes.py with the list of movies[].

fresh_tomatoes.py:
- This file is used to generate all the html needed. The html content is written into strings which are taken in by the
create_movie_tiles() function to create a tile for each instance of 'Movie'.
- open_movies_page() method takes all the tiles generated and renders it into a .html file. 

/images
- Stores image files needed. 


INSTALLATION: 
Internet access is required. 
media.py, entertainment_center.py, fresh_tomatoes.py and images folder must all be saved in the same directory.
RUN the entertainment_center.py file. 
This project is also hosted at anirvan90.github.io

CITATIONS:
- Udacity: fresh_tomatoes.py was create by udacity with addtions from me
- Udacity Discussion Forums: Some questions pertaining to the functionality of certain bits of code were answered with the help of other members of the Udacity community, particularly these forums: -https://discussions.udacity.com/t/extend-functionality-of-movie-trailer-website/35531/3
-https://discussions.udacity.com/t/error-adding-new-modal/36003/23

  
