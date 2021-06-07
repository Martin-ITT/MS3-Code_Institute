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
Inspiration for "In Vino Veritas" was sourced from wisdom found in Latin Quotes. These are very popular around many people and we will try to spread these out even further. It will not only gather the most famous quotes but it also aims to be the largest collection as users can add their favourite ones too. 


<span id="ux"></span>
# 1. UX 👌
## 1.1 Strategy 👪

The goal of this project is to provide friendly database of latin quotes for users while they can update it themselves. Professional and resposinve design should attract more people to create an account and extend this project beyond our expectations. 

### User stories

With an agile approach I will be focusing on both external and internal clients.

As user I would like to:

- view popular latin quotes and their authors
- create and delete an account
- trust this page where my data will be stored securly
- log in and log out
- add, edit and delete my favourite qoutes
- display a random quote for the day
- display my favourite quotes
- easy navigation menu
- responsive design for mobile devices

As a website owner I would like to:

 - admin account to be able manage details of authors
 - admin account to be able manage standard user accounts
 - attract users with intuitive design


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

In Vino Veritas will contain structured navbar for easy navigation. Following links will be displayed when no user is logged in. First link Today's quote containig random or selected quote for the day. Second link Quotes will navigate to page displaying all quotes in database and a search bar. Third link will bring user to log in page and fourth will provide user a registration form. Logo in left side of navbar will return to main page with hero image.
When user is logged in Todays Quote will remain the same. The second page will also contain buttons to add new quote or see users favourites quotes. Third link will read My Quotes where user will find funcionality to add, edit or delete his or her quotes. Fourth link will provide log out funcionality.
When admin is logged in the navbar will also contain Manage Authors link to maintain the Authors database.
Same as navbar, every page will display consistent footer with Developer's GitHub link and Copyright section. The right corner will show a name of user who is curently logged in and a delete account function. A message "No user logged in" will read if no active user is looge in.

Back-end

Database will be devided into three main sections. User section will contain user names and hashed passwords for enhanced security. Quotes section will store a latin version, english translation and name of author if known.  Third section will contain name of authors, era they lived in and brief description.
Web content will be rendered using Pyhton with Flask framework.
