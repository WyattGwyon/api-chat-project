# Creating a Flask API to connect to Mongo for chat database

This project will involve creating an API that will read and write to a MongoDB for a chat database. We are using Flask in Python to create our API endpoints and we will find sources for our users and dialogue either from slack or text documents. We only need sample dialogue so it isn't necessary to use real chat messages.

After we connect and populate our database. We will apply NLTK to evaluate the probabiltiy of positive to negative sentiment expressed in the chat. 

## Connect to Flask to Mongo
This is an important first step for the first time. We want to be able to enter and retrieve user information easily.

Now, we also want to think about three things simultaneaously. 
- Our Flask API
- The structure of our Mongo DB
- The content we will populate our chat database with.

Forutnately, because Mongo is JSON native we can expect to have an easier time handling it. And Mongo being a non-relational database will be more flexible with information that we enter. 

## Choosing our Sample Dialogue
The content to fill our database with can be more playful. We don't need actual chat material, just a lot of dialogue. Taking into consideration that scripts contain dialogues and characters we could look it a script for a television program or movie.

We have some candidates:
- Monty Python's Life of Brian (make a reference to Python's namesake)
- The Big Lebowsk (always a favorite)
- An Episode of Twin Peaks (because I'm always looking for an excuse...)

It turns out that we found subtitles for the Big Lebowski first which was easy to clean. We will use it to populate our database but we won't be too perfectionist about it. Chats are generally not to clean texts anyway.

## MongoDB organization
Being more accustomed to SQL, the concept of relating information is not obvious in Mongo. But we are going to make two colletions. One for Users, another for chat and another for Messages that will contain user and chat id numbers.

## Challenges in this project
- Connecting for the first time many different components: Mongo, Flask, Python, functions wrapped in flask decorators in order to create an API that passes arguments to pymongo methods that then return objects to the aforesaid functions wrapped in flask that give an output to the terminal, url page, and mongo database, and using jupyter notebook as a presentation format on top of that.
- Easy enough to say, suprisingly easy to accomplish but please don't ask me to explain it all again.
- Next stop...rocket science.

## Things to improve
We really need to take our time with this. The time spent reading documentation further complicated and clarified the process in equal measures. It seems that taking a step beyond 

- make the appropriate `_id` connections between `user/chat/message`
- create an `update` endpoint that works
- create an `get` endpoint that works
- use the `NLTK` to analize the sentiment probability of each user and each chatroom

## Overall
It feels good to get this paper plane to fly. But we have more work to do before we can call ourselves pilots.