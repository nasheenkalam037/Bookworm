Webserver Instructions
======================

Below are the instructions you will need to [setup](#installation) and [run](#running-the-server) the webserver.

## Installation
1. Install Node.js LTS (version 10.15.0+): https://nodejs.org/en/download/
    * Make sure to install NPM when installing Node (it is packaged together)
    * Make sure you install it on your path
1. Open a terminal and navigate to THIS directory
1. Enter the command `npm install`, you should have NO ERRORS and the following output
<details>
<pre>
>npm install
npm notice created a lockfile as package-lock.json. You should commit this file.
added 79 packages from 100 contributors and audited 172 packages in 5.39s
found 0 vulnerabilities
</pre>
</details>

## Running the Server
1. Enter the command `SET DEBUG=web:* & npm start`, you should have NO ERRORS and the following output
<details>
<pre>
>SET DEBUG=web:* & npm start

\> web@0.0.0 start D:\Work\Masters_Phd\workspace (GradSchool)\ece651-project\src\web
\> node ./bin/www

  web:server Listening on port 3000 +0ms
</pre>
</details>


## Running the Server (ALTERNATIVE)
If you are using VS Code, you can easily run the server:
1. Open the DEBUG side bar (looks like a bug with a cirlce and a cross through)
1. Select Launch Web Server from the drop down list (beside the green play button)
1. Press the green play button

***

## Adding a New Route
Routes are web urls that we support.

If we wished to add the route: `ourwebserver.com/not_created_yet`, we need to follow these steps:
1. Open `./routes/index.js`
1. Add the following lines:
```javascript
router.get('/not_created_yet', function(req, res, next) {

  // I can process the request here with any extra processing, IF NEEDED

  // This grabs our view: 'views/index.hbs' and gives it the information contained within the object
  res.render('index', { title: 'Express' });
});
```