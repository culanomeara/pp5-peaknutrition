# **Peak Nutrition**

Peak Nutrition is a full stack ecommerce application that provides a platform for the nutritionist, Trish Garrett to sell and marklet her services and products. The intention of the site is to provide a simple, intuitive, visually appealing and user-friendly platform for users. The intended target audience is anyone with an interest in general nutrition, sports performance nutrition. The target audience will mostly be individuals, coaches, teachers, athletes, team managers.

The application implements user authorisation and full CRUD functionality, allowing users to create, update, read and delete products and articles stored in a relational database management system.

The site also features a back-end admin dashboard that allows a superuser to monitor, edit, delete products, articles, orders, users. 

Link to the live site - https://peak-nutrition.herokuapp.com/

# Contents

* [**Portfolio Five**](<#portfolio-five>)
    * [Objective](<#objective>)
    * [Site User Goals](<#site-user-goals>)
    * [Site Owner Goals](<#site-owner-goals>)
    * [**Project Management**](<#project-management>)
        * [GitHub Project Board](<#github-project-board>)
        * [Database Schema](<#database-schema>)
* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Site Design](<#site-design>)
    * [Site Structure](<#site-structure>)
    * [Typography](<#typography>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
        * [**Homepage**](<#homepage>)
            * [Navigation](<#navigation>)
            * [Carousel](<#carousel>)
            * [Intro](<#intro>)
            * [Most Popular projects List](<#most-popular-projects-list>)
        * [**Project and Post Pages**](<#projects-and-posts-pages>)
            * [Project](<#projects>)
            * [Post](<#posts>)
        * [**Project and Post Details**](<#project-and-post-details>)
            * [Project Details](<#project-details>)
            * [Post Details](<#post-details>)
            * [Like Unlike Project](<#like-unlike-project>)
            * [Project Comments](<#project-comments>)
            * [Comment Form](<#comment-form>)
            * [Form Validation](<#form-validation>)
        * [**Authorisation**](<#authorisation>)
            * [Sign Up](<#sign-up>)
            * [Sign Up Notification](<#sign-up-notification>)
            * [Sign In](<#sign-in>)
            * [Sign In Notification](<#sign-in-notification>)
            * [Sign Out](<#sign-out>)
            * [Sign Out Notification](<#sign-out-notification>)
        * [**Create A Project or Post**](<#create-a-project-or-post>)
            * [Create Form](<#create-form>)
            * [Create Notification](<#create-notification>)
        * [**Update Project or Post**](<#update-project-or-post>)
            * [Update Form](<#update-form>)
            * [Update Notification](<#update-notification>)
        * [**Delete Project or Post**](<#delete-project-or-post>)
            * [Delete Confirmation Page](<#delete-confirmation-page>)
            * [Delete Notification](<#delete-notification>)   
        * [**403 Page**](<#403-page>)
    * [**Future Features**](<#future-features>)
        * [Admin Area](<#admin-area>)
        * [User Profile](<#user-profile>)
        * [Notification feature](<#notification-feature>)
        * [Categories](<#categories>)
        * [Search feature](<#search-feature>)
        * [Print Project instructions](<#print-project-instructions>)
        * [Enhanced Form Validation](<#enhanced-form-validation>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks](<#frameworks>)
    * [Software](<#software>)
    * [Libraries](<#libraries>)
* [**Testing**](<#testing>)
    * [**User Story Tests**](<#user-story-tests>)
    * [**Validator Tests**](<#validator-tests>)
        * [W3C (HTML)](<#w3c-html>)
        * [W3C (CSS)](<#w3c-css>)
        * [PEP8 (Python)](<#pep8-python>)
    * [**Input Validation Tests**](<#input-validation-tests>)
        * [Post project Form Tests](<#post-project-form-tests>)
        * [Edit project Form Tests](<#edit-project-form-tests>)
        * [Comment Form Tests](<#comment-form-tests>)
    * [**Additional Tests**](<#additional-tests>)
        * [Manual Tests](<#manual-tests>)
        * [Automated Tests](<#automated-tests>)
        * [Responsive Tests](<#responsive-tests>)
        * [Browser Tests](<#browser-tests>)
        * [OS Tests](<#os-tests>)
        * [Lighthouse Tests](<#lighthouse-tests>)
    * [**Bugs**](<#bugs>)
        * [Resolved](<#resolved>)
        * [Unresolved](<#unresolved>)
* [**Setup and Deployment**](<#setup-and-deployment>)
    * [**Setup**](<#setup>)
    * [**Deployment to Heroku**](<#deployment-to-heroku>)
    * [**Final Production Deployment**](<#final-production-deployment>)
    * [**Forking**](<#forking>)
    * [**Cloning**](<#cloning>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
    * [**Code**](<#code>)

# Portfolio Five

## Objective

This project was created for Portfolio Project Five submission for the Full Stack Software Development Higher National Diploma at [Code Institute](https://codeinstitute.net/). Amongst other assessment criteria, the project had to be built using HTML, CSS, JavaScript, Python and Django and feature full ecommerce ability, CRUD functionality and user authorisation. The project also had to be planned and designed using Agile methodologies. 


[Back to top](<#contents>)

## Site User Goals

- To

[Back to top](<#contents>)

## Site Owner Goals

- Provide a stable and enjoyable user experience that encourages product purchase.
- The platform should be accessible, welcoming and appealing to new users.
- Content should be high quality and well structured.
- Provide fully responsive application with straightforward navigation
- Ensure only authenticated and valid users have access to CRUD functionality

[Back to top](<#contents>)

## Project Management

### Github Project Board

Agile methodology was used to plan and design the Peak Nutrition application. User stories were created on GitHub and added to the board in the TODO section. They then moved across the board into IN PROGRESS when they were being actioned, and then into the DONE section when they were completed. This helped greatly in tracking progress and organising and allocating work.

[Back to top](<#contents>)

### Database Schema

Database scheme was drawn up using [App Diagrams.net](https://app.diagrams.net/). The scheme was used to plan the database models and fields. It also helped to display the relationships between the models and how they interact. Peak Nutrition consists of five custom models and one generic - Product, Article, Contact, Subscription, Category and User. I did not include Keywords or Userlevels in my final design.

![Peak Nutrition Database Scheme](media/readme/images/db_model_design.jpg)

[Back to top](<#contents>)

# User Experience UX

## User Stories

In terms of project management, user stories are an integral part of the software development creative process. Peak Nutrition consists of ?? user stories. 

A full list of user stories can be found in the [Peak Nutrition GitHub Project Board](https://github.com/users/culanomeara/projects/4/views/1).

[Back to top](<#contents>)

## Site Design 

The Peak Nutrition app features a simple and user friendly design. Balsamiq was used to do some wireframe mock ups for the homepage and projects/posts pages.

-Index.html wireframe

![Peak Nutrition index.html](media/readme/images/aww_wireframe_index.png)

-Projects.html wireframe

![Peak Nutrition projects.html](media/readme/images/aww_wireframe_projects_page.png)

[Back to top](<#contents>)

## Site Structure 

Site structure is one that users will be quite familiar with a top navigation bar. However, some content is hidden / restricted to users who are not logged in. The main pages / templates of Peak Nutrition include - Home, Products, About, Contact. Site users can freely and easily browse the various pages using the site navigation bar which is visible at the top of each page. The nav bar options automatically change depending on whether a user is signed in or not to allow for easy and intuitive site navigation.

[Back to top](<#contents>)

## Typography 

Peak Nutrition uses [Google Fonts](https://fonts.google.com/) for the site typography. The specific fonts are [Raleway](https://fonts.google.com/specimen/Raleway). Raleway is clear but defined with a clear, functional form.

[Back to top](<#contents>)

# Features

## Existing Features

### Homepage

The homepage is the first page of the site that a user will see when they navigate to the [Peak Nutrition URL](https://peak-nutrition.herokuapp.com/). It's designed to be eye catching to users and to quickly summarise the intention of the site. It is also a central location for all users to view the various product categories. 

- Navigation bar

![Navigation bar](media/readme/images/index.jpg)

- Who We are
![Who We are](media/readme/images/index_who_we_are.png)

- Free Consult Call
![Free Consult Call](media/readme/images/index_most_popular_projects.jpg)

[Back to top](<#contents>)

#### Navigation

Site navigation is present at all times on every page of the site in the form of header nav bars. These navigational elements change depending on whether a user is logged in or not. Non logged in users only have viewing access to projects and posts. They are unable to comment or like a project. These elements are also fully responsive and the header collapses to become a mobile menu on small screen sizes.

- Navigation Bar - Not Logged in - Full

![Navigation Bar - Not Logged in - Full](media/readme/images/navbar_not_logged_in_full.png)

- Navigation Bar - Logged in - Full

![Navigation Bar - Logged in - Full](media/readme/images/navbar_logged_in_full.png)

- Navigation Bar - Mobile

![Navigation Bar - Mobile](media/readme/images/navbar_mobile.png)

[Back to top](<#contents>)

#### Free Consult Call

The homepage Free Consult Call-to-action is the large eye-catching section which is just underneath the site title. The call-to-action is only displayed on the homepage. It is used to catch the users attention, and to attract users to click. It features a large button and title.

- Free Consult Call

![Free Consult Call](media/readme/images/index_carousel.jpg)

[Back to top](<#contents>)

#### Hexagon Product Display

The unique styling draws the users attention. Each hexagon represents one category of product/service. Clicking on a hexagon will brign you directly to the product page for that specific cateogry.

- Hexagons

![Hexagons](media/readme/images/index_who_we_are.png)

[Back to top](<#contents>)

### Product Pages

#### Products
The product page is a template used to display the list of ALL projects or a specific category of products. Each product has a summary. These pages are available for all users to view, including non-logged in users. The main purpose of the page is to display the brief product overview. Users will generally navigate to a full product detail page by clicking on the product from the product card. As the user has now shown a specific interest in the product, all the information about the product is displayed on the details page.

- Product Page

![Product page](media/readme/images/projects_page.png)

[Back to top](<#contents>)

### Product Details

#### Product Details
The product details page is a template used to display the full information on a product. Each product has a details page. These pages are available for all users to view, including non-logged in users. The main purpose of the page is to display the product information and price. Users will generally navigate to a full product page by clicking the product image on the project card either on the product page. As the user has now shown a specific interest in the product, all the information about the product is displayed here.

- Product Details

![Product Details](media/readme/images/project_details.png)

[Back to top](<#contents>)

#### Form Validation

The built-in validation is used to validate the comment form. The form is checked for required fields and passwords require a level of difficulty. A notification appears on the users screen to advise them about the failure. The user can then rectify their mistake and submit the form again. When the comment form is filled out correctly the form submits successfully.

- Form Validation: Field Required

![Form Required Field](media/readme/images/form_validation_field_required.png)

- Form Validation: Password

![Form Password](media/readme/images/form_validation_password_issue.png)

[Back to top](<#contents>)

### Authorisation

#### Sign Up

A user can navigate to the sign-up page via the site navigation bars if they are not logged in. The Peak Nutrition sign up page is a built-in template from the [Django Allauth Package](https://django-allauth.readthedocs.io/en/latest/installation.html). Allauth provides the basic functionality for the user authorisation used in Peak Nutrition. Once a user submits the form correctly, they are redirected back to the homepage as a logged in user. For each action, they are notified of that action: via a message at the top of the page. These messages can be removed by clicking on the X.

- Sign Up Form
![Sign Up](media/readme/images/sign_up_form.png)

- Sign Up Notification

![Sign Up Notification](media/readme/images/sign_up_notification.png)

[Back to top](<#contents>)

#### Sign In

A user can navigate to the Sign in page via the site navigation bars if they are not already signed in. As with the Sign-Up page, it's a built-in form. The styling of the sign in page is very similar to the rest of the user authorisation pages. The colour scheme and layout are consistent, but the form and page heading are different. Once the sign in form is submitted correctly the user is redirected to the homepage as a logged in user.

- Sign In Form

![Sign In](media/readme/images/sign_in_form.png)

- Sign In Notification

![Sign In Notification](media/readme/images/sign_in_notification.png)

[Back to top](<#contents>)

#### Sign Out

A user can navigate to the Sign Out page via the site navigation bars if they are logged in. They are prompted on this page to confirm if wish to log out. Upon confirmation the user is logged out and redirected to the homepage. If they click on Cancel, they are brought back to the previous page. 

- Sign Out Confirmation Page

![Sign Up](media/readme/images/sign_out_confirm.png)

- Sign Out Notification

![Sign Out Notification](media/readme/images/sign_out_notification.png)

[Back to top](<#contents>)

### Add a new product

#### Add form

The Add Product template form is a page which features a product form to enable users to add a product to the Peak Nutrition site. This page is only visible to logged in users and appears in the navigation menu. The page features similar styling to the rest of the site for consistency.

- Product Add Form

![Product Add Form](media/readme/images/project_create_form.png)

[Back to top](<#contents>)

#### Add product notification

When a user adds a product successfully, a toast message appears confirming the submission of the project/post.

- Add product notification

![Add product notification](media/readme/images/project_create_notification.png)

[Back to top](<#contents>)

### Edit Product

The Edit product page is available to logged in users. The Edit option appears below the summary on the list page and details page. When the Update option is clicked, the user is navigated to the edit product page. The page styling and content is exactly the same as the add page. The only difference is the form is prefilled out with the content. The user can then use this form to edit the content and submit the amendments to overwrite the previous content.

- Edit Product Form

![Edit Product Form](media/readme/images/project_update_form.png)

#### Edit Notification

If a user successfully submits the update form the page is refreshed. A message is displayed to the user which confirms the successful form submission. The user is redirected to the list page for products.

- Edit Product Notification

![Edit Product Notification](media/readme/images/project_update_notification.png)

[Back to top](<#contents>)

### Delete Product

A user can delete their product easily from the relevant list page or details page. This option is only visible to a superuser. If a user clicks on delete, a delete confirmation toast is displayed.

- Delete Product

![Delete Product](media/readme/images/update_delete.png)

[Back to top](<#contents>)

#### Delete Notification

If a user deletes a product, a notification is displayed to the user at the top of the page. This notification confirms the deletion of the project. The user can hide this notification by clicking the x icon. 

- Delete Confirmation Notification

![Delete](media/readme/images/delete_notification.png)

[Back to top](<#contents>)

### 404 Page

The 403 page is triggered when a user navigates to a site URL which doesn't exist. This could be because of a number of reasons, mainly if they mistype something.

- 404 Page

![404 Page](media/readme/images/403.png)

[Back to top](<#contents>)

## Future Features

I believe the Peak Nutrition site has a lot of potential for expansion in the future. The basic functionality is there for the MVP but there are many features I would like to add in the future.

### Admin Area

I would like to add an admin area for administrators so they wouldn't have to log into the Django admin area. The basic concept would be to have an admin navigation option on the main site navigation bar that is only visible to users with admin privileges. Navigating to this page would open a dashboard for administrators to view the basic site stats like number of site visits. This page would have to be secured and hidden from other site users.

[Back to top](<#contents>)

### User Profile

Another feature that would improve the site would be a customisable user profile section. In this section a user would be able to edit their profile. They would also be able to add a profile picture/avatar. This would greatly improve the social element of the app and the overall user experience. 

[Back to top](<#contents>)

### Categories

The Peak Nutrition site currently features category fields which don't have any usable functionality. These fields were originally intended to group projects together to be displayed in project category lists/sections.

[Back to top](<#contents>)

### Enhanced Form Validation

I would like to add enhanced form validation above the built-in ones. Validation for typos, numbers instead of letters, etc

[Back to top](<#contents>)

# Technologies Used

## Languages

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - Provides the basic content and structure for the site.
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Provides the styling for the site.
* [Python](https://www.python.org/) - Provides the functionality for the site.
* [JavaScript](https://www.javascript.com/) - Provides the timeout functionality for the messages/notifications
* [Git](https://git-scm.com/) - Provides the version control system for the site.

[Back to top](<#contents>)

## Frameworks

* [Bootstrap](https://getbootstrap.com/) - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains HTML, CSS and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
* [Django](https://www.djangoproject.com/) - Django is a free and open-source, Python-based web framework that follows the model–template–views architectural pattern.

[Back to top](<#contents>)

## Software

* [GitHub](https://github.com/) - An internet hosting service used for version control. Used to host the Peak Nutrition repository and for the project board used for project management and user stories.
* [GitPod](https://www.gitpod.io/) - A cloud development environment used as the primary site code editor.
* [Heroku](https://dashboard.heroku.com/) - A cloud platform used to host the Peak Nutrition full stack application.
* [Stripe](https://stripe.com/) - Ecommerce software and APIs to accept payments, send payouts, and manage shop orders
* [Amazon Web Services](https://aws.amazon.com/) - a cloud platform that allows you to store and retrieve static files
* [Slack](https://slack.com/intl/en-gb/) - An online instant messaging program used for site feedback and guidance from the [Code Institute](https://codeinstitute.net/) community.
* [App Diagrams](https://app.diagrams.net/) - An online diagram software used for the database schemas.
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - A set of web developer tools built directly into the chrome browser. Used for responsiveness tests and further testing.
* [Google Fonts](https://fonts.google.com/) - A web-based font service by Google used to supply the site typography.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - An open-source automated testing tool used for site tests.
* [Responsive Design Checker](https://responsivedesignchecker.com/) - An online testing tool used for responsive site testing.
* [Am I Responsive](https://ui.dev/amiresponsive) - An online testing tool used for responsive site testing.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - An online suite of evaluation tools used to test the site for accessibility.

[Back to top](<#contents>)

## Libraries

This is a list of the Python / Django libraries used in this project.

* [asgiref](https://github.com/django/asgiref) - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
* [Django](https://www.djangoproject.com/) - A python package for the Django framework.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - An integrated set of Django applications addressing user authentication, registration and account management.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - A Django package that provides tags and filters to control the rendering behaviour of Django forms.
* [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.
* [oauthlib](https://github.com/oauthlib/oauthlib) - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
* [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter for Python.
* [PyJWT](https://pyjwt.readthedocs.io/en/latest/) - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
* [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages to support use of the OpenID decentralized identity system.
* [pytz](https://pypi.org/project/pytz/) - A Python package for world timezone definitions, modern and historical.
* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - A Python package for OAuthlib authentication support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python.

[Back to top](<#contents>)

## Testing

The testing approach is as follows:
1. Manual testing of user stories
2. Automated testing

### User Story Tests

### Users
1. I want to get inspiration for DIY wooden projects

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/ | Home page main body loads with carousel, site introduction and most popular projects | Works as expected |

2. As a user, I can view all projects

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/projects | All projects should be visible | Works as expected |

3. As a user, I can view all posts 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/posts | Posts page main body loads with all Posts displayed | Works as expected |

4. As a site user I want to be able to view the most popular Projects

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/ and scroll down to most popular Projects section | Projects with likes appear in three panels on homepage | Works as expected |

5. As a user, I want to be able to view details of a particular project

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/ and click on project image on carousel or most popular projects section | click on any picture to be brought to details page | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/projects/ and click on a project to see project details page | User can see projects displayed and click on any picture to be brought to details page | Works as expected |

6. As a user, I want to be able to view details of a particular post

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/posts/ and click on a post to see post details page | User can see posts displayed and click on any picture to be brought to details page | Works as expected |

7. As a site user, I can log in

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ and submit user details | User is logged in | Works as expected |

8. As a site user, I want to be able to create a new Project

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/project_create or click on Create New Project nav link | Create New Project Form is displayed | Works as expected |
Enter details on Create New Project Form page then click submit| New project is created | Works as expected |

9. As a site user, I want to be able to create a new Post

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/post_create or click on Create New Post nav link | Create New Post Form is displayed | Works as expected |
Enter details on Create New Post Form page then click submit| New post is created | Works as expected |

10. As a site user, I can view comments on an individual project

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/Projects/ | Projects page loads | Works as expected |
Click on Projects card for more information | Projects detail page loads with comments section at the bottom of the page | Works as expected |
Logged in users can fill out the comment form and click submit button | Comment is submitted for approval | Works as expected |

11. As a site user, I can comment on projects
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/Projects/ | Projects page loads | Works as expected |
Click on Projects card for more information | Projects detail page loads with comments section at the bottom of the page | Works as expected |
Logged in users can fill out the comment form and click submit button | Comment is submitted | Works as expected |

12. As a site user, I want to be aware of logged in status

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to any page and check nav bar | Logged in users see sign out link | Works as expected |
Navigate to any page and check nav bar | Unauthenticated users see nav bar with Sign Up and Sign In options | Works as expected |

13. As a site user, I want to be able to update one of my projects

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/projects or navigate to project details page of specific project they want to update | Logged in user that is also author of that project will see Update option under project summary | Works as expected |
Click on Update | Project Update form will be displayed with pre-filled content shown | Works as expected |
Click on Submit | Project updates will be submitted, and confirmation message shown | Works as expected |

14. As a site user, I want to be able to update one of my Posts

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/posts or navigate to post details page of specific post they want to update | Logged in user that is also author of that post will see Update option under post summary | Works as expected |
Click on Update | Post Update form will be displayed with pre-filled content shown | Works as expected |
Click on Submit | Post updates will be submitted, and confirmation message shown | Works as expected |

15. As a site user, I want to be able to Delete one of my projects

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/projects or navigate to project details page of specific project they want to delete | Logged in user that is also author of that project will see Delete option under Project summary | Works as expected |
Click on Delete | Project Delete Confirm Page will be displayed | Works as expected |
Click on Confirm | Project will be deleted, and confirmation message shown | Works as expected |

16. As a site user, I want to be able to Delete one of my posts

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/accounts/login/ or click on Login nav link and submit user details | User is logged in | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/posts or navigate to post details page of specific post they want to delete | Logged in user that is also author of that post will see Delete option under post summary | Works as expected |
Click on Delete | Post Delete Confirm Page will be displayed | Works as expected |
Click on Confirm | Post will be deleted, and confirmation message shown | Works as expected |

### Site admin
17. As a site admin, I can create a project or post in the backend to manage site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Project add + button | Project add form is presented to user in backend | Works as expected |
Fill out form with relevant details and click save | New project is added to database | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Post add + button | Post add form is presented to user in backend | Works as expected |
Fill out form with relevant details and click save | New post is added to database | Works as expected |

18. As a site admin, I can update a project or post in the backend to manage site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Project table button | Project list is displayed | Works as expected |
Click on Project you want to update | Project details are displayed | Works as expected |
Update details and click save | Project is updated to database | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Post table button | Post list is displayed | Works as expected |
Click on Post you want to update | Post details are displayed | Works as expected |
Update details and click save | Post is updated to database | Works as expected |

18. As a site admin, I can delete a project or post in the backend to manage site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Project table button | Project list is displayed | Works as expected |
Click on Project you want to delete | Project details are displayed | Works as expected |
Click delete | Project is deleted from database | Works as expected |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Post table button | Post list is displayed | Works as expected |
Click on Post you want to delete | Post details are displayed | Works as expected |
Click delete | Post is deleted from database | Works as expected |

18. As a site admin, I can remove comments so that I can filter out objectionable comments

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Comments table | A list of all comments is displayed | Works as expected |
Select the comment(s) for removal | Comment is selected | Works as expected |
Select "delete selected comments" from dropdown menu and click "go" | Confirm delete notice appears | Works as expected |
Click "Yes, I'm sure" | Comment(s) deleted | Works as expected |

19. As a site admin, I can create categories to organise site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Category Add+ button | Category add form is presented to user in backend | Works as expected |
Fill out form with relevant details and click save | New category is added to database | Works as expected |

19. As a site admin, I can update categories to organise site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Category table | Category list appears | Works as expected |
Click on Category you wish to update | Category name and type fields appear | Works as expected |
Make updates and click save | Updated category is saved to database | Works as expected |

20. As a site admin, I can delete categories to organise site content

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://adventureswithwood.herokuapp.com/admin logged in as superuser | Admin dashboard is displayed | Works as expected |
Click on Category table | Category list appears | Works as expected |
Select Category(s) you wish to delete | Category(s) are selected | Works as expected |
Select "delete selected categorys" from dropdown menu and click "go" | Confirm delete notice appears | Works as expected |
Click "Yes, I'm sure" | Category(s) deleted | Works as expected |

### Site Owner

21. As a site owner, I want the user to come to a custom 403 error page tha explains in simple language what has gone wrong if they enter a URL that they don't have permission to access

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to an Update page by adding ".../update" to post/project url | Reroute to a customised 403 page | Works as expected |

22. As a site owner, I want the user to come to a custom 404 error page tha explains in simple language what has gone wrong if they enter a URL that does not exist

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to a url that does not exist | Reroute to a customised 404 page | Works as expected |

### Automated testing

Automated testing was done using the Django's TestCase module. 

### Performing tests on various devices

The website was tested using Google Chrome Developer Tools Toggle Device Toolbar to simulate viewports of different devices.

The website was tested on the following devices:
- MacBook Pro with macOS 13.2
- MS Surface Pro Windows 10
- Samsung s20 with Android v13

## Validator Tests

### W3C (HTML)

When the Peak Nutrition site was first tested with the [W3C HTML Markup Validation Service](https://validator.w3.org/) it showed two errors and some info messages. The errors were missing alts for images. The info messages were all related to a stray semi-colon and a stray / after hr.

[HTML link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fadventureswithwood.herokuapp.com%2F)

![HTML Validation Test](media/readme/images/html_validator_test.jpg)

- Projects Page

![HTML Validation Test Projects Page](media/readme/images/html_validator_test_projects.jpg)

- Posts Page

![HTML Validation Test Projects Page](media/readme/images/html_validator_test_posts.jpg)

- Sign Up Page

![HTML Validation Test Sign Up Page](media/readme/images/html_validator_test_signup.jpg)

[Back to top](<#contents>)

### W3C (CSS)

The Peak Nutrition CSS stylesheet has been assessed using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) by direct input. Unfortunately there were two errors shown for grid template areas proj1 and proj2. I removed the offending references and the site passed the test.

[CSS link](https://jigsaw.w3.org/css-validator/validator#css)

![CSS Validation Test](media/readme/images/css_validator_test.jpg)

[Back to top](<#contents>)

### PEP8 (PYTHON)

I used the new [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to test all of the Peak Nutrition python code files. 

#### urls.py
Passed without error

#### settings.py
Has two max line length errors

#### forms.py
Passed without error

#### models.py
Passed without error

#### admin.py
Passed without error

#### views.py
Passed without error

#### tests.py
Passed without error

[Back to top](<#contents>)

## Input Validation Tests

### Create project Form Tests

[Back to top](<#contents>)

### Edit project Form Tests

[Back to top](<#contents>)

### Comment Form Tests

[Back to top](<#contents>)

## Additional Tests

### Manual Tests

[Back to top](<#contents>)

### Automated Tests

Three automated tests were set up in the file tests.py to test views: Home, Project and Post. All tests passed.

[Back to top](<#contents>)

### Responsive Tests

[Back to top](<#contents>)

### Browser Tests

#### Site tested in:

- Google Chrome

![Google Chrome](media/readme/images/browser_test_chrome.jpg)

- Apple Safari

![Apple Safari](media/readme/images/browser_test_safari.jpg)

- Mozilla Firefox

![Mozilla Firefox](media/readme/images/browser_test_firefox.jpg)

- Microsoft Edge

![Microsoft Edge](media/readme/images/browser_test_edge.jpg)

[Back to top](<#contents>)

### OS Tests

Site was developed on an Apple MacBook using iOS v13.2

#### Site tested in:

- Windows 10 PRO

![Windows 10 PRO](media/readme/images/os_test_windows.jpg)

[Back to top](<#contents>)

### Lighthouse Tests

#### Mobile

[Mobile Link](https://pagespeed.web.dev/analysis/https-adventureswithwood-herokuapp-com/mx8dwnnzdu?form_factor=mobile)

![Screenshot Mobile](media/readme/images/lighthouse_test_mobile.jpg)

#### Desktop

[Desktop link](https://pagespeed.web.dev/analysis/https-adventureswithwood-herokuapp-com/mx8dwnnzdu?form_factor=desktop)

![Screenshot Desktop](media/readme/images/lighthouse_test_desktop.jpg)

[Back to top](<#contents>)

## Bugs

### Resolved 

**Bug** | **Cause** | **Outcome**
------------ | ------------ | ------------ |
Images were showing up tiny on Projects page | Missing semi-colon in CSS file | Resolved |
All users were able to access CRUD functions  | Didn't have authentication set up across the site | Resolved |
When updating project or post, crash occurred if you didn't add new image  | Image already in DB wasn't returned back when saving | Used request.files to pull image in and then sent back when saved. Resolved |

[Back to top](<#contents>)

### Unresolved

There are no unresolved bugs that I am aware of!

[Back to top](<#contents>)

## Setup and Deployment

### Setup

_In GITHUB:_

 Once the repository has been created using the Code Institute student template....

1. Install Django and supporting libraries. 
    * Django and gunicorn --> pip3 install 'django<4' gunicorn
    * Supporting libraries --> pip3 install dj_database_url psycopg2
    * Cloudinary libraries --> pip3 install dj3-cloudinary-storage

2. Create a requirements file --> pip3 freeze --local > requirements.txt

3. Create your project: in this case adventures-with-wood

4. Create an app using command --> python3 manage.py startapp APP_NAME

5. Add it to installed apps --> INSTALLED_APPS = [
    …
    'APP_NAME',
]

6. Save file and migrate changes using command --> python3 manage.py migrate

7. Run server to test

8. Commit and push changes to github

[Back to top](<#contents>)

### Deployment to Heroku

1. Create Heroku Account
2. In Heroku dashboard: go to Create new app.
3. Give your app a unique name.
4. Select region --> EUROPE
5. Click create App.
6. Go to Database App/Resources/ Add-ons and search and click 'Heroku Postgres'.
7. Go to the Settings tab, scroll down to Config Vars and select Reveal Config Vars and copy text.

_IN GITPOD..._

8. Create env.py file on top of level directory.
9. Import os library
10. set environment variables --> os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
11. Add in a secret key --> os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"

_IN HEROKU ..._

12. Add secret Key to config vars --> SECRET_KEY, “randomSecretKey”

_IN GITPOD / IN SETTINGS.PY_

13. Reference env.py file -->
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env

14. Remove the secret key and replace it with the following variable--> SECRET_KEY = os.environ.get('SECRET_KEY')

15. Comment out the DataBases section -->
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

 16. Add new database section -->
 DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

17. In the terminal, save files and make migrations --> python3 manage.py migrate

_GETTING STATIC AND MEDIA FILES STORED ON CLOUDINARY..._

18. Create a cloudinary account, and copy the CLOUDINARY_URL from the dashboard.

19. Add url to env.py -->
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"

_BACK IN HEROKU ..._

20. Paste Cloudinary URL to Heroku Config Vars -->
Add to Settings tab in Config Vars e.g. COUDINARY_URL, cloudinary://************************

21. In config vars, add DISABLE_COLLECTSTATIC, 1. This will be rmeoved before final deployment.

_IN GITPOD / SETTINGS.PY_

22. Install Cloudinary libraries -->
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'cloudinary',
    …,
]

23. Tell Django to use Cloudinary to store media and static files -->
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

23. Link file to templates -->
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

24. Change template directory to templates array -->
TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
]

25. Add heroku hostname to ALLOWED_HOSTS-->
ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]

_IN GITPOD..._

26. Create 3 new folders: media, static and templates

27. Create procfile and add code -->
web: gunicorn PROJ_NAME.wsgi

28. In terminal --> Add, Commit and Push

_IN HEROKU ..._

29. Deploy manually -->  Github as deployment method, on main branch

[Back to top](<#contents>)

### Final Production Deployment

_IN GITPOD / ENV.PY_

1. Set DEVELOPMENT variable to 0!
2. Add a few more settings--> X_FRAME_OPTIONS = 'SAMEORIGIN'
    * Without this, the summer note editor would no longer work when we deploy the project. This is due to Cross-Origin Resource Sharing, which tells the browser which resources are permitted to be loaded.
3. Save, add and commit as "deployment commit", and push to github.

_IN HEROKU..._

4. In reveal config vars, remove DISABLE_COLLECTSTATIC environment variable.

5. Go to deploy tab, scroll down to the end and deploy our branch! 

6. Your app has been deployed to heroku!

[Back to top](<#contents>)

### Forking

You can Fork the Repository. This makes a copy of the original repository on our Github account so you can make changes without affecting the original repository.
1. Log into GitHub and locate the GitHub repository you want.
2. Click on the "Fork" button which is in the top right corner.
3. You will now have a copy of the original repository in your GitHub account.

[Back to top](<#contents>)

### Cloning

1. Log into GitHub and locate the GitHub repository you want.
2. Under the repository name, click "Code" button which will produce a dropdown menu.
3. Where it says Clone, copy the link below.

[Link to deployed site](https://adventureswithwood.herokuapp.com/)

[Back to top](<#contents>)

# Credits

## Content

All content that was copied from other sites such as Instructables https://www.instructables.com/ has been credited on the relevant page itself on the site.

[Back to top](<#contents>)

## Readme
Readme structure adapted from/inspired by:
- Matthew Hurrell https://github.com/Matthew-Hurrell/viva-la-nacho/blob/main/README.md
- John Constant https://github.com/johnConstant/CI_PP4_Projects_site/blob/main/README.md
- Stephanie Crocker https://github.com/stephaniecrocker91/for-the-love-of-food/blob/main/README.md

[Back to top](<#contents>)

## Media

Images were sourced on Google from various sites including Instructables and Pinterest. Creative commons images were used where possible.

The site logo/placeholder image was created using Canva https://www.canva.com/

[Back to top](<#contents>)

## Code 

I used the "I think therefore I blog" walk through project as a starting point and template. I created a blog like page that presented projects and posts. I added to the base code with custom views, models, html and CSS. I used the JS script for message timeouts from that blog and modified it for my own requirements.

I watched a good few of Codemy videos for Django blog building https://www.youtube.com/watch?v=m3efqF9abyg

The home page carousel was from bootstrap docs https://getbootstrap.com/docs/4.0/components/carousel/

I got the idea for the MOST POPULAR projects in this CI PP4 project by John Constant https://ci-pp4-recipe-site.herokuapp.com/

[Back to top](<#contents>)