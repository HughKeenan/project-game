The site has the following pages:
+ Thread list (home page)
+ Thread content (content page for a given thread)
+ Register
+ Login
+ Logout
+ About Us
+ Report User

Access to pages according to user role:

|Page Name|Unregistered user|Regsitered User|
|--|--|--|
|Thread list|Full access|Full Access|
|Thread content|Can read but not respond|Can read, can respond, update and delete responses|
|Register|Full access|Full Access|
|Login|Can access but not use until account is made|Full access|
|Logout|Full access|Full Access|
|About Us|Full access|Full Access|
|Report User|No access|Full Access|

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

![Register](documentation/features/register/register.png)

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

![Passwords Not matching](documentation/features/register/password_non_match.png)

### Thread list
The homepage is the most recent entries in the list of threads that makes up the site's content. This was designed to have a clean, uncomplicated look which was inspired by sites like Reddit and the forum pages on Escapistmagazine, with a list of threads prominently displayed with clearly legible titles. It does not change depending on login status. Each entry displays the title and username of the person who posted it, along with the date of post.

![Thread List](documentation/features/thread_list/thread_list.png)

At the bottom of the page, there are buttons that can be used to navigate to older entries. When in the page of older entries, the button marked Next will change to Previous, and when there are 3 pages or more, the two buttons will appear side by side when not on the first or last page.

![Next Button](documentation/features/thread_list/next_button.png)

![Previous Button](documentation/features/thread_list/previous_button.png)

### Thread Content
From the homepage, one can click on the title of any thread to view its contents. The view presented will depend on the status of the user.

Users who are not signed in will see the following:

![Thread Content (not signed in)](documentation/features/thread_content/thread_content_signed_out.png)

A user must be authenticated before being allowed to respond to threads. A user who is signed in will see the following:

![Thread Content (signed in)](documentation/features/thread_content/thread_content_signed_in.png)

The user may fill out a response in the form and post with the submit button. On posting a response, it will appear beneath the thread, along with the options to edit or delete it. The counter of responses will also increment up.

![Response Posted](documentation/features/thread_content/response_posted.png)

The user will also receive a message to say that they have posted

![Posted message](documentation/features/thread_content/posted_message.png)

If the user decides to update by pressing the edit button below their response, the response form will repopulate with the text of their response. The button below will also change to say update.

![Update Response](documentation/features/thread_content/update_response.png)

Any updates will be posted in their original position.

![Response Updated](documentation/features/thread_content/response_updated.png)

And a message will be displayed

![Updated message](documentation/features/thread_content/updated_message.png)

If the user chooses to delete, a modal asking for confirmation will appear

![Delete Modal](documentation/features/thread_content/delete_modal.png)

The user may choose to cancel, in which case the page view will be unchanged. If they choose to delete, the response in question will be removed and the counter will decrement

![Response after delete](documentation/features/thread_content/responses_after_delete.png)

A message will also display.

![Deleted Message](documentation/features/thread_content/deleted_message.png)

### About Us
This is an entry in the thread list intended to function as a page to explain to new users the purpose of the site. It can be accessed by scrolling through the list like any other thread, but it was decided that having a dedicated link would be a better user experience. As it's a thread like the others, it shares all of the functions mentioned in the thread content section

![About Us](documentation/features/about_us/about_us.png)

### Login
Users who already have an account can use this page to sign in to the site.

![Sign In](documentation/features/sign_in/sign_in.png)

If the user doesn't have an existing account they can redirect to the register page using this link:

![Redirect to register](documentation/features/sign_in/redirect_to_register.png)

If the user attempts to sign in without a username, they will get the following error:

![No Username](documentation/features/sign_in/no_username.png)

If the user attempts to sign in without a password, they will receive the following error:

![No Password](documentation/features/sign_in/no_password.png)

If the user uses an incorrect password, they will see the following:

![Wrong Password](documentation/features/sign_in/wrong_password.png)

If the user signs in successfully, they will be redirected to the home page and receive amessage like the following, updated for their username:

![Successful Sign in](documentation/features/sign_in/successful_sign_in.png)

### Logout
Signed in users can use this to log out of the site by clicking the Sign out button.

![Sign Out](documentation/features/sign_out/sign_out.png)

If they sign out they will be redirected to the home page and they will receive a notifcation

![Sign Out Message](documentation/features/sign_out/sign_out_message.png)

### Report User

This page is available to users to report others for inappropriate behaviour on the site. By clicking the Report User button in the navbar, this will open in a separate window. It was decided that opening it in a new window would be better as it means the user can more easily refer to what they wish to report without having to reset the report form.

![Report User](documentation/features/report_user/report_user.png)

The form requires specific data types in order to be submitted successfully. If the user attempts to submit the form with blank fields or data that doesn't match the required type, they will see an error message like this one:

![Report User](documentation/features/report_user/report_form_error.png)

If the user submits the for correctly, the page will refresh and the report form will be blank, in case they wish to submit another. They will receive the following message:

![Report Message](documentation/features/report_user/report_message.png)


## Admin Features
This site is dependent on input from the superusers, who can post new content from the admin page, accessed by appending '/admin' to the homepage url

### Post threads
Superusers can post new threads to the site. This is accessed by the Threads option in the admin menu
![Admin Menu](documentation/features/admin/admin_menu.png)

![Threads Menu](documentation/features/admin/thread_menu.png)

By selecting New thread in the top left, a new one can be posted

![New Thread](documentation/features/admin/new_thread.png)

Once saved, this will appear in the list of threads, and at the top of the list on the front end, and may be accessed and interacted with like any other thread

![Posted Thread](documentation/features/admin/posted_thread.png)

![Posted Thread Content](documentation/features/admin/posted_thread_content.png)

Existing threads can also be edited by selecting them from the list and changing the text using the summernote editor

![Edited Thread](documentation/features/admin/edited_thread.png)

![Edited Thread Content](documentation/features/admin/edited_thread_content.png)

Posted threads can also be deleted by selecting them in the list and choosing to delete in the dropdown menu.

### Reports

The report guidelines can be updated in much the same way as a thread by selecting reports from the list in the main admin page and then selecting the report entry

![Report Guidelines](documentation/features/admin/reports.png)

To view submitted reports, select Report Users. The title is visible, as is the status of whether or not it has been looked at yet. 

![Reports on users](documentation/features/admin/report_users_.png)

By selecting it, the superuser can review it and once satisfied, change the status to examined

![Report details](documentation/features/admin/report_details.png)

This will update it in the list.

![Examined report](documentation/features/admin/examined_report.png)

And it can then be deleted in the same manner as a thread.

While this is being examined, comments that have been reported on can be rendered invisible while the admin decides what to do.

This is done by selecting a response from the list under Responses, the same manner as a thread. Once viewing the details, the comment can be disabled by unchecking the 'Visible' box. This is to ensure that anything unsuitable can be hidden while still being retained in case authorities need to be contacted.

![Response details](documentation/features/admin/response_details.png)

This is the view before the check:

![Visible Response](documentation/features/admin/visible_response.png)

And after:

![Invisible Response](documentation/features/admin/invisible_response.png)

Once the response has been rendered invisible, reported users can have their accounts disabled. To do this, select users from the menu and then the profile of the specific user being reported. Once in there, the Active box can be unchecked, at which point the user will be unable to log in until it is unchecked. Users can then be deleted if necessary. Any responses will remain on the database, again in case they contain anything requiring further investigation.

![User details](documentation/features/admin/user_details.png)