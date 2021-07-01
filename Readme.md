.<span id="index"></span>
## Index
 <a href="#project">Project Idea 💁</a>
1. <a href="#ux">UX 👌</a>
1. <a href="#features">Features 👍</a>
1. <a href="#technologies">Technologies Used 👉</a>
1. <a href="#testing">Testing 🔧</a>
1. <a href="#deployment">Deployment 💥</a>
1. <a href="#credits">Credits 👋</a>



<span id="project"></span>
# In Vino Veritas
## [Code Institute](https://codeinstitute.net)
### Full Stack Web Development Course
### Milestone Project 3 - Data Centric Development
--------------------------------------
![In Vino Veritas](img/Capture.JPG "In Vino Veritas")

Third Milestone project will demonstrate Back End Data Centric Development skills using Python and MongoDB.
Inspiration for "In Vino Veritas" was sourced from wisdom found in Latin Quotes. These are very popular around many people and I will try to spread these out even further. It will not only gather the most famous quotes but it also aims to be the largest collection as users can add their favourite ones too. 


<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy 👪

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

Front-end

In Vino Veritas contains structured navbar for easy navigation. Following links are displayed when no user is logged in. First link - In Vino Veritas - brings user to index page providing quote of the day. Second link - Random Quote displays randomly generated quote every time clicked. Third link - All quotes - navigates to page displaying all quotes in database, sort funcionality, a search bar and how many users likes certain qoute. Third link brings user to log in page and fourth provides the user registration form.
When user is logged in the first three links remain the same. There is added funcionality for user to like or unlike quote on the all quotes page. Fourth link reads - My qoutes - which displays qoutes added by user. Add a new qoute, edit and delete funcionality is also on the same page. Fifth link - Favourite Quotes - return page with quotes which user likes. On the next page - Profile - can users change password or completely delete their account. Last one - Log Out - terminates user session and returnes to Log In page.
When admin is logged in the navbar also containes Manage Authors link to maintain the Authors database.
Same as navbar, every page displays consistent footer with Copyright section on a left side. The right corner contains a name of user who is curently logged in. A message "No user logged in" reads if no active user is loged in.

Back-end

Database is devided into three main sections - Users, Quotes and Authors.

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
![alt text][dbmodel]

[dbmodel]: https://github.com/Martin-ITT/MS3-Code_Institute/blob/main/static/img/Untitled.png "Database schema"





Wireframes


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")





 Users, Quotes, Authors. Apart from generated ID, user section stores user names, email addresses and hashed passwords for enhanced security. Quote document consists of six fields - latin text, english text, name of author if known, added by, number of likes counter and an array of user who liked the qoute. Authors section contains name of author, era they lived in, a brief description and a url address for image.




Web content will be rendered using Pyhton with Flask framework.


testing
registration form
user name checked against empty input and not to be less than 5 and more than 15 char
user name white spaces and special char
password checked against blank input and not to be less than 8 and more than 20 char
password against white spaces
password match checked
password change - check for error messages
email validator checked for empty input, valid email address and not to be more than 120 char
session cookie test - user logged / registered in

update quote - problem with likes
delete quote

check admin session
search returned no pics

registration checked for same user name
registration checked for same email address (diferent names)

add like
remove like
num of likes - various users

references
wtf forms https://www.youtube.com/watch?v=vzaXBm-ZVOQ
form validation https://stackabuse.com/flask-form-validation-with-flask-wtf
password comlexity https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions#32542964
https://stackoverflow.com/questions/26105804/extract-month-from-date-in-python/26105888
https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict

https://dbdiagram.io/d/60ddf0e8dd6a59714828a429