# Online video store   
###### Second django project from "Python developer" course in programming school "IT technologies itProger" https://itproger.com  

## In the site realised online store with video courses:  

- ### Each video course could has a lessons.  

Lessons database has "foreign key" field that allows to attach every lesson with a specific video course. On the site lessons are displayed on the page of specific course (which are belonged). On the site each lesson has individual url by the "slug field" name. Process of adding lessons on the site realised only through the admin panel.

- ### Courses on the site.  

In database, courses have "boolean field" for realisation access permissions for checking user has paid subscription or not. If guest or user with free subscription would move to a pay course page that he don't see the lessons list and couldn't move to a lesson page of this course.  

- ### Profile, registration, authorisation and password recovery.  

Site has a realisation of these functions. On the profile page user could change his data. If you want that works the password recovery function, you got to change the variables in `settings.py` (that displaying below) on yours.  

``
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'mezorservice123@gmail.com'  
EMAIL_HOST_PASSWORD = 'dsfasdgdfafdss'  
EMAIL_PORT = 587  
``

- ### Templatly realisation of payments.  

`courses/views.py` has the `tarrifs_page()` function where realised a template for payment through the https://fondy.ru/.  

## On the website were used:
- Fonts: "EB Garamond", "Oswald" from https://fonts.google.com/ .
- Styles: "Bootstrap4" and own-styles.

###### Creator: Dmitry Shelukhin

### P.S.

Many thanks to Georgy Dudar and programming school "IT technologies itProger" for learning and experience.
