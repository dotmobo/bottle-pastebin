<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Bottle-pastebin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="An anonymous pastebin">
    <meta name="author" content="mobo">
	
    <!-- Le styles -->
    <link href="/static/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="/static/css/bootstrap-responsive.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/bottle-pastebin.css" />

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="/static/js/html5shiv.js"></script>
    <![endif]-->

   </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="/">Bottle-pastebin</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="/">Home</a></li>
              <li><a href="/about">About</a></li>
              <li><a href="mailto:pastebinbottle@gmail.com">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
