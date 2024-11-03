# Paige's Books Testing

## Manual Testing

|  Test Number 	|   User Story	|   Expected Outcome/action | Test Outcome  |
|---	|---	|---	|---	|
|  T01 	|   2.1	| User can complete the registration form by providing a username, email address and password.  	|  Pass  	| 
|  T02	|   2.1	|  user is notified if they have complete the form incorrectly.	|  Pass 	|
|  T03	| 2.2  	|  User can successfully login using their credentials. 	|  Pass     |
|  T04	|   2.2	|   User is notified if they have provided incorrect credentials. 	| Pass  	|   
|  T05	|   1.5	|   User can detect if they are logged in based on the user icon and username field, if logged in the user icon is solid and their username appears underneath.	|  Pass 	|
|  T06  |   2.3	| User can reset their password on the login screen should they have forgotten it.  	        |     Pass         	|
|  T07  | 2.2  	|  User can logout of their account using the navigation item under the user icon to logout. 	        |      Pass        	|
|  T08  |   2.4	| User can update personal details on their profile page  	        | Pass             	|
|  T09  | 4.5  	| User can see their order history on their profile page.  	        |    Pass          	|
|  T10  |   1.1	| A list of books are dipsplayed on the screen.	        |    Pass          	|
|  T11  |   1.1	|  A  number of options are available to filter the books.	        |      Pass        	|
|  T12  |   3.1	|  Books can be sorted either be genre or by price.      |      Pass        	|
|  T13  |   1.2 + 1.4	|  A navigation link leads users to the books with a discount applied.	        |      Pass        	|
|   T14   |   1.2    |  In the main books view, if a book has a discount applied a discount label will be displayed.         |
|  T15  |  1.3 + 3.2 	|   Book's information is displayed alongside its image. User can find, title, author, a short description, number of pages and a price. |     Pass        	|  
|  T16  |   1.3	|   Upon clicking a 'read more' button users can find a longer blurb of each title.	        |       Pass       	|
|  T17  |   1.4	|   When navigation links are clicked, users are taken to the respective page/have the respective filter applied to the view.	        |       Pass       	|
|  T18  |   3.3 + 1.4	|  A logged in user can save a book to a wishlist when they click on the bookmark icon. The icon will change style and the book will appear in a wishlist page.	        |      Pass       	|
|  T19  |   4.1	|  When on a book's detail page, a user can add a book (or multiple copies) to their shopping basket. The value on the basket icon will increase. 	        |      Pass       	|
|  T20  |   4.2	|   In the basket page, users can increase or decrease the number of copies, or remove books from the basket. When an action is complete, the value of the basket changes accordingly.	        |      Pass        	|
|  T21  |   4.3	|   Users can navigate to the chekout from the basket page. Here once payment credentials are completed, users can make a secure payment. Users are informwed of the success of failure of their payment with messags. 	        |      Pass        	|
|  T22  |   	|   	        |      Pass        	|


## Code Validation

### HTML

#### Index Page


![Book Detail](/documentation/media/images/testing/validator/html-val-index.png)


#### Signup

![Book Detail](/documentation/media/images/testing/validator/html-val-signup.png)


#### Log In

![Book Detail](/documentation/media/images/testing/validator/html-val-login.png)


#### Log Out

![Book Detail](/documentation/media/images/testing/validator/html-val-logout.png)


#### Profile

![Book Detail](/documentation/media/images/testing/validator/html-val-profile.png)


#### Basket

![Book Detail](/documentation/media/images/testing/validator/html-val-basket.png)


#### Books

![Book Detail](/documentation/media/images/testing/validator/html-val-books.png)


#### Book Detail

![Book Detail](/documentation/media/images/testing/validator/html-val-books-1.png)


#### Genre Filter

![Book Detail](/documentation/media/images/testing/validator/html-val-genre-fitler.png)


#### Offers

![Book Detail](/documentation/media/images/testing/validator/html-val-books-offers.png)


#### Authors

![Book Detail](/documentation/media/images/testing/validator/html-val-author-1.png)


#### Checkout

![Book Detail](/documentation/media/images/testing/validator/html-val-checkout.png)


#### Checkout Success

![Book Detail](/documentation/media/images/testing/validator/html-val-checkout-success.png)


#### Contact Page

![Book Detail](/documentation/media/images/testing/validator/html-val-contact.png)


#### FAQs Page

![Book Detail](/documentation/media/images/testing/validator/html-val-faqs.png)


#### About Us

![Book Detail](/documentation/media/images/testing/validator/html-val-about.png)


### CSS

https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpaiges-books-9655906010a2.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en


### Python

Author Model Contact Page

![Author Model](/documentation/media/images/testing/validator/py-val-author-model.png)

#### Author Url

![Author Url](/documentation/media/images/testing/validator/py-val-author-url.png)

#### Basket Contexts

![Basket Contexts](/documentation/media/images/testing/validator/py-val-basket-contexts.png)

#### Basket Url

![Basket Url](/documentation/media/images/testing/validator/py-val-basket-url.png)

#### Basket Views

![Basket Views](/documentation/media/images/testing/validator/py-val-basket-views.png)

#### Books Form

![Books Form](/documentation/media/images/testing/validator/py-val-books-forms.png)

#### Books Model

![Books Model](/documentation/media/images/testing/validator/py-val-books-models.png)

#### Books Url

![Books Url](/documentation/media/images/testing/validator/py-val-books.url.png)

#### Books Views

![Books Views](/documentation/media/images/testing/validator/py-val-books.views.png)

#### Checkout Forms

![Checkout Forms](/documentation/media/images/testing/validator/py-val-checkout-forms.png)

#### Checkout Models

![Checkout Models](/documentation/media/images/testing/validator/py-val-checkout-models.png)

#### Checkout Url

![Checkout Url](/documentation/media/images/testing/validator/py-val-checkout-url.png)

#### Checkout Webhook Handler

![Checkout Webhook Handler](/documentation/media/images/testing/validator/py-val-checkout-webhook-handler.png)

#### Checkout Webhook

![Checkout Webhook](/documentation/media/images/testing/validator/py-val-checkout-webhook.png)

#### Contact Views

![Contact Views](/documentation/media/images/testing/validator/py-val-contact-views.png)


