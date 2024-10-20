
# Paige Turner's Books Shop

## Project Goals

### Overview

### Goals

## User Experience Design

### Strategy Design

#### User Requirements and Expectations

#### User Stories and Epics

##### Epic: Viewing and Navigation

- [1](https://github.com/paddyw11/paiges-books/issues/1) - As a user, I want to browse through different categories of books to find what interests me.

- [2](https://github.com/paddyw11/paiges-books/issues/2) - As a user, I want to see a list of offers on the homepage

- [3](https://github.com/paddyw11/paiges-books/issues/3) - As a user, I want to be able to view detailed information about a specific book, including its description, author, price and category.

- [4](https://github.com/paddyw11/paiges-books/issues/4) - As a user, I want to be able to navigate easily between different pages of the website using a main navigation menu.

##### Epic: Registration and User Accounts

- [5](https://github.com/paddyw11/paiges-books/issues/5) - As a user, I want to register for an account so that I can save my favourite books and manage my orders.

- [6](https://github.com/paddyw11/paiges-books/issues/6) - As a registered user, I want to be able to log in to my account using my email address/username and password.

- [7](https://github.com/paddyw11/paiges-books/issues/7) - As a registered user, I want the option to reset my password if I forget it.

- [8](https://github.com/paddyw11/paiges-books/issues/8) - As a registered user, I want to update my account information such as my shipping address or payment details.

##### Epic: Sorting and Searching

- [9](https://github.com/paddyw11/paiges-books/issues/9) - As a user, I want to be able to sort books by with filters such as price, author, or genre/category.

- [10](https://github.com/paddyw11/paiges-books/issues/10) - As a user, I want to see search results displayed in a clear and organised manner, with relevant book information. 

##### Epic: Puchasing and Checkout

- [11](https://github.com/paddyw11/paiges-books/issues/11) - As a user, I want to add books to my shopping cart and view the contents before proceeding to checkout.

- [12](https://github.com/paddyw11/paiges-books/issues/12) - As a user, I want to be able to easily edit the quantity of books in my cart or remove items altogether.

- [13](https://github.com/paddyw11/paiges-books/issues/13) - As a user, I want to enter my payment information securely and complete the checkout process.

- [14](https://github.com/paddyw11/paiges-books/issues/14) - As a user, I want to receive confirmation of my order via email, including details such as order number and payment.

##### Epic: Administration

- [15](https://github.com/paddyw11/paiges-books/issues/15) - As an admin, I want to be able to add new books to the website, including details such as title, author, category and price.

- [16](https://github.com/paddyw11/paiges-books/issues/16) - As an admin, I want to be able to edit existing book listings to update information such as price, availability, or description.

- [17](https://github.com/paddyw11/paiges-books/issues/17) - As an admin, I want to be able to delete books from the website if they are no longer available or in stock.

- [18](https://github.com/paddyw11/paiges-books/issues/18) - As an admin, I want to manage user accounts, including the ability to view user details, reset passwords, and deactivate accounts if necessary.

- [19](https://github.com/paddyw11/paiges-books/issues/19) - As an admin, I want to receive notifications or alerts for new orders placed on the website, including details such as order number and customer information.

 As a ... i want to be able to .... so that i can ...

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

![Image](/documentation/media/images/bug1.PNG)

Once I had creatd a new table for genre, in order to make it a manyToMany relationshipe i hadn't updated the search query to reflect that. I needed to update to correct syntax.

### HTML Validation Error on allauth password validator form

---

![Image](/documentation/media/images/bug3.PNG)

---

![Image](/documentation/media/images/bug3-1.PNG)

---

I was receiving a W3C validation error on this due to the django password validator and crispy_forms displaying the password vlaidation hints as a list within a small element. 
I attempted to create the form using crispy fields for the other fields and custom design the password1 field. 
![Image](/documentation/media/images/bug3-2.PNG)I decided it was a better UX to leave the whole form as a crispy fomr in the end. 


## Credits: 


[Image](https://pixabay.com/photos/people-woman-coffee-cafe-couch-1421097/) by [Yerson Retamal](https://pixabay.com/users/voltamax-60363/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1421097) from [Pixabay](https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1421097)