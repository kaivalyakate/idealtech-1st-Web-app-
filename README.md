# idealTech - My personal first web application

Idealtech is a my personal project, a web application for managing, ordering domestic workers for households (Workers which you can hire for doing some of your households). The whole project runs on Django framework Version 1.9.5 along with certain dependencies. 

### Deployment 

This web applicaton is live on 6522kaivalya.pythonanywhere.com - (Not Live Now - 2021)
It is being hosted on pythonanywhere.com 
Great website for hosting your apps and testing personal django projects in production. 

## Built With
```
* [Django](https://www.djangoproject.com/) - The web framework 
* [Bootstrap](https://getbootstrap.com/) - Front End Template with heavy editing from my side
* Crispy forms used with bootstrap for enhancing the look of the forms as forms are an integral part of this website.
* Din't focus a lot on the frontend part of the Application as it is my first Project and wanted to build a good and powerful backend. ;-;
```

## Application-Operations
There are 3 sections basically in which I have divided the working of the application:
1. Skilled Professionals Registration:
  * So a worker bascially signs up on the webiste with the help of company's representative.
  * He/She gets their unique ID.
  * Now this ID is the only important vector which is used for identifying a worker as a part of the system.
  * Done, Now they're registered with us. They start working.
2. Domestic Workers Ordering:
  * Now if its your first time, you will need to login. So we keep track of all the users on the application. 
  * There is a simple form with (6-7) fields maybe ;-;. Fill up the form, now our representatives get your order on a specific url which     is the backend part and thus the team can assign a professional to the user.
3. Worker Management:
  * Now we have this Database consisting of all the information about the workers. We can use this for a lot of constructive purposes.
    (Data is the new Oil :))
  * Once the worker starts working with the user. The user has to come online and enter the worker ID which the worker shares with the user,       we do that too and review the maid. (Reviewing is compulsory)
  * This is how we form relationships between user and the workers.
This web application isn't fully automated, there are humans in the process but as it is my first project, I have tried to implement everything I can. :))

## Code-Referencing

You can reference this django code for learning and implementing certain tasks in your web application like form filling, sending emails (Refer the features section for more details) through your web app, etc. other application properties.

## Versioning

Would love to make new additions to this project as and when time would permit. :)))


## Acknowledgments

* Youtube Django Tutorials helped a lot.
* This was intially a startup idea but someone was already doing this successfully and this idea was too naive at that point of time, so   dropped it for a while.
* Ping me up on twitter if there's something you wanna tell me.
