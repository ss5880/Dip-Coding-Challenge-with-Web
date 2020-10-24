How to set up Heroku:

1) Go to heroku.com and make an account
2) You will probably have to add a credit card, but you wont be charged for the free tier
3) Create a new app (https://dashboard.heroku.com/apps), the "New" button is in the top right, choose "create new app"

A) Click the "Settings" tab
B) Click "Reveal config vars"
C) Add a variable called "HOSTED", and set its value as true
D) Install the Heroku CLI
E) Open a terminal and type "heroku login"
F) Type "heroku ps:scale web=1 -a "NAME OF YOUR APP" "

4) Click the "Deploy" tab
5) Under "Deployment Method", select "connect to github"
6) Under "App connected to GitHub" choose your repository
7) Under "Manual Deploy" click "Deploy Branch"
8) Once that finishes, it will either give you an error, or it will say successful
9) You can click the "view live app" button, or the "Open App" button at the top of the page
10) You should see the webpage (if you didn't chage the GET path from "/test" to something else, you will have to go to WEBPAGENAME.herokuapp.com/test to view it)