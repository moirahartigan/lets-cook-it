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

Even without being logged in, a user is able to browse through all the recipe cards, choose one and view the full recipe:

![testing from user stories]([#4](https://github.com/moirahartigan/lets-cook-it/issues/4))
[[#4](https://github.com/moirahartigan/lets-cook-it/issues/4)]
---

+ *I want to be able to search for specific recipes.*
+ *I want to be able to search for recipes that have a specific ingredient.*

From the recipes page, the user can use the search bar for specifics:

![testing from user stories](static/images/README/Testing/testing-02.png)

The words searched will come from the cocktail name, main ingredient and full ingredients list. 

If there were any results, the user will see just them:

![testing from user stories](static/images/README/Testing/testing-02-a.png)

If there were no matches, the user will be shown a message informing them:

![testing from user stories](static/images/README/Testing/testing-02-b.png)

The user can then use the use the clear button to revert back to seeing all recipes. 

---

+ *I want to have a varied range of cocktails.*

The recipes page gives the user the ability to browse through all of the recipes on the site, regardless of which collection it belongs to:

![testing from user stories](static/images/README/Testing/testing-03.png)

---

+ *I want to have a some cocktail suggestions when I'm not sure what to look for.*

On the home page, the carousel will give the user various collections to scroll through. Each image is a link to the appropriate collection page:

![testing from user stories](static/images/README/Testing/testing-04.png)

---

+ *I want to have the option to register an account if I want to come back at a later date.*

From the navigation bar, the user can go to the registration page. From there, they can choose a username and password:

![testing from user stories](static/images/README/Testing/testing-05.png)

 If their chosen username has already been taken, they will be informed and can choose another:

 ![testing from user stories](static/images/README/Testing/testing-05-a.png)

---

### As a returning user: 
+ *I want to be able to log into my account.*

As long as the user has been through the registration process, they can use the long in page from the navigation bar to access their account:

![testing from user stories](static/images/README/Testing/testing-06.png)

If they use the wrong username or password, they will be informed and can retry:

![testing from user stories](static/images/README/Testing/testing-06-a.png)

---

+ *I want to be able to upload a recipe.*

From their account page, the use will see the upload button towards the top of the page:

![testing from user stories](static/images/README/Testing/testing-07.png)

Once they have clicked it, they will be redirected to the upload page:

![testing from user stories](static/images/README/Testing/testing-08.png)

---

+ *I want to be able to add a recipe to the pre-determined collections.*

Once the user has been directed to the upload page, the first option is to choose which categories they would like their recipe to be added to:

![testing from user stories](static/images/README/Testing/testing-09.png)

---

+ *I want to have ease of access to any recipes that I have already uploaded.*

From their account page, the user will be able to view all recipes that they have uploaded:

![testing from user stories](static/images/README/Testing/testing-10.png)

---

+ *I want to be able to edit or delete any recipes that I have already uploaded.*

From the account page, a logged in user has access to all of their recipes. From there, the user can hover over any of the recipes and they are presented with the edit or delete options:

![testing from user stories](static/images/README/Testing/testing-11.png)

**EDIT:**
if the user presses the edit button, the page reloads to the edit page which is a visual duplication of the upload page. However, the input fields will be populated with their original input:

![testing from user stories](static/images/README/Testing/testing-12.png)

Once the user has made the necessary changes, they can save them at the bottom of the page. Alternatively, they can cancel all changes they've made. Both buttons lead back to their account page:

![testing from user stories](static/images/README/Testing/testing-13.png)

**Delete:** if the user chooses the delete button, they will be presented with a modal to either confirm or cancel the deletion: 

![testing from user stories](static/images/README/Testing/testing-14.png)

---

### As the site owner/admin:
+ *I want to be able to add new collections to the site.*

The admin will be able to log into their account as every other user does. However, they will have the 'Manage Collections' link in the nav bar:

![testing from user stories](static/images/README/Testing/testing-15.png)

Once they're on the 'Manage Collections' page, they'll have access to the 'Add Collection' button:

![testing from user stories](static/images/README/Testing/testing-16.png)

Once they click that, they'll be redirected to the upload page where they can fill in all of the collection information. The tool tips will give them information about the input elements:

![testing from user stories](static/images/README/Testing/testing-17.png)

Once all of the inputs have been filled in correctly, the user can use the 'Add Collection' button at the bottom of the page to add it to the database:

![testing from user stories](static/images/README/Testing/testing-18.png)

---

+ *I want the new collection to be added to the appropriate site areas.*

The new collection is added to the nav bar (and side nav):

![testing from user stories](static/images/README/Testing/testing-19.png)

The new collection is added to the home page carousel:

![testing from user stories](static/images/README/Testing/testing-20.png)

The new collection has its own page created:

![testing from user stories](static/images/README/Testing/testing-21.png)

---

+ *I want to be able to edit the pre-existing collections.*

From the 'Manage Collections' page, the admin can hover/click on whichever collection they wish to edit and click the 'Edit' button:

![testing from user stories](static/images/README/Testing/testing-22.png)

This will redirect them to the edit page where they can update whatever information they want. The only thing they can't update is the collection name:

![testing from user stories](static/images/README/Testing/testing-23.png)

Once the user has updated the information, they can access they buttons at the bottom of the form. If they click 'Edit Collection', the changed will be sent to the database and be updated across the site. They also have the option to 'Cancel' which will ignore any changes and redirect them to the 'Manage Collections' page:

![testing from user stories](static/images/README/Testing/testing-24.png)

---

+ *I want to be able to delete any collections.*

From the 'Manage Collections' page, the admin can hover/click on whichever collection they wish to edit and click the 'Delete' button:

![testing from user stories](static/images/README/Testing/testing-25.png)

A modal will appear asking the admin to confirm that they want to delete the collection. They also have the option to 'Cancel' which will close the modal with no changes made:

![testing from user stories](static/images/README/Testing/testing-26.png)

