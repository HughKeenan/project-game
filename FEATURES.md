The site has the following pages:

Access to pages according to user role:

|Page Name|Unregistered user|Regsitered User|
|--|--|

### Navbar
Each page has a navbar. The navbar looks as follows to a user who is unregistered/not signed in:
![Navbar when not signed in](documentation/features/navbar/navbar_signed_out.png)

The buttons on it are as follows:
![Home Button](documentation/features/navbar/home.png)
![About Us Button](documentation/features/navbar/about_us.png)
![Login Button](documentation/features/navbar/login.png)
![Register Button](documentation/features/navbar/register.png)

It looks as follows to a user who is signed in:
![Signed in navbar](documentation/features/navbar/signed_in_navbar.png)

And it has the following buttons:
![Home Button](documentation/features/navbar/home.png)
![About Us Button](documentation/features/navbar/about_us.png)
![Report User Button](documentation/features/navbar/report_user.png)
![Logout Button](documentation/features/navbar/logout.png)

On smaller screens the navbar is collapsed
![Collapsed Navbar](documentation/features/navbar/collapsed_navbar.png)

The Navbar also displays the site's name and logo, which doubles as a link to the homepage
![Site Logo](documentation/features/navbar/site_logo.png)

### Footer
Each page also has a footer. The footer contains the creator's name, along with icons for instagram, facebook and youtube, which act as links to those sites opening in new tabs. In the case of a professionally used site would link to the site's profile on each platform. The footer layout does not change depending on screen size.
![Footer](documentation/features/footer/footer.png)

### Register
If the user does not already have an account, they can sign up for one using the register link in the navbar. Doing so will bring them to this page:
![Register](documentation/features/register/register.pdf)

If the user already has an account, they can use this link to redirect to the sign in page:
![Redirect Link](documentation/features/register/redirect_link.png)

The username, password and password (again) fields are required to set up an account.

If the user tries to register a username that is already taken, the following message will appear:
![Username Taken](documentation/features/register/username_taken.png)

If they try to submit without entering a username, the following error message will appear:
![Username Blank](documentation/features/register/username_blank.png)

If they try to submit without entering a password, the following error message will appear
![Password Blank](documentation/features/register/password_blank.png)

If they try to submit without repeating the password, they will see the following:
![One password](documentation/features/register/one_password.png)

If the submitted passwords don't match, they will see the following:
![Passwords Not matching](documentation/features/register/password_non-match.png)

### Thread list
The homepage is the most recent entries in the list of threads that makes up the site's content. This was designed to have a clean, uncomplicated look which was inspired by sites like Reddit and the forum pages on Escapistmagazine, with a list of threads prominently displayed with clearly legible titles
![](documentation/features/)

At the bottom of the page, there are buttons that can be used to navigate to older entries. When in the page of older entries, the button marked Next will change to Previous, and when there are 3 pages or more, the two buttons will appear side by side when not on the first or last page.
![](documentation/features/)

### Thread Content
From the homepage, one can click on the title of any thread to view its contents. The view presented will depend on the status of the user.

Users who are not signed in will see the following:
![](documentation/features/)

A user must be authenticated before being allowed to respond to threads. A user who is signed in will see the following:
![](documentation/features/)

On posting a response, it will appear beneath the thread, along with the options to edit or delete it. The counter of responses will also increment up
![](documentation/features/)

The user will also receive a message to say that they have posted
![](documentation/features/)

If the user decides to update, the response form will repopulate with the text of their response
![](documentation/features/)

Any updates will be posted in their original position.
![](documentation/features/)

And a message will be displayed
![](documentation/features/)

If the user chooses to delete, a modal asking for confirmation will appear
![](documentation/features/)

The user may choose to cancel, in which case the page view will be unchanged. If the choose to delete, the response in question will be removed and the counter will decrement
![](documentation/features/)

A message will also display
![](documentation/features/)



