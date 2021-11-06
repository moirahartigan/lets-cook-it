# Full Testing
## Contents
+ [Testing User Stories](#testing-user-stories)
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)

---
---
## Testing User Stories
### As a casual user: 
+ *I want to be able to view recipes without having to register and account.*

Even without being logged in, a user is able to browse through all the recipe cards, choose one and view the full recipe
users can brouse recipes either on the home page carousel:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/carousel.png)

And also on the recipes page: 

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/casual-user-recipe-page.png)

---

+ *I want to be able to search through the recipes on the site.*
+ *I want to be able to search for recipes that have a specific ingredient.*

From the recipes page, the user can use the search bar:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/search.png)

The words searched will come from the full ingredients list. 

If there were any results, the user will see just them:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/search-results.png)

If there were no input in the search box, the user will be shown a message informing them:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/search-no-input.png)

The user can then use the use the back button to revert back to seeing all recipes. 

---

+ *I want to be able to register for an account if I want to come back at a later date.*

From the navigation bar, the user can go to the registration page. From there, they can choose a username and password:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/register-pg.png)

---

+ *I want to be able to able to view a specific number of recipe cards on the recipe page so that only a number of recipe card appear at a time on the page.*

Pagination has been added to the recipe page to enhance the user experience and allow them to easily move from page to page when viewing the recipes:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/page-pagination.png)

---

### As a registered user: 
+ *I want to be able to log into my account.*

As long as the user has registered for an account, they can use the log in page from the navigation bar to access their account:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/login%20pg.png)

---

+ *I want to be able to upload a recipe.*

From their account page, the user will see the add recipe button towards the top of the page:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/add-recipe-button.png)

Once they have clicked it, they will be redirected to the add a new recipe page:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/add-recipe-form.png)

---

+ *I want to have ease of access to any recipes that I have already added.*

From their account page, the user will be able to view all recipes that they have added:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/profile-page.png)

---

+ *I want to be able to view, edit or delete any recipes that I have already added.*

From the account page, a logged in user has access to all of their recipes. From there, the user have a button choice to view, edit or delete any recipe:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/view-edit-delete-buttons.png)

**EDIT:**
if the user presses the edit button, the page reloads to the edit page which is a essentially a duplication of the add a new recipe page. However, the input fields will be populated with their original input:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/edit-recipe-form.png)

Once the user has made the necessary changes, they can save them at the bottom of the page. 

**Delete:** if the user chooses the delete button, they will be presented with a message to either confirm or cancel the deletion: 

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/delete-confirm.png)

---

+ *I want to be able to add a comment to other recipes.*

logged in users can view and add comments to all other recipes, this feature is not available to casual users:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/registered-user-comments.png)

---

### As the site owner/admin:
+ *I want to be able to add new recipes to the site.*

From the back end Django admin planel a superuser such as admin has the ability to log in:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin%20login.png)

Once they're logged in admin can add new recipes in a simular format as the front end user:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-recipe-panel.png)

Once they click add recipe, they'll be redirected to the upload page where they can fill in all of the recipe information. The summernote editor has been used here to allow admin to style the layout as they wish:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-add-recipe.png)

Once all of the inputs have been filled in correctly, the user can use the 'save' button at the bottom of the page to add it to the database:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-save-button.png)

---

+ *I want to be able to edit the pre-existing recipes.*

From the admin page, the admin can select any recipe they wish to edit it:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-edit-recipe.png)

This will redirect them to the edit page where they can update whatever information they want:

---

+ *I want to be able to approve any recipe.*

From the admin page, the admin can select new recipes recently added by a registered user and make them available for casual users:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-approve-recipes.png)

---

+ *I want to be able to delete any recipe.*

From the admin page, the admin can select any recipe to delete it:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-delete.png)

---

+ *I want to be able to approve comments left by registered users.*

From the admin page, the admin can select the comments and review and approve the comments as the are made:

![testing user stories](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/testing-user-stories/admin-approve-comments.png)

---

<br>

[^ back to top ^](#contents)
<br>


## Validator Testing
### **HTML**

 I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)

 Because of the presence of Django within the code, I had to check from the live site by right clicking each page, selecting View Page Source and running that generated code through the validator.

 All pages passed all checks with the exception of those pages containing recipes copied and pasted directly from another website

<details>
<summary>Show validators</summary>
<details>
<summary>Home Page</summary>

![home page](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/Home-page-validation.png)
</details>

<details>
<summary>Add Recipee</summary>

The errors shown relate to the summer note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/add-recipe-page-validation.png)
</details> 

