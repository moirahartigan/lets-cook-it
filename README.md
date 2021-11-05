# Lets Cook It!
## **Code Institute - Portfolio Project 4: _Full-Stack Toolkit_** 
Lets Cook It! is a virtual recipe collection where all your favourite recipes can be saved in the one place.

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes.
## Demo

[View the Live Website Here](https://lets-cook-it-app.herokuapp.com/)

<img src="https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/i-am-responsive.png">


## Table of contents
+ [User Experience](#User-Experience)
     + [Project Goals](#Project-Goals)
     + [User Stories](#User-Stories)
     + [Strategy](#Strategy)
     + [Scope](#Scope)
     + [Structure](#Structure)
          + [Front-end Pages](Front-end-Pages)
     + [Skeleton](#Skeleton)
          + [Wireframes](#Wireframes)
     + [Surface](#Surface)
+ [Features](#Features) 
     + [Existing Features](#Existing-Features)
     + [Features to Implement in the future](#Features-to-Implement-in-the-future)
+ [Database](Database)
+ [Technologies Used](#Technologies-Used)
     + [General Resources](#General-Resources)
     + [Tools](#Tools)
+ [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
+ [Deployment](#Deployment)
     + [Deployment through GitHub Pages](#1-Deployment-through-GitHub-Pages)
     + [Heroku Deployment](#2-Heroku-Deployment)
     + [Forking the Repository](#3-Forking-the-Repository)
     + [Making a Local Clone](#4-Making-a-Local-Clone)
+ [Credits](#Credits)

***
# User Experience
## Project Goals
The primary goal of Lets Cook It! is to allow the users to create, search, and view their favorite recipes in one place. The goal for the design was to make it as easy as possible to access information, while striving for a minimalist and user-friendly layout.

## User Stories
**As a Casual User, I want to:**

1. Be able to view recipes without having to register and account. 
2. Be able to search through the recipes on the site.
3. Be able to search for recipes that have a specific ingredient.
4. Be able to register for an account if I want to come back at a later date.
5. Be able to able to view a specific number of recipe cards on the recipe page so that only a number of recipe card appear at a time on the page.

**As a Registered User, I want to:**

1. Be able to log into my account.
2. Be able to upload a recipe.
3. Have ease of access to any recipes that I have already added.
4. Be able to view, edit or delete any recipes that I have already added.
5. Be able to add a comment to other recipes.

**As an Administrative Account holder, I want to:**

1. Be able to add new recipes to the site.
2. Be able to edit the pre-existing recipes.
3. Be able to approve any recipe.
4. Be able to delete any recipe.
5. Be able to approve comments left by registered users.
6. Add and edit and delete recipe categories.

<br>

[^ back to top ^](#Table-of-contents)
<br>

## Strategy Plane
### — Project Planning —

 Agile development was implemented from the onset of this project and simply explained Agile is an iterative approach to project management and software development that helps teams deliver value to their customers, faster and with fewer headaches. Instead of betting everything on a "big bang" launch, an agile team delivers work in small, but consumable, increments. As the development team for this project was a single developer I attempted to use this approach for building this project. As the methodology requires a detailed and thorough project planning process, to design and create a web-based interactive application. 
 <br>
 I distinguished the required functionality of the site and how it would answer the user stories, as described above, these user stories were then developed through the use of the Five Development Planes framework. To keep track of my development I created a user stories kanban board in github projects. I created an issue for each user story which was set to automatically display in my user story project. As I worked each user story, it was moved to the in progress column and finally into the completed column once it was complete.  
<br>
The website is designed for those who love to cook, and want to be able to access all their favourite recipes in one place. Users can arrive on the site and simply browse the latest recipes or by following very simple registration steps, they can create an account and post their recipes in a well-structured format. There is a search function on the website so they can search for specific recipes by a ingredient. To see recipes, users do not need to register so it is hassle-free. The design of the website is meaningful and simple so that the purpose of the website is very clear for first-time users, and they can easily adapt to the website. This also applies to all the functions to create, post, edit and delete recipes for regular users. The owner’s main goal is to provide a recipe platform that is easy to use whether they are first-time or returning users, and this is the key to grow the community for further business opportunities. To achieve this, the website is designed and created by users first concept.

The functions on the tables below are minimum requirements for the website to achieve the current user's and owner's goals. On a scale of 1  - 5 

| Opportunity                                 | Importance | Viability / Feasibility |
| :------------------------------------------ | :--------: | :---------------------: |
| Register                                    |     5      |            5            |
| Login / Log out                             |     5      |            5            |
| Create / Edit / Delete Recipes              |     5      |            5            |
| Upload Image For Each Recipe                |     4      |            4            |
| Search Recipes By Keywords                  |     4      |            5            |
| Review By Other Users                       |     3      |            3            |
| Responsiveness                              |     4      |            5            |
| Page 404                                    |     3      |            3            |

Below are the additional functions that can improve the website, however, these are not mandatory to achieve the current user's and owner's goals. Some are not implemented due to a lack of my current skills & knowledge and also due to a lack of time allocated for this project.

| Opportunity                             | Importance | Viability / Feasibility |
| :-------------------------------------- | :--------: | :---------------------: |
| Resetting Password When Users Forget It |     4      |            2            |
| Categories page                         |     4      |            2            |
| Search by Category                      |     3      |            3            |
| Contact us form                         |     3      |            3            |
| “Like” Reaction By Other Users          |     3      |            2            |

## Scope Plane

To achieve user and owner’s goals, above are the minimum features to be included in this project. Also, **CRUD** Create, Read, Update, and Delete functions are required for this project so these are implemented as a part of essential features.

- Simple design Home page that first-time users can recognise the purpose of the website easily. All the recipes are shown on *Home* page through the use of a caorusel;
- Register page where users can create an account to add, post and edit and delete recipes
- Login page where users can log in to the website
- Logout function that users can log out the website
- Profile page where users can see all their recipes and access to add, post, edit and delete recipes
- Create Recipe page where users can add and post their recipes;
- Edit Recipe page where users can edit their recipes;
- Delete Recipe function that users can delete their recipes;
- Search by an ingredient function where users can search for specific recipes
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely

> **Note:**<br>
> A superuser/admin can only create a new category from the backend.

## Structure Plane

### — **Front-end** —

The website consists of a **Home** page with **9 other core pages**.

- **Home** (`index.html`)<br>The landing page of the website. There is a logo, navigation bar to *Recipes*, *Register* & *Login* pages, a title and a hero image. The is an owl carosuel showcasing all the most recent recipes on the website, from here users can click on the call to action button to view the full recipe. There is a footer with some social icons

- **Recipes** (`recipes.html`)<br>The page where all the recipe cards available can be viewed individually. Here users can search recipes by ingredient via the search box at the top of the page. The same navigation bar and footer are used as *Home*.

- **Recipe Detail** (`recipe_detail.html`)<br>The page where once a "View recipe" buttom is clicked the user can view the full details of the recipe. If a user is logged in they can read and leave a comment on this recipe. All if the user is logged in and this is their recipe they can edit and delete this recipe from this page. In addition If the user is a superuser, they can delete any recipe from this page. The user also have a search feature available where users can search recipes by ingredient via the search box at the top of the page. The same navigation bar and footer are used as *Home*.

- **Register** (`account/signup.html`)<br>The page where users can create an account. Once a user creates an account successfully, they will be led to *Profile* page where the user can now start adding recipes. The navigation bar is now different to *Home* page and once a user is registered, the *profile* page and *logout* page is now visible on the navbar.

- **Login** (`account/login.html`)<br>The page where users who have an account can log in to the website. Once users log in successfully, they will be led to *Profile* page. Again the navigation bar is different to *Home* page, and once a user is logged in, the *profile* page and *logout* page is now visible on the navbar.

- **Profile** (`profile.html`)<br>The page where users will be led when they create an account or log in. Users see all of their recipes with an option to view the full recipe,edit or delete the recipe. Users can access the *View Recipe* page *Edit Recipe* page and *Delete Recipe* function by clicking a button on the recipe. There is an option to create a new recipe from this page by clicking a button and that leads to *add Recipe* page. The same navigation bar and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a link to *Profile* page on the navigation bar

- **Add Recipe** (`recipe_form.html`)<br>The page where users can add and post recipes. A summernote editor has been added to the form to allow users the edit the font as they so wish for the recipes they add.

- **Edit Recipe** (`recipe_edit_form.html`)<br>The page where users can edit their own recipes.

- **Search Results** (`search_results.html`)<br>The page where users can view all the recipes returned from their search query.

- **Delete Recipe** (`recipe_delete.html`)<br>The page where users can delete their own recipes.

- **Delete Confirmation** (`recipe_delete_confirmation.html`)<br>The page where users get a confirmation message if they really wish to delete this recipe.

- **Page 404** (`page_404.html`)<br>The page that informs users, that the page they are looking for is not found and takes them back to *Home* page safely. 

Recipe cards and full recipes are accessible by any users. Recipe cards are available on *Home* on the carousel and *Recipe* pages and full recipes are available on *Recipe* page.

<br>

## Skeleton Plane

It is a mobile-first website because people usually cook with a recipe so a good mobile-first design helps users whose main purpose is seeing recipes. For users whose main purpose is creating and posting recipes, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

### — Wireframes —

- [Wireframes: Home](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Landing-page.png)

- [Wireframes: Recipes](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Recipes-page.png)

- [Wireframes: Register](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Register.png)

- [Wireframes: Login](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Login.png)

- [Wireframes: Profile](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Profile-page.png)

- [Wireframes: Recipe Detail For a logged in User](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Recipe-detail-page-logged-in-user.png)

- [Wireframes: Recipe Detail For a Regular non-logged in User](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Recipe-detail-page-reg-user.png)

- [Wireframes: Add Recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Upload-page.png)

- [Wireframes: Edit Recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/Edit-recipe-page.png)


## Surface Plane

— **Colour** —

As this is a recipes website, I kept the colour scheme simple as I wanted to main focus to be on the recipe images
The background image selected is to imitate a marble kitchen countertop and the recipe images do all the work as they are the main focus. All the images used are the original recipe images.

— **Typography** —

<br>

[^ back to top ^](#Table-of-contents)
<br>

# FEATURES

## — Existing Features —
#### **Navigation menu displayed across all pages**

The navigation menu will help the user move easily across all pages.

The navigation buttons update depending on whether a user is logged in, and whether that user is the admin:

| Nav Link              |Not logged in  |Logged in as user
|:-------------         |:------------- |:------------- 
|Home                   |&#9989;        |&#9989;        
|Recipes                |&#9989;        |&#9989;        
|Register               |&#9989;        |&#10060;        
|Profile                |&#10060;       |&#9989;        
|Log Out                |&#10060;       |&#9989;             
|Log In                 |&#9989;        |&#10060;       

#### **Carousel displayed on home page for browsing the various 'recipes'** 

The carousel will allow the user to browse through the different recipes. This adds a more visual element rather than static images. All of the carousel images will link the user to the recipe page of their choosing. 

#### **All recipes accessible to users who don't want to make an account**

As someone who doesn't particularly like to sign up to websites that I don't plan on adding to but like to view, I wanted to make all of the recipes accessible to a casual viewer. But in order to interact with the site, they Do have to have an account. Without one, the option to upload anything isn't available. 

#### **Users can search for recipes based on an ingredients**

Searching by ingredient is an important feature for any recipe website so that was something that I wanted to include.  

#### **Pagination on recipe pages**

At the moment, the database is relatively small. But if this were a site that was going into full production, the recipes list would be much more extensive. As a result, the number of recipes displyed to the user could become overwhelming very quickly. I've limited to number of recipes per page - there's still a good amount displayed to the user without being too much. This will also help reduce loading times, especially on mobile devices. 


#### **User account management**

Anyone is able to make an account through the 'Register' page. They have to choose a username and a password. Users cannot choose a username that is already taken and they cannot use just whitespace.

Once their account is made, they will be able to log in an out when needed. 

#### **User recipe management**

A registered user is able to upload recipes to the site. Once they have recipes that they have added, all recipe management can be done from their account page. This includes editing a deleting.  

  + **Deleting**: there is a confirmation message in place to assure the user doesn't accidentally delete the recipe. 

#### **Recipe Images**

When uploading a recipe, the user needs to add an image alongside the recipe information. This image will be used on both the recipe card and on the full recipe page. But because the image is added via a url, there are some people who don't was to go to have to do this, or they simply can't on their device. As a result of that I have added a placeholder image url that the user can use in place of their own. It's a stylish image that was found on [Unsplash](https://unsplash.com/) that looks good with the overall feel of the site. 


#### **Admin  management**

Admin manages all its CRUD functionality from the backend.

#### **404 page**

Should a user request a page that does not exist they will receive a 404 message and be redirected back to the home page.

## — Features to Implement in the future —
+ A rating system that allows users to rate each others recipes. 
  + This could lead to sorting by top-rated recipes.
+ Ability to 'save' recipes to a users own account to refer back to.
+ Users ability to update username. 
+ Users ability to delete their account. 
  + This could allow the user to either leave their recipes on the site or delete them along with the account 
+ Resetting Password When Users Forget It.
+ “Like” Reaction By Other Users. I ran out of time to implement this feature and decided to leave it out

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Database

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. 
Cloudinary is used to for all images both by the superuser and a standard user for all images uploaded to the website.
<br>
The database contains three custom models - categories recipes and comments. The built in Django user model was utilized and each model liked to this. Each registered user is assigned a user id. They can add recipes which will be linked to their id, and each recipe has an auto generated slug field (this is derived from the recipe's title). The recipe can be edited and deleted by the person who added it only. 

Below is the chart of the custom data model used.

![database](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/database%20models.png)<br>

### Recipes

+ This model stores the recipe details that the user can view from the site
+ This model pulls information from the categories model to catagorize the type of recipe
+ This model pulls information from the comments model to determine who made the comment on what recipe

### Categories

+ This model stores the product category details
+ This model sends information to the recipes model to catagorize the type of recipe being uploaded

### Comments

+ This model stores the user name
+ This model sends information to the recipe model to determine who made the comment on which recipe

# Technologies Used

- [Django3](https://www.djangoproject.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Postgressql](https://www.postgresql.org/) for the database
- [Bootstrap 5 ](https://mdbootstrap.com/) for the mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Cloudinary](https://cloudinary.com/) for images
- [Summernote](https://summernote.org/) editor for adding and editing the recipes
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website


## General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

## Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Tinypng](https://tinypng.com/) for resizing images
- [Tinypng](https://tinypng.com/) for resizing images
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

***

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](https://github.com/moirahartigan/lets-cook-it/blob/main/TESTING.md). 

# Deployment
## — Deployment through GitHub Pages —
This site was deployed through GitHub Pages using the following steps:

* Log into GitHub.
* Locate the repository.
* Click the "settings" option along the options bar.
* Then go to "Pages" tab in the left hand side sidebar.
* Then under "Source" click the "None" dropdown and select the "Main" branch
* Click the save button.

## — Heroku Deployment —
This project was deployed through Heroku using the following steps:

### Step. 1 Installing Django and supporting libraries

Heroku needs to know which technologies are being used and any requirements, so the following commands were used in the Terminal in GitPod:
+ In the GitPod terminal, type ```pip3 install django gnuicorn``` to install django and gunicorn.
+ In the GitPod terminal, type ```pip3 install dj_database_url psycopg2``` to install the supporting libraries.
+ In the GitPod terminal, type ```pip3 install dj3-cloudinary-storage``` to install cloudinary libraries.
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ In the GitPod terminal, type ```django-admin startproject recipebook .``` to create your project. (Don't forget the .)
+ In the GitPod terminal, type ```python3 manage.py startapp lets_cook_it_app``` to create your requirements file.
#### In settings.py file:
+ In the settings.py file type ```lets_cook_it_app``` to create your requirements file.

### Step. 2 Deploying an app to Heroku
#### 2.1 Create the Heroku app:
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (lets_cook_it_app)
+ Select the appropriate region based on your location
+ Click 'Create App'
+ Add Database to App Resources - Located in the Resources Tab, Add-ons, search and add 'Heroku Postgres
+ Copy DATABASE_URL - Located in the settings Tab, in Config Vars, Copy Text

#### 2.2 Attach the Database:
#### In gitpod:
+ Create a new env.py file on the top level directory
#### In env.py file:
<br>

```
import os

os.environ["DATABASE_URL"] - "Paste in Heroku DATABASE_URL Link"
oos.environ["SECRET_KEY"] - "Make up a ramdom a randomSecretKey"
```

#### In heroku.com
+ Add Secret Key to Confid Vars

| Key                    | Value               |
| -------------          |:------------------- |
| SECRET_KEY             |*Secure secret key*  |
 
#### 2.3 Prepare our environment and settings.py file:
#### In settings.py:

+ Reference env.py

```
from pathlib import Path 
import os
import dj_database_url

if os.path.isfile("env.py"):
     import env

```
+ Remove the insecure secret key and replace - links to the secret key variable on Heroku

```
SECRET_KEY = os.environ.get('SECRET_KEY')

```

+ Replace DATABASES Section (comment out the old DataBases Section) - links to the DATABASE_URL variable on Heroku

```
DATABASES = {
     'default':
     dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

```
#### In the Terminal 
+ In the GitPod terminal, type ```python3 manage.py migrate``` to Make Migrations.

#### 2.4 Get our static and media files stored on Cloudinary:
#### In Cloudinary.com: 
+ Copy your CLOUDINARY_URL. eg. API Environment Variable copied from the Cloudinary Dashboard

#### In env.py: 
+ Add Clouldinary URL to env.py - be sure to paste in the correct section of the link

```
os.environ["CLOUDINARY_URL"] ="cloudinary://591333544891113:I7YqdHhfN01xRGjt55dcLywRks4@cloudmoira"

```

#### In Heroku.com:
+ Add Clouldinary URL to Heroku Config Vars - be sure to paste in the correct section of the link
+ Add DISABLE_COLLECTSTATIC to Heroku Config Vars **(temporary step for the moment, must be removed before deployment)**

| Key                    | Value               |
| -------------          |:------------------- |
| CLOUDINARY_URL         |cloudinary://5913333 |
| DATABASE_URL           |postgres://bxctnwwfx |
| SECRET_KEY             |*Secure secret key*  |
| DISABLE_COLLECTSTATIC  |1                    |

#### In settings.py:
+ Add Cloudinary Libraries to installed apps **(note: the order is important)**

```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',

```
+ Tell Django to use Cloudinary to store media and static files *Place under the static files*

```
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

```
+ Change the templates directory to TEMPLATES_DIR *Place within the TEMPLATES array*
+ Link file to the templates directory in Heroku *Placeunder the BASE_DIR line*

```
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

```

+ Add Heroku Hostname to ALLOWED_HOSTS

```
ALLOWED_HOSTS = ["lets-cook-it-app.herokuapp.com", "localhost"]

```

#### In Gitpod:
+ Create 3 new folders on the top level directory ```media, static, templates```
+ Create a Procfile on the top level directory also ```Procfile```

#### In the Procfile:
+ Add the following code ```web: gunicorn recipebook.wsgi```

#### In the Terminal 
+ Add ```git add .```
+ Commit ```git commit -m "Deployment Commit```
+ Push ```git push```

#### In Heroku.com:
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this
+ Underneath, locate 'Manual Deploy'; choose the main branch and click 'Deploy Branch'
+ Once the app is built (it may take a few minutes), click 'Open App' from the top of the page

## — Forking the Repository —
+ Log in to GitHub and locate the GitHub Repository
+ At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
+ You will have a copy of the original repository in your GitHub account.
+ You will now be able to make changes to the new version and keep the original safe. 
## — Making a Local Clone —
+ Log into GitHub.
+ Locate the repository.
+ Click the 'Code' dropdown above the file list.
+ Copy the URL for the repository.
+ Open Git Bash on your device.
+ Change the current working directory to the location where you want the cloned directory.
+ Type ```git clone``` in the CLI and then paste the URL you copied earlier.
+ Press Enter to create your local clone.

<br>

[^ back to top ^](#Table-of-contents)
<br>

# Credits
### Code
* The Code Institute material was the main source of information used to create this project.
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [MND Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) was used as a general source of knowledge.
* [youtube](https://www.youtube.com/watch?v=44axq8Absis) This tutorial was used to learn how to achieve a transparent navigation bar.
* [Stack Overflow](https://stackoverflow.com/) was used to assist during debugging.
* [Django docs](https://docs.djangoproject.com/en/3.2/) django documentation.
* [github docs](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) and (https://www.youtube.com/watch?v=3SKjPppM_DU) was used to create the 404 page.
* [geeksforgeeks](https://www.geeksforgeeks.org/) Many tutorials were followed for learning about building the django app (views - urls - template). Especially the generic views (CreateView, DeleteView, UpdateView)
* [codeamemy.com](https://www.youtube.com/watch?v=m3efqF9abyg&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=4) Tutorial was used to better understand how views and urls work.

### Media
* The Hero image was sourced from the following:
     * [unsplash](https://unsplash.com)
* The 404 page error image was sourced from the following:
     * [unsplash](https://www.freepik.com/free-vector/oops-404-error-with-broken-robot-concept-illustration_7906233.htm#page=1&query=404&position=24&from_view=search)
 * The recipe images were all taken from the original recipes which have been linked on the site in each recipe.
 * Each recipe is referenced to it source via the recipe_url and is available to all users from the redipe detail page

### Acknowledgements
* I would like to thank the Slack Community for their endless support.
* I would like to thank Kasia Bogucka our class cohort facilitator for her constant assistance and encouragement.
* I would like to especially thank two of my fellow students Siobhan and Laura for their help and motivation throughout this project.
* I would like to thank my husband for his understanding and support and for caring for our young children during the long hours taken to complete this project. 
* Finally, I would like to thank my mentor for his guidence and feedback throughout this milestone project.
 
***
