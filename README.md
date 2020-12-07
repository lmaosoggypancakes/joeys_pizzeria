# Joey's Pizzeria

This is my submission for my final project: a website for a pizza place called Joey's Pizzeria.

Please note: loading HTML files from this project will not render properly. Because they are using template syntax, they will not properly load when executed. Because of this, the project that is uploaded to the FTP client will not work properly! This repository serves to both display the project and to deploy from Heroku.

Additional Features:
- Javascript to change the DOM
- Table
- Facebook/Twitter "buttons"
CSS Features
- Gradient
- Animation (upon submitting the apply form, as described here)

### Functionality and URLs

Website: [https://joeyspizzeria.herokuapp.com/](https://joeyspizzeria.herokuapp.com/)

- `/login` - Displays an HTML page where a user can log in. If the credentials are correct, the user is logged in an redirected to the home page. Otherwise, an alert will show up saying their login info is incorrect.
- `/register` - Page where a user can sign up for an account, they must provide an email, username and password (username must be unique and email can be a fake email).
- `/logout` - If the user is logged in, the user is logged out and redirected to the home view.
- `/menu` - HTML page that will display all the items in the menu, with the price, description, picture, and an "add to order" button, formatted by a table. If the user is logged in and clicks the button, the corresponding item is added to the order.
- `/order` This page is only visible when the user is logged in. The user can see their order and all items in it. For each item, there is a button to remove the item from the order.
- `/` - Home page with simple information about the pizza place.
- `/social` - Static HTML page with embedded Twitter and Facebook posts from the social media accounts and hyperlinks to both accounts and to a Google Maps directions for each location.
- `/apply` - Also only visible when the user is logged in. Provides a HTML form where a user can submit an application for a job, with multiple input fields, and, upon submission, is saved in a database of sorts. Note that this will NOT be sent to FormProcessor.html, as will any form throughout this project! I've emailed and sent a message of this through Canvas ahead of time.
- `/api/add` and `/api/remove` - Adds or removes an item from an order. This URL is used only through javascript's `fetch` command and will only return JSON if visited like a normal URL

# Admin Interface

Django has a built-in admin interface, that, in this case, is used to create and add items to the "menu" visting `/admin` will prompt the user to log in. If the user is a superuser, they are logged in. If a logged in superuser creates a new item in the menu, it will show up in the menu page!