<details>
<summary>Edit Recipe</summary>

Again here the errors shown relate to the sunner note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/edit-recipe-page-validation.png)
</details> 

<details>
<summary>login page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/login-page-validation.png)
</details>

<details>
<summary>Logout page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/logout-page-validation.png)
</details> 

<details>
<summary>Recipe page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/recipes-page-validation.png)
</details>

<details>
<summary>Profile page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/profile-page-validation.png)
</details> 

<details>
<summary>Recipe detail page</summary>

Again here the errors shown relate to the sunner note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/recipe-detail-page-validation.png)
</details>

<details>
<summary>Register Recipe</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/register-page-validation.png)
</details>
</details>  
<br>

 ---


### **CSS**

I checked the CSS file using [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/)

![css validator](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/css-validation.png)

### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/)



### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks bar url.py as one of the path line was too long by 3 charactors. Splitting this paths caused issues on the live site so I left the line length as it was.

---


## Lighthouse Testing

![mobile lighthouse score](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/lighthouse-mobile.png)

![desktop lighthouse score](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/lighthouse-desktop.png)

---

<br>

[^ back to top ^](#contents)
<br>

## Manually Testing Functionality
### **base.html**

| Element               | Action        | Expected Result| Pass/Fail  |
|:-------------         |:------------- |:-----|:-----|
| **NavBar**            |               |      |
|Recipes Link           |Click|Redirect to all recipes  |Pass|
|Register Link          |Click|Redirect to register page|Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log In Link            |Click|Redirect to log in page  |Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log Out Link           |Click|Log user out of account  |Pass|
|                       |Click|Redirect to log in page  |Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Profile Link           |Click|Redirect to account page|Pass|
|                       |     |(Only visible if user in session)  |Pass|
|Manage Collections Link|Click|Redirect to manage collections page|Pass|
|                       |     |(Only visible if admin in session) |Pass|
| **SideNav**           |       |    |
|Hamburger Icon         |Click|Open Sidenav             |Pass|
|Recipes Link           |Click|Redirect to all recipes  |Pass|
|Register Link          |Click|Redirect to register page|Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log In Link            |Click|Redirect to log in page  |Pass|
|                       |     |(Not visible if user in session)  |Pass|
|Log Out Link           |Click|Log user out of account  |Pass|
|                       |Click|Redirect to log in page  |Pass|
|                       |     |(Only visible if user in session)  |Pass|
|profile Link           |Click|Redirect to account page|Pass|
|                       |     |(Only visible if user in session)  |Pass|
| **Footer**            |     |     |
|Facebook Link          |Click|Open on external page    |Pass|
|Twitter Link           |Click|Open on external page    |Pass|
|Instagram Link         |Click|Open on external page    |Pass|
|Github Link            |Click|Open on external page    |Pass|

---

### **index.html**
| Element               | Action            | Expected Result           | Pass/Fail  |
|:-------------         |:-------------     |:-----                     |:-----|
| **Carousel**          |                   |                           |    |
|Carousel               |Horizontal scroll  |Scroll through recipes     |Pass|
|Register Link          |Click              |Redirect to register page  |Pass|
|Log In Link            |Click              |Redirect to log in page    |Pass|

---

### **profile.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Add Recipe Btn**        |                   |                                   |    |
|Add Recipe Button          |Click              |Redirect to recipe add recipe page |Pass|
| **Recipe Card**           |                   |                                   |    |
|Recipe Card                |On page open       |Display recipe action buttons      |Pass|
|View recipe btn            |Click              |Redirect to full recipe            |Pass|
|Edit recipe btn            |Click              |Redirect to edit recipe page       |Pass|
|Delete recipe btn          |Click              |Open delete confirmation modal     |Pass|
|Delete msg - confirm btn   |Click              |Delete selected recipe             |Pass|
|                           |                   |'Recipe deleted' confirmation msg  |Pass|
|Delete msg - cancel btn    |Click              |Close message with no change made  |Pass|
| **Pagination**            |                   |                                   |    |
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific page number               |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|

---

### **recipe_form.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|Text input fields          |Type into          |Text appears,                      |Pass|
|Text input fields          |Leave blank        |Line highlights red                |Pass|
|Categories choice          |Dropdown list      |list of categories appear          |Pass|
|Summernote editor          |Click              |Text can be edited/formated        |Pass|
|Upload btn                 |Click              |Recipe appears on profile page     |Pass|
|                           |                   |Redirect to Profile page           |Pass|

---
### **recipe_edit_form.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|All fields                 |On page open       |Pre-populated with previous inputs |Pass|
|Text input fields          |Type into          |Text appears                       |Pass|
|Upload btn                 |Click              |Recipe appears on profile page     |Pass|
|                           |                   |Redirect to recipe page            |Pass|

---

### **recipe_detail.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|Edit button                |Click              |displayed if user is recipe owner  |Pass|
|Delete button              |Click              |displayed if user is recipe owner  |Pass|
|Recipe image               |On page open       |Recipe image displayed properly    |Pass|
|Recipe ingredients list    |On page open       |Recipe ingredients list displayed properly |Pass|
|Recipe method list         |On page open       |Recipe method list displayed properly  |Pass|
|Comments                   |On page open       |only if user is registered/logged in   |Pass|


---
### **login.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Form**                   |                   |                                   |    |
|Username                   |Text input         |Text displayed to user             |Pass|
|Password                   |Text input         |Password hidden to user            |Pass|
|Submit btn (fields correct)|Click              |Redirect to profile page           |Pass|
|Submit btn (fields incorrect)|Click            |error message to try again         |Pass|
|**Redirect Link**          |                   |                                   |    |
|'Register here' link       |Click              |Redirect to registration page      |Pass|

---
### **recipes.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Search**                 |                   |                                   |    |
|Text input                 |Text input         |Text displayed to user             |Pass|
| **Recipe Card**           |                   |                                   |    |
|Recipe Card                |On page open       |Reveal recipe action buttons       |Pass|
|View recipe btn            |Click              |Redirect to full recipe            |Pass|
| **Pagination**            |                   |                                   |    |
|Last btn                   |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|Next btn                   |Click              |Reveal 'next' recipes              |Pass|

---
### **register.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
|**Form**                   |                   |                                   |    |
|Username                   |Text input         |Text displayed to user             |Pass|
|Email address              |Text input         |Text displayed to user             |Pass|
|Password                   |Text input         |Password hidden to user            |Pass|
|Password (again)           |Text input         |Password hidden to user            |Pass|
|**Register btn**           |                   |                                   |    |
|Fields correct             |Click              |New user added to database         |Pass|
|                           |                   |Redirect to account page           |Pass|
|Fields incorrect format    |Click              |Fields highlighted red, user prompted to change format |Pass|
|Username already in use    |Click              |Reload register page, error message to user    |Pass|
|**Redirect Link**          ||||
|'Log in here' link         |Click              |Redirect to log in page            |Pass|

---

<br>

[^ back to top ^](#contents)
<br>

---

## Responsive Testing

Family and friends assisted me with real world testing on their personal devices and overall their feedback was quite positive. The site is easy to read and very intuitive. The forms are straight forward and easy to complete for registration, login adding and editing recipes. Users reported all links, navigation and functions work.

## For the Assessors

**_Please note, due to the time limitations on this project, was not able to add all the testing I wanted to. I Hope the testing that I currently documented, is sufficient_**. 

Thank you 😀

---

## Bugs and Fixes

When refactoring the code I was able to reduce the amout of pylint erros that were in the code. However, there are some that have been left in:

+ *Avoid using null=True on string-based fields such CharField*

The forms that I have in place sometimes need to allow for the fields to be left blank so I need to use null=true combined with blank=true

+ *line too long*

In the code that I have written, I have followed the line length rule. However, in Django generated files like migrations, I have left them as they were created. The migration files aren't generally going to be edited by humans so I feel comfortable leaving them as they are.

+ *'django.contrib.admin' imported but unused*

Not specific to 'django.contrib.admin' but to all imports in files that were created when the app was created and never used. I don't want to delete the files or their auto imports in case they're needed in the future. 

+ *Missing module docstring*

I have added docstrings to the views.py. I didn't add them to the models or forms files because:
1. They tended to be smaller than the views
2. The information on the pages was very self explanitory than the views

+ When registering for a profile, users who enter an email address get a 500 server request. I fixed this bug by truning off the email varification.

+ When a user was adding a recipe the slug field was not auto generating as in the admin panel, I fixed this by add slugify to the model for front end users. 

+ When I first attempted to run my final deployment to heroku I was getting a server 500 error and after checking every line of code in the setting.py file I finally discovered an additional comma  ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ] ,``` which I removed and this resolved the issue.


### Known Bugs

+ I attempted to style the summernote editor however I was unable to override the iframe for dexktop view and there is an overflow of a white box on the page. I kept the form background neutral to to make the issue as subtle as possible.   
---

<br>

[^ back to top ^](#contents)
<br>