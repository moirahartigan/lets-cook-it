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

![testing user stories](admin-save-button)

---

+ *I want to be able to edit the pre-existing recipes.*

From the admin page, the admin can select any recipe they wish to edit it:

![testing user stories](admin-edit)

This will redirect them to the edit page where they can update whatever information they want:

---

+ *I want to be able to delete any recipe.*

From the admin page, the admin can  select any recipe they wish to edit it:

![testing user stories](admin-delete)

---

+ *I want to be able to approve comments left by registered users.*

From the admin page, the admin can select the comments and review and approve the comments as the are made:

![testing user stories](admin-comments)

---
