    **Social Media Project**

Description:-
This Django project is a simple social media platform where users can register, login, and logout. Once logged in, users can view all posts, like posts, comment on posts, post their own content, edit their profile, view their own posts, and see the number of likes and comments on each post.

Features:-
Registration: Users can register for an account by providing their username, email, and password.

Login:-
Registered users can log in to their account using their username and password.

Logout:-
Logged-in users can log out of their account.

View All Posts:- 
After logging in, users can view all posts created by other users.

Like Posts:- 
Users can like posts created by other users.

Post Comments:- 
Users can comment on posts created by other users.

Post Own Content:-
Users can create and post their own content.

Edit Profile:- 
Users can edit their profile details such as username, email, and profile photo.

View My Posts:- 
Users can view their own posts on a dedicated page.

Feed for All Posts:-
Users can access a feed displaying all posts from all users.

See Likes and Comments:-
Users can see the number of likes and comments on each post.

Usage:-

Registration:
Navigate to the registration page.
Provide a username, email, and password.
Click the "Register" button.

Login:
Navigate to the login page.
Enter your username and password.
Click the "Login" button.

Logout:
Click the "Logout" button located in the navigation menu.

View All Posts:
After logging in, you will be redirected to the homepage where you can view all posts.

Like Posts:
Click the like button on a post to like it.

Post Comments:
Scroll down to the comments section of a post.
Enter your comment in the input field.
Click the "Post" button to submit your comment.

Post Own Content:
Navigate to the "Create Post" page.
Enter your content in the provided form.
Click the "Post" button to publish your post.

Edit Profile:
Click on the "Edit Profile" option in the navigation menu.
Update your profile details as needed.
Click the "Save" button to save your changes.

View My Posts:
Click on the "My Posts" option in the navigation menu to view your own posts.

Feed for All Posts:
Click on the "Feed" option in the navigation menu to access a feed displaying all posts from all users.

See Likes and Comments:
Each post will display the number of likes and comments it has received.



Installation :-

1. Clone the repository:
git clone <repository-url>


2.Install dependencies:
pip install -r requirements.txt
npm install


3.Intialize style.css by tailwind:
npm install tailwindcss
npx tailwindcss init

Make a tw.css file in users/static/ which contains : 
@tailwind base;
@tailwind components;
@tailwind utilities;

Now run :-
npx tailwindcss-cli@latest build tw.css -o style.css


4.Run migrations:
python manage.py makemigrations
python manage.py migrate


5.Create a superuser 
python manage.py createsuperuser


6.Start the development server:
python manage.py runserver


Access the application in your web browser at http://127.0.0.1:8000/
