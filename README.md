
# Paige Turner's Books Shop

## Project Goals

### Overview

### Goals

## User Experience Design

### Strategy Design

#### User Requirements and Expectations

#### User Stories and Epics

##### Epic: Viewing and Navigation

- 1.1 - As a user, I want to browse through different categories of books to find what interests me.

- 1.2 - As a user, I want to see a list of offers on the homepage

- 1.3 - As a user, I want to be able to view detailed information about a specific book, including its description, author, price and category.

- 1.4 - As a user, I want to be able to navigate easily between different pages of the website using a main navigation menu.

##### Epic: Registration and User Accounts

- 2.1- As a user, I want to register for an account so that I can save my favourite books and manage my orders.

- 2.2- As a registered user, I want to be able to log in to my account using my email address/username and password.

- 2.3- As a registered user, I want the option to reset my password if I forget it.

- 2.4- As a registered user, I want to update my account information such as my shipping address or payment details.

##### Epic: Sorting and Searching

- 3.1- As a user, I want to be able to sort books by with filters such as price, author, or genre/category.

- 3.2 - As a user, I want to see search results displayed in a clear and organised manner, with relevant book information.

- 3.3 - As a user, I want to be able to save a list of books that i wish to purchase/read. 

##### Epic: Puchasing and Checkout

- 4.1 - As a user, I want to add books to my shopping cart and view the contents before proceeding to checkout.

- 4.2 - As a user, I want to be able to easily edit the quantity of books in my cart or remove items altogether.

- 4.3 - As a user, I want to enter my payment information securely and complete the checkout process.

- 4.4 - As a user, I want to receive confirmation of my order via email, including details such as order number and payment.

- 4.5 -  As a user, i want to be able to view my order history.

##### Epic: Administration

- 5.1 - As an admin, I want to be able to add new books to the website, including details such as title, author, category and price.

- 5.2 - As an admin, I want to be able to edit existing book listings to update information such as title, author, category and price.

- 5.3 - As an admin, I want to be able to delete books from the website if they are no longer available or in stock.

- 5.4 - As an admin, I want to be able to add new authors to the website, including details such as name, nationailty and a short bio.

- 5.5 - As an admin, I want to be able to edit existing author listings to update information.

- 5.6 - As an admin, I want to be able to delete authors from the website.

### Features

