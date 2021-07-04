
![In Vino Veritas](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/amIResponsive.JPG "In Vino Veritas")

<span id="index"></span>
## Index
 <a href="#project">Project Idea 💁</a>
1. <a href="#ux">UX 👌</a>
1. <a href="#features">Features 🎮</a>
1. <a href="#technologies">Technologies Used 👉</a>
1. <a href="#testing">Testing 🔧</a>
1. <a href="#deployment">Deployment 💥</a>
1. <a href="#credits">Credits 👋</a>



<span id="project"></span>
# In Vino Veritas
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
### Milestone Project 3 - Data Centric Development
[live website here](https://in-vino-veritas.herokuapp.com/get_index)
--------------------------------------

Third Milestone project demonstrates Back End Data Centric Development skills using Python, Flask framework with WTForms and MongoDB. The key requirement was to implement CRUD funcionality to the website.
Inspiration for "In Vino Veritas" was sourced from wisdom found in Latin Quotes. These are very popular around many people and I will try to spread these out even further. It will not only gather the most famous quotes but it also aims to be the largest collection as users can add their favourite ones too. 


<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy

The goal of this project is to provide friendly database of latin quotes for users while they can update it themselves. Professional and resposinve design should attract more people to create an account and extend this project beyond my expectations. 

### User stories

With an agile approach I will be focusing on both external and internal clients.

As user I would like to:

- view popular latin quotes and their authors
- create and delete an account
- trust this page where my data will be stored securly
- log in and log out
- add, edit and delete my favourite qoutes
- display a quote of the day
- display my favourite quotes
- easy navigation menu
- responsive design for mobile devices

As a website owner I would like to:

 - admin account to be able manage details of authors
 - attract users with intuitive design
 - have the quotes sorted according user needs - name, popularity etc...


## 1.2 Scope 

From our strategy plan there were few funcionalities identified in order to satisfy user needs. To implement Minimum Viable Product our product will need folowing features:

- welcoming main page
- appropriate navigation
- responsive design
- page with latin qoutes content and search function
- user page to add, update, display and delete quotes
- user page with favourite quotes
- admin access to maintain the database
- registration page, log in page
- database model
- database of users
- databes of authors and a database of quotes
- back-end feature to access our data for CRUD funcionality

## 1.3 Structure

Project consist of two main sections. Front end part which is focused at HTML code and design using CSS and Materialize framework.
Back end part is Data oriented. Data is stored in MongoDB cluster created for this project and accessed through Python app.
To avoid repeating same HTML code, to enable some logic and to have more control over content the website will be rendered using Pyhton with Flask framework.

## 1.4 Skeleton

Front-end

In Vino Veritas contains structured navbar for easy navigation. The Logo and text - In Vino Veritas is a link to index page. Following links are displayed when no user is logged in. First link - *In Vino Veritas* - brings user to index page providing date and quote for the day. Second link - *Random Quote* displays randomly generated quote every time clicked. Third link - *All quotes* - navigates to page displaying all quotes in database, sort funcionality, a search bar. Fourht link brings user to *log in* page and fifth provides the user *registration* form.
When user is logged in the first three links remain the same. There is added funcionality for user to like or unlike quote on the all quotes page. Fourth link reads - *My qoutes* - which displays qoutes added by user. Add a new qoute, edit and delete funcionality is also on the same page. Fifth link - *Favourite Quotes* - returns page with quotes which user likes. The next link - *Profile* - brings users to profile page where they can change password or completely delete their account. Last one - *Log Out* - terminates user session and returnes to Log In page.
When admin is logged in the navbar also containes *Manage Authors* link to maintain the Authors database.
Same as navbar, every page displays consistent footer with Copyright section on a left side. The right corner contains a name of user who is curently logged in. A message "No user logged in" reads if no active user is loged in.


Back-end

Database is divided into three main sections - Users, Quotes and Authors.

### Users
| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | MongoDB generated ID |
| user_name  | String   | Contains user name for log in |
| user_email | String   | Contains user email address   |
| user_password | String | Stores hashed user password for log in |


### Quotes
| Key | Type of | Info |
|-----|:-------| :----|
| _id | Object ID | MongoDB generated ID |
| latin_text | String | Contains latin text of the qoute |
| english_text | String | Contains english translation |
| added_by | String | Name of the user who added this qoute - user_name from Users collection |
| num_of_likes | Int32 | Counter how many users liked this qoute |
| author | String | Name of author whom the qoute is attributed to |
| users_liked | Array | Containes user names who liked this qoute - user_name from Users collection |


### Authors
| Key        |Type of   | Info                          |
| ---------- |:--------| :-----------------------------|
| _id | Object ID | MongoDB generated ID |
| author_name  | String   | Contains name of a famous person |
| era-lived | String   | Era which this person lived in |
| description | String | brief description what was the person famous for |
| img | string | url address of image of the famous person |


Database schema:
![DBmodel](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/dbDiagram.png "Database schema")

## 1.5 Surface

The design was built on the hero image of the index page - two glasses of wine and grapes. I tried to experiment with fonts but I found the best result using generic fonts. The color scheme was generated using Accessibility Tools provided by Adobe Color. The color pattern was slightly adjusted for easy use with Materialize framework. Text is displayed in white, black or Indigo color. Help text uses grey color.
- #FFCA28 Materialize Amber lighten-1 / CSS - Gold
- #3FS1BS Materialize Indigo / CSS - Darkslateblue
- #FFFFFF White color
- #26A69A Materialize default button color / CSS - Lightseagreen
- #F44336 Materialize Red / CSS - Tomato

![Color scheme](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/colorScheme.JPG "Color scheme")

### Wireframes

Wireframes were created usign online tool Figma. Pages will be responsive and layout shall remain the same. First set of wireframes show the website when no user is logged in. A change in navigation can be seen on second picture when a user logs in. There is added funcionality to maintain Authors database when admin is currently logged in.

No user logged in
![No user logged in](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/figma01_no_user.JPG "No user logged in")

User logged in
![User logged in](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/figma02_user_logged.JPG "User logged in")

Admin logged in
![Admin logged in](https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/figma03_admin-logged.JPG "Admin logged in")

<a href="#index">Back to top ☝️ </a>
<span id="features"></span>

# 2. Features 🎮

## 2.1 Implemented features

As mentioned the project contains consistent navbar and a footer. The Navbar is responsive supported with nice slide-out feature on smaller screens using Materialize framework. Using Python code navbar links change based on active session when user or admin is logged in. This funcionality is also implemented in footer on a right side where logged in user name is displayed. The year in Copyright section is automaticaly updated using JQuery code. There is also Back to top button on each page if user scrolls down more than 300 px.

If an internal or server error occurs, special page is returned with a flash message explaining something went worng or content can't be found. This can happen if no user is logged in and tries to access a site which can be only accessed by logged user. This is added security feature checking session status. More details about the error can be obtained when clicking the error status bar.

The index page displays nice hero image and a current date. A quote of the day is generated based on the day of the month.

When Random Quote link is clicked a random number is generated. This is matched with loop index of quotes to display only one random quote.

All Quotes page contains a search bar, sort by funcion and quote cards. User can search in both latin and english version of text as only these are indexed.  Minimum of three characters must be provided. Quotes can be sort alphabeticaly, by rating or by newest. Quotes are displayed on cards. Each quote card reads latin and english text, author name and user name who added quote to database. If author is in Authors collection, a portrait is displayed. Offensive language is censored using flask_censor. There is a favourite section at the bottom of the card. The left icon provides a link to log in page when no user is logged in. This change to add to / remove from favourites when user is logged in. Hearth icon changes from white to red if user liked the quote. The right icon displays number of people who liked this quote.

User can create account on register page providing a user name, password which needs to be confirmed and an email address. These inputs are validated using WTForms library. For enhanced security stored password is encrypted using Werkzeug security library. An extra login button is added for convenient login from registration page.

Registered user can gain access on Log In page. User name and password is required.
Flash messages are used to display certain messages - eg user Log In or Log Out. Again there is extra button which brings user to register page if needed.

CRUD funcionality is implemented on My Quotes page. User can add new quote, edit or delete quote which was added already. To add new quote, latin text, english text and author name is required. Convenient feature is added when user wants to change the quote previous text is displayed for easier editing. When deleting qoute, user is prompted to confirm if they realy wants to delete that quote.

Quotes which user liked are displayed on Favourite Quotes.

Users can also change password or completely delete their accounts in Profile section. For security purposes, user needs to enter current password in order to change this. Again, when deleting account user is asked to confirm this action to prevent accidental deletion.

Admin can also access and maintain Authors database. New author can be added with name, era lived, description and url address for image. Author data can be also modified or author can be deleted. When editing or deleting author, same features are in place as when modifying or deleteing quotes.

Users / admin can log out when they no longer wish to work with database.

# 2.2 To be implemented

Few more features were identified which could be implemented. Blog / user forum could be added to share experience and opinions about latin wisdom. User could be able to upload their picture to promote design. In a case user forget password account recovery function would be handy.
Admin account could also provide funcionality to control all quotes in a database and also to control user accounts, eg to be able suspend user who post inapropriate content.
 
<a href="#index">Back to top ☝️ </a>
<span id="technologies"></span>

# 3. Technologies Used 👉

## 3.1 Languages

- HTML/HTML5
Each web page was built using HTML elements.

- CSS
Some HTML elements were styled using CSS

- JavaScript / Jquery
Jquery was used for following features:
    Drag out mobile menu, ollapsible server error messages, year auto update in footer and back to top button.

- Python
This app was build using various python based frameworks, libraries and template engines.
Flask - python based micro web framework. Web pages are rendered using Flask
Jinja2 - python based template engine. Together with HTML creates dynamic web content.
WTForms - library for python to work fast and efficiently with forms.
Pymongo - library which enables Python code to acces MongoDB

## 3.2 Other libraries

- Materialize
Navbar, Footer and some other elements were implemented using this popular library.
Materialize was also used to design most of the content.

## 3.3 IDE, Version control and hosting

- Visual Studio Code with Git / GitHub extensions
Code was written localy using Visual Studio Code and so

- Git and GitHub
Version control and repository

- Heroku
GitHub repository was linked with Heroku and is hosted here

- MongoDB
All content is stored in cluster provided by MongoDB

## 3.4 Other tools

- Figma was used to create wireframes

- Adobe Color was used to identify the color scheme

- Am I Responsive was used to create title image for readme.md

- Dbdiagram was used to create DB schema

- Chrome Devtools were used to see the behaviour of the elements and their style

<a href="#index">Back to top ☝️ </a>
<span id="testing"></span>

# 4. Testing 🔧

## 4.1 Validation

HTML code was checked in W3C validator with no errors - https://validator.w3.org/

CSS code was checked in W3C validator with no errors - https://jigsaw.w3.org/css-validator/

JS code was checked in BeautifyTools with no errors - http://beautifytools.com/javascript-validator.php

JS code was also checked in JSLint with no errors - https://jslint.com/

Python code was checked in pep8 online and errors were fixed. White spaces at the end of lines, and lines with non compliant lenght were the only issues.  - https://pep8online.com/

Responsivness was tested in Chrome and Firefox on Win10 with Devtools, ipad mini 6th gen, onePlus 7pro phone and Am I Responsive website. Iphone 5 was used in Devtools as standard for smallest screen. Text on some buttons had to be removed as it was overflowing on Iphone 5. Materialize grid classes and helpers were used to hide /show content and enable it to be responsive.

## 4.2 Features testing

- Navbar

All test were completed with user signed in and out.
All links in navbar were tested on Iphone 5, ipad mini and in browsers on Win10 laptop. All links were working fine and appropriate pages were rendered corectly. Mobile drag out navbar was displayed on Iphone 5 and ipad mini on portrait orientation. Full navbar is displayed on screens wider than 993px.

- Footer

All test were completed with user signed in and out.
Correct year was dipslayed in copyright section at all times after feature was added. Code was amended to return month instead of year and result was correct. No user logged in changed imediately after user or admin loged in. This changed back when user logged out.

- Back to top button
All test were completed with user signed in and out.
Button was checked if appers on scrolling down and brings user back to top of the scree.

- Index page

All test were completed with user signed in and out.
Correct date was displayed every time since this funcionality was added. Appropriate quote of the day was also displayed.

- Random Quote

All test were completed with user signed in and out.
Every time Random quote link is clicked a new random quote is displayed. This was tested with added flash messages to see the random number, to ensure that the first and the last quote is returned and also the max value is adjusted if a quote is added or removed.

- All quotes

All test were completed with user signed in and out.
Search bar was tested with various words which either exist or not in indexed text. Error message is displayed if user provides less than 3 characters. 
Sort by functionality was tested and all results were correct.
Login button returns log in page.
Like / Dislike button was checked and also cross checked in MongoDB users_liked array.
Number of likes indicator was tested every time a quote was liked or disliked.
Quote with offensive text was added and censore function was correctly applied.

- Register

Registration form was tested as follows:
User name must be between 5-15 characters. Error messages "Name must be between 5 and 15 characters long" were returned if input was incorrect.
Password must be between 8-20 characters. Error messages "Password must be between 8 and 20 characters long." were returned if input was incorrect.
Passwords must match. Error message reading "Passwords don't match" was returned.
Email address input must have valid format. Error messages "Invalid email address." were returned if format was not correct.
Duplicate user names was tested and error message "User name alredy exist" was returned. This was checked with capitalized characters and same error message was returned.
Duplicate email addresses were tested and error message "Email address already registered" was returned. As previously, error message is returned with capitalize characters too.
Login link works as expected.


- Log in

Log in funcionality was tested to check all relevant features are available when user or admin correct details are provided.
Non existing user name was provided. "Incorrect login details" message was returned without stating if the user name or password is incorrect. Supporting flash messages were used during development to see if certain condition was not met.
A correct user name was provided with incorrect password. "Incorrect login details" message was returned without stating if the user name or password is incorrect.
A correct user name was provided with capitalized password to check if this is case sensitive. Same error message was displayed if password was capitalized.
Register link works as expected.
A session cookie was checked through Devtools - Application - Storage - Cookies. Session cookie was added succesfully,


- My Quotes

My quotes page was tested if returning only quotes which were added by active user.
Three quotes were added succesfuly to test if add quote feature works correctly.
When unknown author name was added no image was displayes. This is correct as authors database is maintained manually by admin.
Cancel button was tested and no quote was added to database.
Edit quote function was tested and correct quote was returned to pre-fill change quote form. Both save and cancel button working as expected.
Delete quote feature was tested and selected quotes were deleted. Back / cancel button works correctly.
Text censor was tested and original text was displayed. This is correct as only user who added this quote can see the text.

- Favourite Quotes

Five quotes was liked and disliked later to see if correctly displaying on this page. All results were as expected.

- Profile

Change password feature was tested providing incorrect current password and no changes were made. Error message "Password not changed - incorrect old pasword provided!" is returned. This is correct result
Change password was tested providing corrrect current password, valid new password and same re-entered password. Password was changed succesfuly.
Change password was tested providing non valid new password. Error message "Password must be between 8 and 20 characters long." is returned.
Change password was tested with different new passwords. Error message "Password don't match" is returned.
Save and cancel buttons work as expected.

Test accounts were created and succesfuly deleted using delete account funcionality. Cancel button also works as expected.

- Manage authors.

Add author form was tested to add new author into database. All fields are validated and error message reads "Please fill out this field" if no input is provided. There is no added validation since this is only accesible by DB admin. Add author and cancel button work correctly.
Edit author function was tested and correct author was returned to pre-fill change author form. Both save and cancel button working as expected. A bug was found where image url was modified to lower characters and no pictures were rendered.
Delete author feature was tested and selected authors were deleted. Back / cancel button works correctly.

- Log out

Log out feature was tested. Session cookie has been removed from storage. Error page is rendered is user tries to access application over browser url line.

<a href="#index">Back to top ☝️ </a>
<span id="deployment"></span>

# 5. Deployment

<a href="#index">Back to top ☝️ </a>
<span id="credits"></span>


# 6. Credits

wtf forms https://www.youtube.com/watch?v=vzaXBm-ZVOQ
form validation https://stackabuse.com/flask-form-validation-with-flask-wtf
password comlexity https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions#32542964
https://stackoverflow.com/questions/26105804/extract-month-from-date-in-python/26105888
https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict

https://dbdiagram.io/d/60ddf0e8dd6a59714828a429