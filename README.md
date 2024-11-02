# Project Game
Project Game is a gaming related news website modelled on sites such as Reddit and the Escapist where the site owner and registered users can post stories (called threads) about news from the games industry or anything else related to the topic of video games. The goal is to provide a space where those with an interest in gaming can discuss it and get to know other hobbyists.

## UX Design:
This site has been designed to have a simple easy to understand layout. The target user is anyone interested in gaming of any age who wishes to discuss their hobby and developments in the industry. 

### Colours and typography
The colour scheme of the site was inspired by that of the forums on escapistmagazine.com. This was chosen because the colours are not distracting but provide a high enough contrast that everything is easily readable. Colours such as these are often used as standard in games consoles and websites, making the website more thematic.

Pixelify Sans was used for the site logo as it provides a thematic way to present the site without compromising on readability. Gill Sans was chosen for the main body elements, Nanum Gothic for the footer and Rubik for the links to threads and the names of who posted a given entry. This variance of font styles on the page allowed elements to be visually distinct without becoming distracting.


## User Stories

## Technologies used
### Languages
+ Python - the language used to develop the server side of the site
+ HTML - markup language used to create the site
+ javaScript - used to develop interactive elements of the site
+ CSS - used to style the site

### Frameworks and Libraries
+ Django - the python framework used to create the site's logic
+ jQuery - used to control click events and AJAX requests
+ Bootstrap - CSS framework used to help style the site

### Databases
+ SQLite: database used during development 
+ PostgreSQL: tUsed to store project data

### Other tools
+ Git: Used for version control
+ Pip3: used to install the dependencies
+ Gunicorn: webserver used to run the site
+ Spycopg2: the database driver used to connect to the database
+ Django-allauth: authentication library used to create users
+ Django-crispy-forms: Used to help render Django forms
Render: the cloud platform used to host the website.
ElephantSQL: the cloud database used to store all the data.
+ GitHub: used to host source code
Gitpod: IDE used for development.
+ Chrome DevTools: used to help with debugging
+ Font Awesome: used for footer icons
+ Miro: website used to make a flowchart and wireframes
Coolors was used to make a color palette for the website.
+ W3C Validator: Used to validate HTML code
+ W3C CSS validator: Used to validate CSS code
+ JShint: Used to validate JS code
+ PEP8: Used to validate python code
## Features



### Colours and typography
The colour scheme of the site was inspired by that of the forums on escapistmagazine.com. This was chosen because the colours are not distracting but provide a high enough contrast that everything is easily readable. Colours such as these are often used as standard in games consoles and websites, making the website more thematic.

Pixelify Sans was used for the site logo as it provides a thematic way to present the site without compromising on readability. Gill Sans was chosen for the main body elements, Nanum Gothic for the footer and Rubik for the links to threads and the names of who posted a given entry. This variance of font styles on the page allowed elements to be visually distinct without becoming distracting.


### Wireframes & Flowcharts
[Wireframes](features/wireframes)

[Organisational-Flowchart](features/flowchart)

There is a difference visible between the flowchart and wireframes and what was deployed. The differences in layout were decided on because the current layout was found to be as easy to read as the inital proposal, and required less adjustment for smaller and larger screen sizes, resulting in a more consistent layout. The proposed feature that would have allowed users to post and edit threads of their own was implemented but had to be removed from the project due to time constraints. Ongoing difficulties implementing the update and delete functionality caused significant delays and the feature had to be scrapped to ensure and MVP would be deployed. 

## Information Architecture
### ERD

### Data Modelling

1. Thread Model
This provides the structure for the threads that users can post and respond to. 

|Name|Key|Field Type|Validation|
|--|--|--|--|
|Title|title|CharacterField|max_length=150, unique = True, blank=False|
|Slug|slug|SlugField|max_length=200, unique=True|
|Poster|poster|ForeignKey|User, on_delete=models.RESTRICT, related_name="news_posts"|
|Body|body|TextField|--|
|Posted on|posted_on|DateTimeField|auto_now_add=True|

2. Response Model
This provides the structure for the reponses that users can post, edit and delete from threads. 

|Name|Key|Field Type|Validation|
|--|--|--|--|
|Poster|poster|ForeignKey|User, on_delete=models.RESTRICT, related_name="news_posts"|
|Thread|thread|ForeignKey|Thread, on_delete=models.RESTRICT, related_name="responses"|
|Content|content|TextField|--|
|Posted on|posted_on|DateTimeField|auto_now_add=True|

3. Report Model
This provides the guidelines users should follow when reporting specific individuals. 

|Name|Key|Field Type|Validation|
|--|--|--|--|
|Title|title|CharacterField|max_length=150, unique = True, blank=False|
|Updated on|updated_on|DateTimeField|auto_now_add=True|
|Content|content|TextField|--|

4. Report User Model
Provides structure for users to input information when reporting others that admins can read

|Name|Key|Field Type|Validation|
|--|--|--|--|
|Thread URL|thread_url|URLField|blank=False|
|User Being reported|user_being_reported|CharField|blank=False|
|Reason for report|reason_for_report|TextField|blank=False|
|Reporter's email|reporters_email|EmailField|blank=False|
|Examined|examined|BooleanField|default=False|

## Testing
For full details of testing , please see [TESTING.md](TESTING.md)

## Deployment

## Credits

## Acknowledgements