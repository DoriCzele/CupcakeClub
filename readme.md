# **The Cupcake Club**

![Mock up](/docs/mockup.png)

## **Goal for this project**
Welcome to [The Cupcake Club](https://cupcake-club.herokuapp.com)!

This website was created to allow visitors to write, share and find cupcake recipes. An online collection of various cupcake recipes that allows cupcake-lovers to browse, share, add or edit recipes, all wrapped into a fun and modern design.

The website has a user-friendly layout and provides easy access to all necessary information.

Thank you for visiting!

Should you have any questions regarding my project feel free to reach out to me via the provided GitHub contact details.

## Table of contents 
- [**The Cupcake Club**](#the-cupcake-club)
  - [**Goal for this project**](#goal-for-this-project)
  - [Table of contents](#table-of-contents)
  - [**UX**](#ux)
    - [User Goal](#user-goal)
    - [User Stories](#user-stories)
    - [Site Owner's Goals](#site-owners-goals)
    - [Design Choices](#design-choices)
    - [Colours](#colours)
    - [Structure](#structure)
    - [Logo](#logo)
    - [Background](#background)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Wireframes](#wireframes)
      - [Desktop Wireframes](#desktop-wireframes)
      - [Tablet Wireframes](#tablet-wireframes)
      - [Mobile Wireframes](#mobile-wireframes)
      - [Additional wireframes](#additional-wireframes)
  - [**Technologies used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Database Structure**](#database-structure)
    - [User Table Schema](#user-table-schema)
    - [Recipe Table Schema](#recipe-table-schema)
  - [**Testing**](#testing)
  - [**Testing User Stories**](#testing-user-stories)
    - [Applicable to all users](#applicable-to-all-users)
      - [Common to all devices](#common-to-all-devices)
      - [Mobile/Tablet only](#mobiletablet-only)
      - [Desktop only](#desktop-only)
    - [User that is not logged in](#user-that-is-not-logged-in)
    - [Common to logged in Member and Admin Users](#common-to-logged-in-member-and-admin-users)
    - [Logged in Admin User](#logged-in-admin-user)
  - [**Security**](#security)
  - [**Deployment**](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)
  - [**Credits**](#credits)


## **UX**

### User Goal
* A recipe collection containing information about how to make cupcakes.
* A fully responsive website that is accessible and easy to use on desktop, tablet & mobile.
* Appealing, modern and clear design.
* Visibility of my own recipes, and an easy way to edit or delete these.
* Providing option to share recipes on social media.
* Direct links to social media sites.

[Back to Top](#table-of-contents)

### User Stories
* As a user, I want to be able to register to the website so I can access write and submit my own recipes.
* As a user, I want to be able to log in with my account and access my previous recipes.
* As a user, I want a simple way to edit or delete my previous recipes.
* As a user, I want to be able to share recipes from the website on social media.
* As a user, I want to be able to access relevant social media links from the website, and expect these to open on separate tabs.
* As a user, I want to be able to see the most recent recipes first.
* As a user, I want text and images to appear clear and visible.
* As a user, I want the website to be easy to navigate.
* As a user, I want the website to be available on mobile, tablet and desktop devices.

[Back to Top](#table-of-contents)

### Site Owner's Goals
* Providing information about how to make cupcakes. 
* Providing a fully responsive and enjoyable interface with great functionality for users to write, share and find recipes.
* To make the website as personal as possible by giving the user the possibility to customise their recipe avatar and add and access their own recipes on a separated page.

[Back to Top](#table-of-contents)

### Design Choices
The website's main functionalities to add, share and find cupcake recipes. The design choices reflect a fun and modern design with bold colours while keeping the flow clear and simple for users. 

### Colours

![Colour Scheme](/docs/colour-palette.png)

The colour palette was created via [Coolors](https://coolors.co/ "Coolors.co")

* #FFFFFF: The background of the overall website is white in order achieve a clean nad modern look. 
* #7386C2: This colour is used as background colour in different sections. 
* #D63384: This color is used in the navbar and certain texts to draw user's attention to it.
* #2C3E50: This colour is used as a feature colour in dividers across the website as well as in the footer.

### Structure

The website's structure was created with the use of [Bootstrap 5](https://getbootstrap.com/) and a free template from [Start Bootstrap](https://startbootstrap.com/previews/freelancer) to ensure compatibility across various devices.

### Logo

The cupcake logo was created by [Tamas Barta](https://linkedin.com/in/tamas-barta-50850013a) Graphic Designer.

### Background

The background image is created via [Patternico](https://patternico.com).

### Fonts

Fonts are customised via [Google Fonts](https://fonts.google.com)

### Icons

Fav icons are created via [Favicon.io](https://favicon.io/favicon-generator/) 

[Back to Top](#table-of-contents)

### Wireframes

The website's wireframes were created via [Balsamiq](https://balsamiq.com/wireframes/).

Wireframes are available on the links below:

#### Desktop Wireframes
* [Home](/docs/wireframes/home_desktop.png)
* [Login](/docs/wireframes/login_desktop.png)
* [Register](/docs/wireframes/register_desktop.png)
* [Recipe form](/docs/wireframes/recipe_form_desktop.png)
* [Edit recipe form](/docs/wireframes/edit_recipe_desktop.png)
* [My recipes](/docs/wireframes/my_recipes_desktop.png)
* [Recipes](/docs/wireframes/recipes_desktop.png)
* [Recipe details](/docs/wireframes/recipe_details_desktop.png)

#### Tablet Wireframes
* [Home](/docs/wireframes/home_tablet.png)
* [Login](/docs/wireframes/login_tablet.png)
* [Register](/docs/wireframes/register_tablet.png)
* [Recipe form](/docs/wireframes/recipe_form_tablet.png)
* [Edit recipe form](/docs/wireframes/edit_recipe_tablet.png)
* [My recipes](/docs/wireframes/my_recipes_tablet.png)
* [Recipes](/docs/wireframes/recipes_tablet.png)
* [Recipe details](/docs/wireframes/recipe_details_tablet.png)

#### Mobile Wireframes
* [Home](/docs/wireframes/home_mobile.png)
* [Login](/docs/wireframes/login_mobile.png)
* [Register](/docs/wireframes/register_mobile.png)
* [Recipe form](/docs/wireframes/recipe_form_mobile.png)
* [Edit recipe form](/docs/wireframes/edit_recipe_mobile.png)
* [My recipes](/docs/wireframes/my_recipes_mobile.png)
* [Recipes](/docs/wireframes/recipes_mobile.png)
* [Recipe details](/docs/wireframes/recipe_details_mobile.png)

#### Additional wireframes
* [Error page](/docs/wireframes/error_wireframe.png)
* [Toast message](/docs/wireframes/toast_message.png)

[Back to Top](#table-of-contents)

## **Technologies used**
### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)

### **Tools**
* [GitHub](https://github.com)
* [VS Code](https://vscode.dev)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### **Database Structure**

"User" and "Recipe" collections were used in this project.

### User Table Schema

The structure of a document within this collection is as follows:  
| Title | Database Key | Data type |
--- | --- | ---
User ID | _id | ObjectId
Username | username | String
Hashed Password | password | String
Is Administrator | is_admin | Boolean

### Recipe Table Schema

The structure of a document within this collection is as follows:
| Title | Database Key | Data type |
--- | --- | ---
Recipe ID | _id | ObjectId
Recipe Name | name | String
Ingredients | ingredients | Array
Instructions | instructions | Array
Avatar Color | color | String
Author | author | string
Creation Time | created_at | Date

[Back to Top](#table-of-contents)

## **Testing**

The W3C Markup Validator and the W3C CSS Validator were used to validate the html and css files in the project and to ensure there were no syntax errors.  
ESLint was used to check the javascript files.  
Flake8 and Black were used to validate python files.

* **W3C Markup Validator for HTML5**

On the Recipes page there was an unclosed div, closing tag was added.
There were no other errors reported.
Comment: The SVG file was pre-generated from an adobe product therefore validation was deemed unnecessary.

* **W3C CSS Validator**

On the styles.css file there was an invalid value which has been removed.
There were no other errors reported.

* **ESLint** 

ESLint resolved quotation style inconsistency, missing semi-colons and unused variable definitions across all javascript files.
There were no other errors reported.

* **Flake8**

An unused import was detected and subsequently removed.
There were no other errors reported.

* **Black**

Black has detected and resolved line length and white space errors.
There were no other errors reported.

## **Testing User Stories**

The manual testing was carried out based on the User Stories to demonstrate key functions and features are fulfilled.

**CRUD functionality**

Users can upload their recipes via the recipe form (see below) on the "Add a recipe" for other users and visitors to view, fulfilling the "create" aspect of CRUD. 

![Recipe form](/docs/testing/recipe_form.png)

Users can read recipes on the "Recipes" page (see below) starting with the most recent recipe, fulfilling the "read" aspect of CRUD. Pagination was added to the "Recipes" and "My recipes" pages to enable improved data efficiency and enhance user experience by reducing loading time.

![Recipes](/docs/testing/recipes.png)

Users can update or delete their own recipes on the "My recipes" page by clicking on the edit or delete buttons in the detailed recipe view, fulfilling the "read" and "delete" aspects of CRUD. 

![Recipe details](/docs/testing/edit_delete_buttons.png)

After clicking the edit button the user is navigated back to the recipe form view (see below) where ingredients and instructions can be amended or removed. 

![Edit recipe](/docs/testing/edit_recipe.png)

The user's own recipes can be deleted in the  detailed recipe view by clicking the delete button then confirming by clicking it again. 

![Confirm delete](/docs/testing/delete_confirmation.png)

**Registration and Log in**

Users expect to be able to register to the website in order to share their own recipes, and access these at any time by logging in. Under the "Login/Register" button in the navbar a registration and log in form was implemented to fulfill this function (see below).

![Register/Login](/docs/testing/reg_login.png)

**Share functionality**

Users expect to be able to share recipes through social media, therefore a Facebook share button was implemented navigating the user to the correct share link in a new window.

**Social media links**

Relevant social media links are available in the footer, these are opening in separate windows.
  
**Design elements**

Users expect to be able to access information easily therefore a clear and easy to read design was implemented with added aria-labels for accessibility. The website design is fully responsive across all devices, this feature was tested on desktop, tablet and mobile. 

**Manual testing**

Manual testing was used to make sure all buttons and functions are fully functional. Cross-browser testing was carried out to ensure the website's functions work as desired across all applications. Browsers used for testing: Safari, Google Chrome, Firefox. Devices used for testing: mobile, tablet and desktop.  
All database interactions on the backend were tested with raised errors to ensure graceful handling and suitable feedback to the end user.  

### Applicable to all users
#### Common to all devices

✅ Given the user is using any device when accessing any page: then render the navigation bar with "Recipes", "Add A Recipe" and "About" links.  
✅ Given the user is using any device when accessing any page and activating the "Recipes" navigation item: then the user is redirected to view all preview recipe tiles in a paginated view.  
✅ Given the user is using any device when accessing the "Recipes" page when activating the pagination navigation buttons then redirect to the corresponding pagination page.  
✅ Given the user is using any device when accessing any page and activating the "Home" navigation item: then the user is redirected to the homepage.  
✅ Given the user is using any device when accessing any page and activating the "About" navigation item: then the user is redirected to the about section on the homepage.  
✅ Given the user is using any device when accessing any page: then render the footer with links to GitHub and LinkedIn of the product developer.  
✅ Given the user is using any device when accessing any page and activating the GitHub link in the footer: then open the developer's GitHub profile in a new tab.  
✅ Given the user is using any device when accessing any page and activating the LinkedIn link in the footer: then open the developer's LinkedIn profile in a new tab.  
✅ Given the user is on the recipes list page, when rendering a recipe preview: then the corresponding recipe avatar color and name is displayed.  
✅ Given the user is on the recipes list page, when activating a "Let's bake it" button: then redirect the user to the corresponding recipe detail page.  
✅ Given the user is on the detailed recipe view, when activating Share button: then share recipe on Facebook in a new tab.  
✅ Given the user is on the detailed recipe view, when activating Go to Recipes button: then redirect user to "Recipes" page.  
✅ Given the user is on any page, when an error occurs, then display "Error" page with the corresponding error code.  
✅ Given the user is on the "Error" page, when activating Go to homepage button, then redirect user to the homepage.  
✅ Given the user is on detailed recipe view, when clicking on author's name, then navigate to the author's recipes.  

#### Mobile/Tablet only

✅ Given the user is using a mobile/tablet when accessing any page: then the navigation bar is not expanded then display a burger icon in its place.  
✅ Given the user is using a mobile/tablet when accessing any page: then the navigation burger icon is activated the expand the navigation bar vertically to display all nav links.  

#### Desktop only

✅ Given the user is using a desktop when accessing any page: then render the navigation bar as a horizontal bar, without a burger icon.  


There are no other functional changes between devices when accessing the site as a specific user.  


### User that is not logged in

✅ Given the user is not logged in when accessing any page: then render the navigation bar with additional "Log in/Register" link and not "Logout".  
✅ Given the user is not logged in when accessing any page and activating the "Log in/Register" navigation link: then redirect the user to a login page.  
✅ Given the user is not logged in and accessing the "Login" page when submitting a form with incorrect credentials: then reload the page with an error toast message.  
✅ Given the user is not logged in and accessing the "Login" page when submitting a form with empty input fields: then reload the page with an error toast message.  
✅ Given the user is not logged in and accessing the "Login" page when submitting a valid form and the user is found in the database: then redirect to the home page and display a welcome toast message.  
✅ Given the user is not logged in and does not have an existing account when accessing the login page and activating the "Register" link: then redirect to a register page.  
✅ Given the user is not logged in and accessing the "Register" page when submitting a form with empty input fields: then reload the page with an error toast message.   
✅ Given the user is not logged in and accessing the "Register" page when submitting a form with invalid input (e.g. username is "ejhpw^!%3"): then reload the page with an error toast message.  
✅ Given the user is not logged in and accessing the "Register" page when submitting a form with a username that already exists in the database: then reload the page with an error toast message.  
✅ Given the user is not logged in and accessing the "Register" page when submitting a form with valid input: then create user in database, redirect to the homepage and display a welcome toast message.  


### Common to logged in Member and Admin Users

✅ Given the user is logged in when accessing any page: then render the navigation bar with additional "Log out" link and not "Login/Register".  
✅ Given the user is logged in when activating the "Log out" link: then remove the user from session, redirect to Homepage and display a confirmation toast message.  
✅ Given the user is logged in when accessing any page: then render the navigation bar with additional "My Recipes" link.  
✅ Given the user is logged in and does not have recipes when accessing "My Recipes" link: then display "There are no recipes here yet!" heading.  
✅ Given the user is logged in and has recipes when accessing "My Recipes" link: then display the user's own recipes in paginated preview.  
✅ Given the user is logged in when accessing any of their own recipes in detailed view render Edit and Delete buttons.  
✅ Given the user is logged in when activating the Delete button on their own recipes display confirmation button requiring confirmation click before deleting recipe from the database.  
✅ Given the user is deleting a recipe, when activating the confirm delete button: then remove the target recipe from the database and redirect to the recipes page.  
✅ Given the user is logged in when deleting their own recipe: then redirect to "Recipes" page with a confirmation toast message.  
✅ Given the user is logged in when activating the Edit button on any of their own recipes in detailed view: then redirect the user to an edit recipe form pre-populated with the chosen recipe's details.  
✅ Given the user is logged in when activating the Delete button on any of their own recipes in detailed view: then remove the recipe from the database and redirect the user to "Recipes" page.  
✅ Given the user is logged in when activating the "Add recipe" link: then redirect the user to the recipe form.  
✅ Given the user is logged in when inputting invalid values to the recipe form: then prevent form submission and display error toast message.  
✅ Given the user is logged in on the create recipe page with populated ingredients/instructions fields, when activating the Edit button: then make the corresponding field writable.  
✅ Given the user is logged in on the create recipe page with populated ingredients/instructions fields, when activating the Delete button: then remove the corresponding field.  
✅ Given the user is logged in when inputting valid values to the recipe form: then allow submission and display confirmation toast message.  


### Logged in Admin User

✅ Given the admin user is logged in, when on the detailed recipe view: then display edit and delete recipe buttons.  
✅ Given the admin user is on the edit recipe view, when submitting a valid recipe input: then update the target recipe record with the recipe input (retaining the original author's name) and redirect to that recipe's detail page with a confirmation toast message.  
✅ Given the admin user is on the detailed recipe view, when activating the delete recipe button: then display confirmation button requiring confirmation click before deleting recipe from the database.  


## **Security**

This project involves secret keys for the successful melding of GitHub, Heroku and MongoDB with the development environment. This was achieved via a local env.py that is listed in the .gitignore file and can be found in the repository as well as the password and database name.

All users are required to provide a password when they register which are hashed by using "generate_password_hash" from the werkzeug.security library. Hashed passwords are then checked against each other upon log in.

Admins have the ability to access, edit or remove any recipes. The Cupcake Club admins reserve the right to modify any recipes that are deemed inappropriate, irrelevant or offensive.

[Back to Top](#table-of-contents)

## **Deployment**

### Local Deployment

I have created The Cupcake Club using Github and VS Code. 
With every change in the codebase I've made a commit with a detailed description attached, followed by a "git push" to update my GitHub repository.
I've deployed this project to Heroku and used the "git push heroku main" command to make sure my pushes to GitHub were also made to Heroku. 

For local deployment see the following steps:

1. From the application's repository, click the "code" button and download the zip of the repository. Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/DoriCzele/CupcakeClub.git
    ``` 

2. Access the folder in your terminal window and install the application's [required modules](https://github.com/DoriCzele/CupcakeClub/blob/main/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

3. Sign-in to [MongoDB](https://www.mongodb.com/) and create a new cluster:
    * Click on Collections button then click on Create Database (Add My Own Data) called cupcakeClub (ensure same as DB_NAME environment variable)
    * Set up the following collections: users and recipes according to the database structure
    * Under the Security Menu on the left, select Database Access.
    * Add a new database user and keep the credentials secure
    * Within the Network Access option add IP Address 0.0.0.0

4. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It should contain the following lines and variables:

    ```
    import os

    os.environ["HOST"] = "0.0.0.0"
    os.environ["PORT"] = "8000"
    os.environ["DEBUG"] = "True"
    os.environ["SECRET_KEY"] = "<YOUR_SECRET_KEY>"
    os.environ["MONGO_URI"] = "<YOUR_MONGODB_URI>"
    os.environ["MONGO_DB"]= "<DATABASE_NAME>"
    ```

    Update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DB** variables with those provided by MongoDB.
    To find your MONGO_URI, go to your clusters and click on connect. 
    Choose connect your application and copy the link provided. 
    Update the necessary fields like password and database name. 

    In case you're pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

5. To run the application locally type the following command to the terminal: 
    ```
    python3 app.py. 
    ```
    
### Heroku Deployment 

1. Log in to Heroku account and create a new app (make sure you chose the correct region). 

2. Ensure the Procfile and requirements.txt files are present and up-to-date in the local repository.  

    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
3. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

4. Scroll down to "deployment method"-section and pick "Github" for automatic deployment.
5. Select your github user, enter the name for your repository and click on connect.
6. Click on "settings" then click on "Reveal config vars". Set up the same variables as in your env.py (HOST, PORT, DEBUG, SECRET_KEY, MONGO_URI and MONGO_DB):
    MAke sure you don't set the DEBUG variable in under config vars, to avoid DEBUG being active on the live website. 

    ```
    IP = 0.0.0.0
    PORT = 8000
    SECRET_KEY = <YOUR_SECRET_KEY>
    MONGO_URI = <YOUR_MONGODB_URI>
    MONGO_DBNAME = <DATABASE_NAME>
    ```

7. Click "Deploy" then click "Enable automatic deployment".
8. Click "Deploy branch" and Heroku starts building the app. Once the build is complete to open it click "view app".
    
[Back to Top](#table-of-contents)

## **Credits**

* I would like to thank my mentor Simen [Eventyret_mentor](https://github.com/Eventyret) for his support and encouragement.

* I would like to thank [Tamas Barta](https://linkedin.com/in/tamas-barta-50850013a) for the graphic design of the cupcake logo which has significantly improved my website's overall look as well as the user experience.

[Back to Top](#table-of-contents)