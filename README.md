# Lets Cook It!
## **Code Institute - Portfolio Project 4: _Full-Stack Toolkit_** 
Lets Cook It! is a virtual recipe collection where all your favourite recipes can be saved in the one place.

It is a community based experience that allows casual, one-time users to browse recipes, and allows returning users to create profiles and upload and manage recipes.
## Demo

[View the Live Website Here]()

<img src="https://github.com/moirahartigan/Ms1-Schools-Out-Childcare/blob/master/readme/am-i-responsive.png">


### Table of contents
1. [UX](#UX)
     1. [Project Goals](#Project-Goals)
     2. [User Stories](#User-Stories)
     3. [Project Planning](#Project-Planning)
2. [Data Schema](#Data-Schema)
     1. [Users Collection](#Users-Collection)
     2. [Recipes Collection](#Recipes-Collection)
     3. [Categories Collection](#Categories-Collection)
3. [Features](#Features)
     1. [Design Features](#Design-Features) 
     2. [Existing Features](#Existing-Features)
     3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Languages](#Languages)
     2. [Tools](#Tools)
     3. [Libraries](#Libraries)
     4. [Database Management](#Database-Management)
6. [Testing](#Testing) ☞ **[Testing.md](TESTING.md)**
7. [Deployment](#Deployment)
     1. [1. Database Creation](#1-Database-Creation)
     2. [2. Local Copy Creation](#2-Local-Copy-Creation)
     3. [3. Heroku App Creation](#3-Heroku-App-Creation)
8. [Credits](#Credits)
9. [Acknowledgements](#Acknowledgements)
10. [Technical Support](#Technical-Support)
***

### Project Goals
The primary goal of Lets Cook It! is to allow the users to create, save, search, and view their favorite recipes in one place. The goal for the design was to make it as easy as possible to access information, while striving for a minimalist and user-friendly design.

### User Stories
**As a Casual User, I want to:**

1. Easily find recipes on the database. 
2. View the recipe detail page to get additional information.

**As a Non-Registered User, I want to:**

1. Navigate to Registration page to Sign-up for an account.

**As a Registered User, I want to:**

1. Log into my account to gain access to the full functionality of the site.
2. Navigate to my recipes page to view my uploaded recipes.
3. Navigate to upload page to add my recipe to the database.
4. View and edit my recipes as needed.
5. View and delete my added recipes if I so wish.
6. Add a comment to another users recipe.

**As an Administrative Account holder, I want to:**

1. View **any** recipe to edit recipe as needed.
2. View **any** recipe to delete recipe as needed.
3. Approve recipe comments from registered users.
4. Approve user's uploaded recipes for public view.
5. Add and edit and delete recipe categories.


### Strategy Plane

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

> **Note:**<br>
> During the project, decide to add pagination as it makes the website much neater so it is implemented in the current project

### Scope Plane

To achieve user and owner’s goals, below are the minimum features to be included in this project. Also, **CRUD** Create, Read, Update, and Delete functions are required for this project so these are implemented as a part of essential features.

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

### Structure Plane

— **Front-end** —

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

— **Back-end** —<br>

The database was built with postgres and was used both locally in gitpod and deployed to a live site by heroku.
Cloudinary is used to for all images both by the superuser and a standard user for all images uploaded to the website.

The database contains three custom models - categories recipes and comments. The built in Django user model was utilized and each model liked to this. Each registered user is assigned a user id. They can add recipes which will be linked to their id, and each recipe has an auto generated slug field (this is derived from the recipe's title). The recipe can be edited and deleted by the person who added it only. 

<!-- Registered users can leave comments on any recipe and the comment will display their username. A registered user can choose to publish recipes so they are displayed on the public recipe page, or leave them as drafts so they will only be visible on their own profile page. -->

Below is the chart of the custom data model used.

![image]()<br>


### Skeleton Plane

It is a mobile-first website because people usually cook with a recipe so a good mobile-first design helps users whose main purpose is seeing recipes. For users whose main purpose is creating and posting recipes, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

- [Wireframes: Home]()

- [Wireframes: Recipes]()

- [Wireframes: Register]()

- [Wireframes: Login]()

- [Wireframes: Profile]()

- [Wireframes: Recipe Detail]()

- [Wireframes: Add Recipe]()

- [Wireframes: Edit Recipe]()






### Surface Plane

— **Colour** —

As this is a recipes website, I kept the colour scheme simple as I wanted to main focus to be on the recipe images

![image]()

— **Typography** —

**Amatic SC** is used for the main heading “Uncle Jam’s Baking Recipes” &#40;h1&#41; and headings of other pages &#40;h2&#41; because this handwritten type of font links with recipes (hand made) very well.

![image]()

**Balsamiq Sans**, which is also another type of handwritten font, is used for menu and other headings &#40;h3 - h6&#41; as it matches the image of the website well.

![image]()

**Nunito**, which is Sans Serif type font, is used for texts on the body to give users maximum readability.

![image]()


## WEBSITE CONSTRUCTION PLANS

This project contains both front-end and back-end so well-structured planning is required to do the work efficiently. Below is a summary of the plans.

1. Creating Database in Django
1. Installing necessary Python frameworks, creating a Python file for the app and testing functions
1. Deploying the website in Heroku
1. Connecting Database and App
1. Creating base HTML template with common sections e.g. header & footer
1. Creating *Register*, *Login*, *Profile* pages
1. Creating *Add*, *Edit* recipe pages
1. Creating an individual *Recipe* page
1. Creating a *Delete confirmation* page
1. Creating *404* page

Some testing is also done during the above process


## FEATURES

### Existing Features

- 

### Features Left To Implement

- **Resetting Password When Users Forget It:** To achieve this, an e-mail address is probably required for creating an account. The current primary purpose of the website is to provide easy access to the platform so do not ask e-mail address to create an account. In addition, do not know how to implement this with my current skills, decide to leave this out

- **“Like” Reaction By Other Users:** Do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out



## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Material Design for Bootstrap 5 & 4](https://mdbootstrap.com/) &#40;an open-source toolkit based on Bootstrap for developing Material Design&#41; for the mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Flask](https://flask.palletsprojects.com/) &#40;a micro web framework written in Python&#41; as the main framework of Python
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment &#40;IDE&#41;
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website



## RESOURCES

### General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

### Tools

- [Balsamiq](https://balsamiq.com/) for wireframes
- [Adobe](https://www.adobe.com/ie/photoshop/online/resize-image.html) for resizing images
- [PNG to ICO](https://hnet.com/png-to-ico/) for converting png to ico for favicon
- [removebg](https://www.remove.bg/) for removing background images
- [Transparent Textures](https://www.transparenttextures.com/) for creating background image
- [Canva](https://www.canva.com/) for creating logos and some images
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php) for mockup
- [Autoprefixer](https://autoprefixer.github.io/) for parsing CSS and add vendor prefixes
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

















***
# Testing
### Validator Testing
At the completion or heavy editing of sections, I used the following to check my code for syntax errors:


#### <em>HTML Validator</em>

  <p align="center">  
 <img src=""> 
 </p>
  
  
* The warning returned from the html validator identified the navigation section was lacking a heading - however a business logo was used in place of a heading for this section. 
#### <em>CSS Validator</em>

  <p align="center">  
  <img src="
  ">
 </p>
    
    
* All pages came back with no errors.
 
### Lighthouse Testing
I used Chromes Lighthouse tools to test the site's performance. I made sure to check both desktop and mobile performances. Below are the screenshots from both tests:
#### <em>lighthouse Mobile</em>
![Mobile]()
#### <em>lighthouse Desktop</em>
![Desktop]()
***
# Deployment
### Deployment through GitHub Pages
This site was deployed through GitHub Pages using the following steps:

* Log into GitHub.
* Locate the repository.
* Click the "settings" option along the options bar.
* Then go to "Pages" tab in the left hand side sidebar.
* Then under "Source" click the "None" dropdown and select the "Main" branch
* Click the save button.
* The page will update and at the top it will say: "Your site is ready to be published at
* ()

# Credits
### Code
* The Code Institute material was the main source of information used to create this project.
* [Bootstrap](https://getbootstrap.com/) for creating a responsive site.
* [w3schools](https://www.w3schools.com/) was used as a general source of knowledge 
* [MND Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-direction) was used as a general source of knowledge.
* [youtube](https://www.youtube.com/watch?v=44axq8Absis) This tutorial was used to learn how to achieve a transparent navigation bar.
* [Stack Overflow](https://stackoverflow.com/) was used to assist during debugging.
* [github docs](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) was used to create the 404 page.

### Media
* Images were sourced from the following:
    * [unsplash](https://unsplash.com)
    * [pexels](https://www.pexels.com)
    * [pixabay](https://pixabay.com/)
 * The site logo image was designed by myself Moira Hartigan with the use of [Free Logo Maker](https://logomakr.com/)

### Acknowledgements
* I would like to thank the Slack Community for their endless support.
* I would like to thank Kasia Bogucka our class cohort facilitator for her constant assistance and encouragement.
* Finally, I would like to thank my mentor Oluwafemi Medale for his guidence and feedback throughout this milestone project.
 
***