-   **Viewing and Navigation Features**

    -   __Feature 1 - Consistent Look and Feel__

        The site's navigation bar and footer appear on every page framing the page's content. The fonts and colours are consitent throughtout providing an intuitive experience for the user. The novagation bar is respoonsive with a burger style icon replacing the nav links on smaller screens. 

        <br><strong>Fig 01-A.  Desktop example</strong><br><br>
        ![F01 Large Screen](documentation/media/images/features/f1-nav-bar-lg.png)
        
        <br><strong>Fig 01-B.  Mobile example</strong><br><br>
        ![F01 Small Screen](documentation/media/images/features/f1-nav-bar-sm.png)
    
    -   __Feature 2 - User Logged in Indicator__

        The user can easily see if they are logged in at any given time. The user icon will be solid when a user is logged in and emplty if not. The text undernaeth the symbol will display 'My Account' is not logged in and the user's username when logged in. 

        <br><strong>Fig 02-A.  Logged Out</strong><br><br>
        ![F02 Logged Out](documentation/media/images/features/f2-user-indicator-out.png)

        <br><strong>Fig 02-B.  Logged In</strong><br><br>
        ![F02 Logged In](documentation/media/images/features/f2-user-indicator-in.png)

    -   __Feature 3 - Home Page__

        The home page is dominated with an image and some header text infomrming the user of the site's main purpose with a prominent call to action button. The navigation section contains links for clear procedures.  

        <br><strong>Fig 03-A.  Home Page</strong><br><br>
        ![F03 Home Page](documentation/media/images/features/f3-home-page.png)

    -   __Feature 4 - Books Views__

        The books view allow the user to easily scroll through a number of books and allows sorting by several attriburtes including price, genre and author. Using a card feature, each card displays the front cover of each book and includes a few details about each title. A scroll to top button allows the user to return to the start of the list. A pagination feature is inluded to allow users to navigate through a longer list of titles. 

        <br><strong>Fig-04-A.  All books view</strong><br><br>
        ![F04 Books Views](documentation/media/images/features/f4-all-books-view.png)

    -   __Feature 5 - Search, Filer and Sort__

        There are options available to the user on the navigation bar to filter the list of books and allow them to restrict the results to items they are particularly interested in. For example, the user can choose to just see books for a particular genre or just discounted prints using the 'offers' link. The user can also restrict the list of results based on a search term which will attempt to find matches in the book titles, description, genres and authors name.

        <br><strong>Fig-05-A.  Search by key term</strong><br><br>
        ![F05 Search by key term](documentation/media/images/features/f5-search-key-term.png)

        <br><strong>Fig-05-A.  Search by genre</strong><br><br>
        ![F05 Search by genre](documentation/media/images/features/f5-search-genre.png)

        <br><strong>Fig-05-A.  Search by offers </strong><br><br>
        ![F05 Search by offers ](documentation/media/images/features/f5-search-offers.png)

    -   __Feature 6 - Offers__

        The dedicated page displays all books that have a discount offer applied. Each book will also be marked with a discount in the main list views.    

        <br><strong>Fig-06-A.  Offers Page</strong><br><br>
        ![F06 Offers](documentation/media/images/features/f6-offers-page.png)

    -   __Feature 7 - Book Details__

        When a user clicks on a book they are taken to a book detail page. This will display the full details of the book including short description, a full blurb (opened in a modal), the number of pages, the price, the author and the genre(s). The user can add the book to their basket from this view and can also browse 'Similar Books' which displays books in the same genre(s).  

        <br><strong>Fig-07-A.  Book Detail View</strong><br><br>
        ![F07 Book Detals](documentation/media/images/features/f7-book-detail-view.png)

    -   __Feature 8 - Author Detials__

        Whilst in a book detail view, the user can click one the authors name to     
        reach the author bio page which includes the author's nationalisty and a short bio description. 

        <br><strong>Fig-08-A.  Author Detail View</strong><br><br>
        ![F08 Author Details](documentation/media/images/f8-author-details.png)

    -   __Feature 9 - Wishlist__

        When viewing a book user's can select a bookmark icon to add the respective book to their wishlist. For a logged in user they can see a wishlist option in the navigation links to take them to their wishlist view. The books added to the wishlist will be retained for a user when they return to their log in. Users can remove the book from the wishlist by clicking the bookmark icon. The icon changes style when books are in, or out of the wishlist.     

        <br><strong>Fig-09-A.  Book can be added to the wishlist from the book detail page.</strong><br><br>
        ![F09 Wishlist](documentation/media/images/features/f9-wishlish-out.png)

        <br><strong>Fig-09-B. Books added to the wishlist can be viewd on the wishlist page.</strong><br><br>
        ![F09 Wishlist View](documentation/media/images/features/f9-wishlist-view.png)

    -   __Feature 10 - Error Pages__

        The site has custom error pages to give a better user experience.     

        <br><strong>Fig-10-A.  404 Error Page</strong><br><br>
        ![F10 Error Pages](documentation/media/images/features/f10-error-page-404.png)

    -   __Feature 11 - Onscreen Messages__

        Users can be notified of certain actions with on-screen messages. They can receive messages for actions such as successful logging in, logging out, adding a book to the basket and a successful checkout. 

        <br><strong>Fig-11-A.  Logged In</strong><br><br>
        ![F11 Onscreen Messages - Logged In](documentation/media/images/features/f11-a-logged-in.png)

        <br><strong>Fig-11-B.  Logged Out</strong><br><br>
        ![F11 Onscreen Messages - Logged Out](documentation/media/images/features/f11-b-logged-out.png)

        <br><strong>Fig-11-C.  Added to Basket</strong><br><br>
        ![F11 Onscreen Messages - Added to Basket](documentation/media/images/features/f11-c-added-to-basket.png)

        <br><strong>Fig-11-D.  Order Success</strong><br><br>
        ![F11 Onscreen Messages - Order SUccess](documentation/media/images/features/f11-d-order-success.png)

