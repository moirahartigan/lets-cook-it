# Full Testing
## Contents
+ [Testing User Stories](#testing-user-stories)
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
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

### As a returning user: 
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
---

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
<summary>Home Page</summary>

The errors shown relate to the summer note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/add-recipe-page-validation.png)
</details> 
<details>
<summary>Add Recipe</summary>

Again here the errors shown relate to the sunner note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/edit-recipe-page-validation.png)
</details> 
<details>
<summary>Edit Recipe</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/login-page-validation.png)
</details> 
<details>
<summary>login page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/logout-page-validation.png)
</details> 
<details>
<summary>Logout page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/recipes-page-validation.png)
</details> 
<details>
<summary>Recipe page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/profile-page-validation.png)
</details> 
<details>
<summary>Profile page</summary>

Again here the errors shown relate to the sunner note editor
![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/recipe-detail-page-validation.png)
</details> 
<details>
<summary>Recipe detail page</summary>

![add recipe](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/register-page-validation.png)
</details> 
<details>
<summary>Register Recipe</summary>


### **CSS**

I checked the CSS file using [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/)

![css validator](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/css-validation.png)

### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/)



### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

---
---


## Lighthouse Testing

![mobile lighthouse score](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/lighthouse-mobile.png)

![desktop lighthouse score](https://github.com/moirahartigan/lets-cook-it/blob/main/static/readme/validation/lighthouse-desktop.png)

---
---

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

### **Profile.html**

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

### add_recipe.html

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
### **edit_recipe.html**

| Element                   | Action            | Expected Result                   | Pass/Fail  |
|:-------------             |:-------------     |:-----                             |:-----|
| **Form**                  |                   |                                   |    |
|All fields                 |On page open       |Pre-populated with previous inputs |Pass|
|Text input fields          |Type into          |Text appears                       |Pass|
|Upload btn                 |Click              |Recipe appears on profile page     |Pass|
|                           |                   |Redirect to recipe page            |Pass|

---

### **full_recipe.html**

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
|<< btn                     |Click              |Reveal 'previous' recipes          |Pass|
|Pagination number          |Click              |Specific recipes page number       |Pass|
|>> btn                     |Click              |Reveal 'next' recipes              |Pass|

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
|                           |                   |Redirect to home page              |Pass|
|Fields incorrect format    |Click              |Fields highlighted red, user prompted to change format |Pass|
|Username already in use    |Click              |Reload register page, error message to user    |Pass|
|**Redirect Link**          ||||
|'Log in here' link         |Click              |Redirect to log in page            |Pass|

---
---