# RetweetBot using Apache OpenWhisk

This is a very small serverless funcion (5 lines of Python code!) that auto retweets tweets with a specific hashtag ('#InServerless' for example). This function is configuared to be triggered every 5 minutes. I have used Apache OpenWhisk for the development, but this code can easliy be migrated (with minor tweeks though) to any of the other cloud platforms.

# Prerequisites

1. <a href = "https://console.bluemix.net/openwhisk/cli">OpenWhisk CLI</a>
2. Python 3
3. 'TwitterFollowBot' python module
4. IBM Cloud account (for deploying the OpenWhisk action)

# The Architecture

<p align = "center"> <img src = "https://user-images.githubusercontent.com/23396903/32169674-86ecb944-bd97-11e7-9a01-5399fafb3181.png"> </img> </p>

The serverless function (OpenWhisk action) is triggered using the periodic trigger. It triggers the action based on a specific time (5 minutes) and will retweet the latest tweets with ‘#InServerless’ in it. One can either choose a pattern or write a cron expression.   
 
# Developing the RetweetBot 

The Twitter API provides programmatic access to read and write Twitter data, create a new tweet, read user profile and follower data, retweet, and more. For this, first you should must create a Twitter application (see https://dev.twitter.com/) and note down the OAuth credentials for the bot configuration.

The Twitter API in Python can be accessed using TwitterFollowBot Python module. Using this module, you can do much more than just retweeting like auto-following, auto-liking. For developing TwitterBot, you must install the module into a folder rather than the default bin directory. For that, use the following command:

```pip install --target <target_folder> TwitterFollowBot```

For configuring the bot, you should create a “config.txt” file and fill in the following information so that the bot can connect to the Twitter API. Here are the entries in the ”config.txt” file:

OAUTH_TOKEN:

OAUTH_SECRET:	            

CONSUMER_KEY:             

CONSUMER_SECRET:

TWITTER_HANDLE: <your twitter handle>

ALREADY_FOLLOWED_FILE: already-followed.txt

FOLLOWERS_FILE: followers.txt

FOLLOWS_FILE: following.txt

USERS_KEEP_FOLLOWING:

USERS_KEEP_UNMUTED:

USERS_KEEP_MUTED:

The files “already-followed.txt”, ”followers.txt” and ”following.txt” contain the respective twitter ids. You must create these files - you can leave them empty, though. The rest of fields may also be left empty. 

# Apache OpenWhisk

Apache OpenWhisk is an open source serverless cloud platform that executes functions in response to events at any scale. 

# RetweetBot using OpenWshik:

Once the wsk CLI (Command Line Interface) is installed and a zip file containing the TwitterFollowBot dependency & code is ready, follow these steps:

1. Create and Update the action:

Create an OpenWhisk action and upload the code using the following command:

```wsk action create tweetBot --kind python:3 OpenWhisk.zip```

2. Invoke the function:

There are two ways of invoking an action: Blocking mode - similar to a synchronous call, Non-Blocking mode - similar to an asynchronous call. Invoke the created action using the following command (Non-Blocking mode):
 
 ```wsk action invoke tweetBot```
 
3. Check for the result:
 
Since we invoked the function in a non-blocking mode (because we haven’t added the ‘--blocking’ parameter), the command returned immediately, but it is executing in the background. Use the following command to check the result:
 
```wsk activation result <action id>```
```Ex: wsk activation result f4df0d1dcb12488396978d2cda832b09```

4. Check out the logs:

Command to check out the logs:

One can check out for the logs using the following command:

```wsk activation logs <action id>```
```Ex: wsk activation logs f4df0d1dcb12488396978d2cda832b09```

# Migration to other serverless platforms

Migrating this action to other platfroms like AWS Lambda or Azure functions is not very difficult. It can be done with minor tweeks to the code. In the AWS lambda perspective, the main function just needs to be modified to accpet two parameters: event, context and the rest would work fine. Similarly, with minor changes this code can easily be floated to a different cloud provider.