-   **Registration and Role-based Authorisation Related Features**

    -   __Feature 12 - Sign Up, Login and Logout__

        Users can register for the site by following the register link and completing the sign up form. Once they have registred they can log in to their profile, and save reading lsits and order history as necessary. 

        <br><strong>Fig-12-A. Sign Up Form</strong><br><br>
        ![F12 Sign Up Form](documentation/media/images/features/f12-a-sign-up-form.png)

        <br><strong>Fig-12-B. Log In</strong><br><br>
        ![F12 Log in Page](documentation/media/images/features/f12-b-log-in-page.png)

        <br><strong>Fig-12-C. Log Out</strong><br><br>
        ![F12 Log out Page](documentation/media/images/features/f12-c-log-out-page.png)

    -   __Feature 13 - Role Based Actions__

        Role based actions allow users access to certain features or action based on their role type. Any logged in user has access to the wishlist page. Logged in admin users have several features to create new books or authors, edit existing ones or delete information. The addtional features are available to users under the profile icon. 
        
        <br><strong>Fig-13-A.  Loggged In User</strong><br><br>
        ![F13 Loggged In User](documentation/media/images/features/f13-a-logged-in-user-options.png)

        <br><strong>Fig-13-B.  Loggged In Admin</strong><br><br>
        ![F13 Loggged In Admin](documentation/media/images/features/f13-b-admin-options.png)


    -   __Feature 14 - User Profile__

        Logged in users can click to save delivery details to their profile when completing an order. These details will be retained in the user's profile page and will pre-populate data-fields in subsequent checkout pages. 

        <br><strong>Fig-14-A.  Profile Page</strong><br><br>
        ![F14 Profile Page](documentation/media/images/features/f14-a-profile.png)

        <br><strong>Fig-14-B.  Pre-filled Checkout Page</strong><br><br>
        ![F14 Pre-filled Checkout Page](documentation/media/images/features/f14-b-pre-filled-checkout.png)

-   **E-commerce related features**

    -   __Feature 15 - Shopping Basket__

        Users can add books they intend to puchase in the shopping basket page. Users can continue shopping and their books will be retained in the basket until they are ready to complete the checkout.     

        <br><strong>Fig-15-A.  Shopping Basket</strong><br><br>
        ![F15 Shopping Basket](documentation/media/images/features/f15-shopping-basket.png)

    -   __Feature 16 - Checkout__

        When the user is ready to complete their purchase they can navigate to the checkout page and enter the delivery details and billing details. If they have saved their personal detials the form will be pre-populated (see Feature 14).
        Payments are securely handled by Stripe's widgets in the site. Webhooks are used to ensure that transactions are handled correctly in the case of any problems encountered during payment processing.

        <br><strong>Fig-16-A.  Checkout</strong><br><br>
        ![F16 Checkout](documentation/media/images/features/f16-checkout.png)

    -   __Feature 17 - Order Confirmation and History__

        Once an order is sucessfully complete users are taken to tne order confimtiaon page which details the items ordered and the delivery address. Logged in users can see their order history. 

        <br><strong>Fig-17-A.  Order Confirmation Page</strong><br><br>
        ![F17 Order confirmation page](documentation/media/images/features/f17-a-order-confirmation-page.png)

        <br><strong>Fig-17-B.  Order History</strong><br><br>
        ![F17 Order History](documentation/media/images/features/f17-b-order-history.png)


