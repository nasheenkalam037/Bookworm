ECE 651 -- Final Project
========================

Group Members
--------------
* Jonathan Shahen (jmshahen [at] uwaterloo [dot] ca)
* Syeda Noor Jaha Azim (snjazim [at] uwaterloo [dot] ca)
* Chetan Joshi (c4joshi [at] uwaterloo [dot] ca)
* Nasheen Kalam (n2kalam [at] uwaterloo [dot] ca)

Project Description
------------------
Books are a shared passion among a large population of the world.
According to BookMap:
> The worldwide market value at consumer prices at around €122 billion (US$143.4 billion).
> Book publishing is bigger than music, video games, or filmed entertainment, roughly equal to newspaper publishing, yet clearly smaller than in-home video entertainment, which is almost double that size.
> (BookMap)[https://www.wischenbart.com/page-59]

This level of commitment and enjoyment of novels has inspired our group to create a product that helps
customers locate where they can find books, and creates a custom recomendation system, using machine learning, to 
provide an "endless" list of book recommendations.

The Minimum Viable Product (MVP) includes the following:
* Details about books scraped from public sources
* A website users can sign-up and have custom new book recommendations provided for them
* Each book will have links to where that book can be purchased from
* Interactive website that users can use to browse for new books and to tell us which books they have liked or disliked

Our context diagram can be found here: [Context Diagram](documents/context-diagram/context-diagram.pdf).
In this diagram we show the following subsystems that we will need to create for our MVP:
* Frontend
    * This is the webserver code that is the public interface that customers will interact with
* Database
    * Here we store all information on the books we have scrapped from public sources
    * We also store relavant information about each user and their book preferences
    * All machine learning data is extracted from the data stored here
* Machine Learning Newest Model
    * This is the newest instance of our learned machine learning model
    * We save this instance so that we do not need to re-train the model for every request
        * Training can take multiple minutes up to 30 minutes
* Machine Learning Module
    * Periodically we will re-train the machine learning model when data has been added or modified to the database
    * The machine learning model uses an AutoEncoder to create our recommendation model

Our UI Mockup can be found here: [UI Mockup](documents/ui-mockup/ui-mockup.pdf).

---

Agile Development
-----------------
We are following a SCRUM model for our software development.

Scrum is a form of Agile development where a product is produced at the end of a "sprint".
Our sprint length is 1 week long.
At the start of a sprint we have a sprint meeting wher we outline all of the sprint tasks we want to complete and any extra tasks that cannot fit within the sprint are placed into a backlog.

We have modified the scrum ceremonies as follows:

* Sprint Planning -- this occurs at the start of a sprint and where the team outlines all user stories/task that need to be completed for that specific sprint
* Daily Scrum -- we will not be having any daily scrum meetings, due to time constraints and commitments outside of this class
* Sprint Review -- at the end of every sprint there is a sprint review meeting where each member of the team summarizes there work and brings forth any concerns or comments they have.

User Stories
------------
Below are a list of Customr level User Stories that we will use to help us create the end product.

* As a [role], I want [feature] so that [reason].
* 


Testing Methodology
-------------------


