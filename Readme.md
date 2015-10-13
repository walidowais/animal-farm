Animal Farm info:
 - Technologies Used: 
     - Python (Flask) web framework for backend server
     - Python (Jinja2) templating language) to dynamically use python 
     code in html pages 
         - //looking back now, could/should have used Javascript
     - SQLite 3 for database work
     - HTML/CSS for front end 

 - with animal farm, the goal was to ramp up the difficulty level and try 
 to do something with more user interactivity than catfacts

 - so flask works mainly through the @app.route("xxx") statements which 
 call the function designated directly afterwards when the specific page 
 is requested from the server and the browser diplays what is returned by 
 the function

     - use flask's render_template function to open and parse html and 
     pass parameters from python server code to Jinja variables.
        best example at end of pages function (line 70)

 - @app.before_request calls a function to connect and setup the database 
 before every page that gets loaded

 - @app.teardown_request calls a function to close the database object 
 after every page is closed

 - error pages: use the flask @app.errorhandler to handle 404 error

 - user starts and homepage : @app.route('/')
    gets a random page from the database of topics and redirects to the 
    url for that page, if there's no pages: redirects to "new_post" page

 - the pages are designated as "/discussion/<page_num>" and flask fills 
    in that page_num with the parameter to the function
    checks if the page number is valid, if its not, send to invalid page
    selects the sqlite database for the requested page and sends the data 
    to be rendered through parameters to Jinja using the Homepage.html as 
    an html template

 - simpler pages
     - about, just renders the about.html and returns it
     - invalid page, lets the user know the discussion number doesnt exist
     - logout, turns off the session's logged in setting and redirects to 
     the login page

 - more advanced interactive pages
     - use POST and GET data to send data from input fields to interact 
     with python code and database
     - GET data is specified in url
     - POST data is sent as part of HTTP request

 - login page
     - check if there is POST data
     - if no post data then just render login.html
     - if there is post data, search database of users, check password
     - login and redirect to the previous page

 - signup page
     - similar to login page
     - check if POST data
     - if no post data then just render signup page with form to fill
         - once user submits form with data routes to same function but 
         instead does it with post data
     - else get info from request object and add new user to database

 - new post page
     - same as login and signup
     - only difference, checks user's session data to see if they're 
     logged in, if not: redirects to login page
     - if no post data, just render the page
     - once user submits the form, directs back to same page with post 
     data, which calls the same function
     - this then adds the new post into the database and redirects them 
     to the page for this topic