-   **Data Admin Features**

    -   __Feature 18 - Book Management__

        Text    

        <br><strong>Fig-18-A.  Loggged In</strong><br><br>
        ![F18 Book management](documentation/media/images/f2-user-indicator-in.png)

    -   __Feature 19 - Author Management__

        Text    

        <br><strong>Fig-19-A.  Loggged In</strong><br><br>
        ![F19 Author Management](documentation/media/images/f2-user-indicator-in.png)

### Structure Plane

#### Website Structure - Wireframes

<details>
<summary>Home Page</summary>

![Home Page](/documentation/media/images/home_page.png)
</details>

<details>
<summary>Author Bio Page</summary>

![Author](/documentation/media/images/author1.png)
</details>

<details>
<summary>Book Management</summary>

![Book Management](/documentation/media/images/book_management.png)
</details>

<details>
<summary>Sign Up</summary>

![Register](/documentation/media/images/register.png)
</details>

<details>
<summary>Checkout</summary>

![Checkout](/documentation/media/images/checkout.png)
</details>

<details>
<summary>Offers</summary>

![Offers](/documentation/media/images/offers.png)
</details>

<details>
<summary>Basket</summary>

![Basket](/documentation/media/images/basket.png)
</details>

<details>
<summary>books</summary>

![books](/documentation/media/images/books.png)
</details>

<details>
<summary>Book Detail</summary>

![Book Detail](/documentation/media/images/book_detail.png)
</details>


#### Database Design
---

I adopted a crows foot ER design to portray the relationship between each table and it's respective fields. 

![Paige's Books ERD](/documentation/er-diagram/Paige's-Books-ERD.png)


## Technologies Used

### Languages Used 

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/) 
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used  

-   [Google Fonts:](https://fonts.google.com/) used for the Lato and Old Standard TT fonts.
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web page
-   [Git:](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/) has been utilied as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking their progress on a Kanban board.
-   [Django v4.2](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
s
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication.
-   [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image handling
-   [jquery library](https://code.jquery.com/jquery-3.4.1.min.js) - for various pieces of functionality including adding and removing items from the shopping cart and handling the increment and decrement of the quantity control.
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.
-   [Stripe](https://js.stripe.com/v3/) used for secure payments (referenced in base.html).
-   [Django Countries](https://pypi.org/project/django-countries/) used on checkout page to pass valid country code to Stripe.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db.
-   [Amazon S3](https://aws.amazon.com/s3/) used to store static files and images.
-   [Boto3](https://pypi.org/project/boto3/) the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
-   [django_storages](https://django-storages.readthedocs.io/en/latest/) used to connect django to S3.
-   [Heroku](https://www.heroku.com) - used to host the deployed application.
-   [Balsamiq:](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [LucidChart](https://www.lucidchart.com/pages/?) was used to create the Entity Relationship diagrams for the application data model


## Testing

For More information on testing [see here](https://github.com/paddyw11/paigesbooks/blob/main/TESTING.md)

## Bugs

### Search query field error

---

![Image](/documentation/media/images/bug1.png)

Once I had creatd a new table for genre, in order to make it a manyToMany relationshipe i hadn't updated the search query to reflect that. I needed to update to correct syntax.

### HTML Validation Error on allauth password validator form

---

![Image](/documentation/media/images/bug3.png)

---

![Image](/documentation/media/images/bug3-1.png)

---

I was receiving a W3C validation error on this due to the django password validator and crispy_forms displaying the password vlaidation hints as a list within a small element. 
I attempted to create the form using crispy fields for the other fields and custom design the password1 field. 
![Image](/documentation/media/images/bug3-2.png)I decided it was a better UX to leave the whole form as a crispy fomr in the end. 


## Credits: 


[Image](https://pixabay.com/photos/people-woman-coffee-cafe-couch-1421097/) by [Yerson Retamal](https://pixabay.com/users/voltamax-60363/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1421097) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1421097)