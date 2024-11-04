# Paige's Books Testing

## User Story Testing

### Epic: Viewing and Navigation

-   1.1 - I know when "As a user, I want to browse through different categories of books to find what interests me" user story is complete when I can follow navigation links, filter options or use the search field to find books in different genres. - PASS

-   1.2 - I know when "As a user, I want to see a list of offers on the homepage" user story is complete when following the link to offers nav link I can only see books with a discount included. When browsing I can also see an offer label on the respective books that have a discount.  - PASS

-   1.3 - I know when "As a user, I want to be able to view detailed information about a specific book, including its description, author, price and Genre" user story is complete when clicking on a book I am presented with a dedicated page displaying more information about a book I choose. I can see the title, the author, a short description, the number of pages, the price the genre and the ability to read a longer blurb about the title. - PASS

-   1.4 - I know when "As a user, I want to be able to navigate easily between different pages of the website using a main navigation menu" user story is complete when navigation is seamless between pages using the ever-present navigation bar or side menu when on smaller devices. The navigation bar clearly displays intuitive navigation around the site.   - PASS

### Epic: Registration and User Accounts

-   2.1- I know when "As a user, I want to register for an account so that I can save my favourite books and manage my orders" user story is complete when I am able to provide credentials and then use those credentials to log in. Once logged in I can easily mark a book to save to my wish list. I can also save my information in my profile page and have that information handy when placing an order. - PASS

-   2.2- I know when "As a registered user, I want to be able to log in to my account using my email address/username and password" user story is complete when using the credentials I used when I registered, I can log in to the site. Once logged in I can access previous orders, update my profile and see my list of saved books. - PASS

-   2.3- I know when "As a registered user, I want the option to reset my password if I forget it" user story is complete when I can click the 'Forgotten Password' link and follow the steps from the email to reset my password.  - PASS

-   2.4- I know when "As a registered user, I want to update my account information such as my shipping address or payment details" user story is complete when once I am logged in I can update my address in my profile area. This information will be readily available to me at the checkout. - PASS

### Epic: Sorting and Searching

-   3.1- I know when "As a user, I want to be able to sort books by with filters such as price, author, or genre/Genre" user story is complete when I am browsing the books views I can use the sort feature and put the books in an order of price (high to low/low to high), genre(a-Z/Z-A) or author(A-Z/Z-a by surname) when selecting the sort the books are displayed in the respective order - PASS

-   3.2 - I know when "As a user, I want to see search results displayed in a clear and organised manner, with relevant book information" user story is complete when I can clearly see the information which is relevant for the book and have the ability to expand the information by opening the respective book's detail page.  - PASS

-   3.3 - I know when "As a user, I want to be able to save a list of books that I wish to purchase/read" user story is complete when as a logged in user I can mark as book to be added to my wishlist by clicking on the bookmark icon on the book's detail page. I am able to access the wishlist when I am logged in to see which books I have in my wishlist. I can easily remove the books from the wishlist by clicking the icon again. - PASS

### Epic: Purchasing and Checkout

-   4.1 - I know when "As a user, I want to add books to my shopping basket and view the contents before proceeding to checkout" user story is complete when I can click on the add to basket button on the book's details page. I can select more than one copy to be added to the basket. In the basket page I can update the number of copies I wish to purchase or remove a book from the basket. If I decide I wish to add more books to the basket, I can return to the shop to find more books. The basket's contents will remain saved until I am ready to purchase. From the basket I can continue my purchasing by clicking on the secure checkout.  - PASS

-   4.2 - I know when "As a user, I want to be able to easily edit the quantity of books in my basket or remove items altogether" user story is complete when I can amend the number of copies of a respective book by increasing or decreasing the quantity. I can also remove the book from the basket by clicking remove. - PASS

-   4.3 - I know when "As a user, I want to enter my payment information securely and complete the checkout process" user story is complete when I am able to complete the checkout of the basket by entering the billing/shipping address and payment information. The details use the third party payment vendor to conduct the transaction. I am updated to the status of the payment and informed whether the payment has been successful or failed.  - PASS

-   4.4 - I know when "As a user, I want to receive confirmation of my order via email, including details such as order number and payment" user story is complete when I receive an email with the confirmation of my order being placed complete with all the necessary information of the order, including costs, the address for delivery and the books purchased. - PASS

-   4.5 - I know when "As a user, I want to be able to view my order history" user story is complete when in my user profile I am presented with details of my previous purchases. I am able to click on an order and be presented with all the order's information. - PASS

### Epic: Administration

-   5.1 - I know when "As an admin, I want to be able to add new books to the website, including details such as title, author, Genre and price" user story is complete when I can navigate to the book management page and input all of the new book's information into the form. I can confirm the book has been added correctly by finding the book in the book shop's search feature.  - PASS

-   5.2 - I know when "As an admin, I want to be able to edit existing book listings to update information such as title, author, Genre and price" user story is complete when I can click edit on the book's detail page, update the necessary information on the form, click save and be presented with the book's updated information.  - PASS

-   5.3 - I know when "As an admin, I want to be able to delete books from the website if they are no longer available or in stock" user story is complete when I can click delete on the book's detail page and then confirm the book has been removed by searching for it in the site. - PASS

-   5.4 - I know when "As an admin, I want to be able to add new authors to the website, including details such as name, nationality and a short bio" user story is complete when I can navigate to the author management page and add a new author to the site. I can then add a book and attribute the title to the newly added author. - PASS

-   5.5 - I know when "As an admin, I want to be able to edit existing author listings to update information" user story is complete when I can navigate to the author management page, select edit on the respective author , make the updates and click save. I can check the author's information to see if the updates have saved.  - PASS

-   5.6 - I know when "As an admin, I want to be able to delete authors from the website" user story is complete when I select delete from the author management page.  - PASS


## Manual Feature Testing

**All Pages**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Navigation bar | Responsive | Test on various devices | Collapses on smaller screens | Pass |
| Logo | Leads to Index page when clicked on | Click on the logo | Leads to index page | Pass |
| Navbar links | Lead to relevant pages | Click on the links | Correct pages open | Pass |
| Search bar | Displays search queries | Input query into the form | Shows results for a given query | Pass |
| Basket total | Correct basket total displays | Add Books to basket | Correct basket total displays | Pass |
| All books dropdown | Shows pre-set Book filters | Click on the dropdown | Displays Books sorted/filtered to requested filter | Pass |
| Genre dropdown | Displays Books for a relevant Genre | Click on the dropdown links | Displays Books for a relevant Genre | Pass |
| Free delivery banner | Shows a correct free delivery threshold | Open all pages | Free Delivery Threshold displayed | Pass |
| Footer | Displayed on all pages | Open all pages | Footer appears | Pass |
| Toasts | Appear after an action is performed | Perform action | Correct toast/message appears | Pass |

**Index Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Image | Displays on load | Go to the index page | Image appears | Pass |
| Shop now Button | Opens the Book Page | Click on the button | Book page opens | Pass |

**Books Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Book cards | Displays Book image | Open the Books Page | Images appear | Pass |
| Book cards | Display Book title and price | Open the Books Page | titles and prices appear | Pass |
| Book image animation | Hovering on the image makes the book appear to open | Hover over the image | Correct book detail page opens | Pass |
| Book image | Clicking on the image opens a relevant book detail page | Click on the image | Correct book detail page opens | Pass |
| Book title | Clicking on the view more button opens a book detail page | Click on the button | Correct book detail page opens | Pass |
| Admin buttons | Appear to the superuser | Log in as superuser | Edit and delete buttons appear | Pass |
| Edit button | Opens a Book edit page | Click on the button | Edit Book page opens for the correct Book | Pass |
| Delete button | Deletes a Book | Click on the button | Book deleted | Pass |
| Toasts | Appear when a Book is edited or deleted | Edit or delete a Book | Toasts appear | Pass |
| Dropdown | Sort Books | Select different sorting options | Books sorted correctly | Pass |
| Genre page | Appears when clicked on a Genre name | Click a Genre name on a Book card | Correct Books appear | Pass |
| Genre name | Appears on a Genre page | Click a Genre name on a Book card | Correct name appears on the genre page | Pass |
| Book count | Shows the amount of Book within the genre | Click a Genre name on a Book card | Correct number of books appears | Pass |
| Book query | Shows relevant Books | Type a query into the search bar | Correct Books appear | Pass |
| Back to the top button | Takes user back to the top of the page | Click on the button | Works as expected | Pass |

**Book Details Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Book Detail page | Displays correct Book information | Go to the Book Detail page for any Book | Correct information displayed | Pass |
| Add to basket button | Adds Book to basket | Click on the button | Book added | Pass |
| Quantity selector | Select quantity | Add to basket | Correct quantity added | Pass |
| Add to basket button | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 Books | Impossible to add | Pass |
| Added to basket toast | Appears when a Book is added to the basket | Add to basket | Toast appears | Pass |
| Added to basket toast | Shows total price | Add to basket | Total price correct | Pass |
| Added to basket toast | Go to Secure Checkout button opens basket | Click on the button | Correct page opens | Pass |
| Add to wishlist icon | Adds or removes from wishlist | Click on the icon | Works as expected | Pass |
| Edit button | Opens a Book edit page | Click on the button | Edit Book page opens for the correct Book | Pass |
| Delete button | Deletes a Book | Click on the button | Book deleted | Pass |

**Add Book Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Book form | Loads all the fields | Go to the Add Book Page | Works as expected | Pass |
| Image field | Image title appears | Add image | Works as expected | Pass |
| Book form | Adds a new Book | Fill out the form and click submit | New Book added | Pass |
| Added book toast | Appears when a Book is added | add a book | Added book toast appears | Pass |

**Edit Book Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Book form | Fields prepopulated with existing information | Go to the Edit Book Page | Works as expected | Pass |
| Image field | Current image displayed | Go to the Edit Book Page | Works as expected | Pass |
| Book form | Updates the Book | Fill out the form and click submit | Book updated | Pass |
| Currently editing book toast | Appears when a Book is being edited | Edit a book | Editing book toast appears | Pass |

**Basket Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Table | Display Book image, title, price, quantity and subtotal | Add Books to basket | Works as expected | Pass |
| Quantity selector | Updates Book quantity | Change quantity and click Update | Works as expected | Pass |
| Quantity selector | Min value is 1, max value is 99 | Try to add less than 1 or more than 99 Books | Impossible to add | Pass |
| Remove link | Removes Book from basket | Click on | Works as expected | Pass |
| Prices | Subtotal, basket Total, Delivery and Grand Total show the correct amount | Add Books to basket | Works as expected | Pass |
| Secure Checkout button | Opens the checkout page | Click on the button | Works as expected | Pass |

**Checkout Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Order Summary | Displays correct details | Add Books to basket and go to checkout | Works as expected | Pass |
| Delivery info | Loads correct fields | Go to checkout | Works as expected | Pass |
| Save delivery info | Saves delivery info | Check the checkbox and go to the profile | Works as expected | Pass |
| Stripe payment | Make a payment | Input stripe testing card details | Works as expected | Pass |
| Loading spinner overlay | Appears when payment is being processed | Click Complete Order | Works as expected | Pass |
| Toast | Appears when an order is successfully processed | Click Complete Order | Works as expected | Pass |

**Checkout Success Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Checkout Success Page | Appears when an order is successfully placed | Place an order | Works as expected | Pass |
| Email | Displays the correct user email | Place an order | Works as expected | Pass |
| Order number | Displays an order number | Place an order | Works as expected | Pass |

**Profile Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Default Delivery Information form | Displays correct fields | Go to the profile page | Works as expected | Pass |
| Default Delivery Information form | Shows saved delivery info | Save delivery info and go to the profile page | Works as expected | Pass |
| Default Delivery Information form | Updates default delivery info | Click Update Information | Works as expected | Pass |
| Order History | Shows previous orders' details | Place orders and go to the profile page | Works as expected | Pass |
| Order number | Displays past order confirmation when clicked on | Click on the order number | Works as expected | Pass |

**Wishlist Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Wishlist Page | Displays Books added to Wishlist by the user | Add Books to Wishlist | Works as expected | Pass |
| Add to wishlist button | Changes Icon | Click the button | Works as expected | Pass |
| Remove from Wishlist button | Changes Icon | Click the button | Works as expected | Pass |

**Register Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Register form | Displays correct fields | Go to the Register Page | Works as expected | Pass |
| Back to Login button | Redirects to the Log in page | Click on the button | Works as expected | Pass |
| Sign in link | Redirects to the Log in page | Click on the link | Works as expected | Pass |
| Toasts | Appear when a confirmation email is sent and when the email address is confirmed | Create a new account | Works as expected | Pass |
| Confirmation email | Received when a new account is created | Create a new account | Works as expected | Pass |

**Log in Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Log in form | Displays correct fields | Go to the Log in Page | Works as expected | Pass |
| Sign up link | Redirects to the Register page | Click on the link | Works as expected | Pass |
| Home button | Redirects to the Index page | Click on the button | Works as expected | Pass |
| Forgot Password link | Redirects to the Forgot Password page | Click on the link | Works as expected | Pass |
| Sign in button | Logs the user in | Click on the button | Works as expected | Pass |
| Toast | Appears when the user logs in successfully | Log in | Works as expected | Pass |

**Log out Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Cancel button | Redirects to the Index page | Click on the button | Works as expected | Pass |
| Sign out button | Logs the user out | Click on the button | Works as expected | Pass |
| Toast | Appears when the user logs out successfully | Log out | Works as expected | Pass |

**Forgotten Password Page**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Forgot password form | Displays the email field | Go to the Forgot Password | Works as expected | Pass |
| Back to Login button | Redirects to the Log in page | Click on the button | Works as expected | Pass |
| Reset Password button | Send a Reset Password Email | Click on the button | Works as expected | Pass |

**Error Pages**

| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- |
| Custom Error Pages | Displays a correct error number | Manually trigger error | Works as expected | Pass |
| Go Home button | Redirects to the Index page | Click on the button | Works as expected | Pass |


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

### JavaScript Validator

I haven't created seperate js filed for my apps, instead including short scripts at the end of a HTML document to create small actions or functions. 

#### base.html

No errors were found when passing through the official Jshint validator
- There are 5 functions in this file.
- Function with the largest signature take 1 arguments, while the median is 0.
- Largest function has 4 statements in it, while the median is 2.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.

#### quantity_input_script.html

No errors were found when passing through the official Jshint validator
- There are 4 functions in this file.
- Function with the largest signature take 1 arguments, while the median is 1.
- Largest function has 6 statements in it, while the median is 5.5.
- The most complex function has a cyclomatic complexity value of 1 while the median is 1.

#### offers.html

No errors were found when passing through the official Jshint validator
- There are 2 functions in this file.
- Function with the largest signature take 1 arguments, while the median is 0.5.
- Largest function has 12 statements in it, while the median is 6.5.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.

#### books.html

No errors were found when passing through the official Jshint validator
- There are 2 functions in this file.
- Function with the largest signature take 1 arguments, while the median is 0.5.
- Largest function has 10 statements in it, while the median is 6.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.

#### book_detail.html

No errors were found when passing through the official Jshint validator
- There are 2 functions in this file.
- Function with the largest signature take 0 arguments, while the median is 0.
- Largest function has 5 statements in it, while the median is 3.5.
- The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.

#### basket.html

No errors were found when passing through the official Jshint validator
- There are 4 functions in this file.
- Function with the largest signature take 1 arguments, while the median is 1.
- Largest function has 6 statements in it, while the median is 1.5.
- The most complex function has a cyclomatic complexity value of 1 while the median is 1.

#### authors.html

No errors were found when passing through the official Jshint validator
- There is only one function in this file.
- It takes one argument.
- This function contains 2 statements.
- Cyclomatic complexity number for this function is 1.

## Lighthouse Testing / Accessibility Testing

### Index Page

![lighthouse-index](/documentation/media/images/testing/lighthouse/lighthouse-index.png)

### Signup Page

![lighthouse-signup](/documentation/media/images/testing/lighthouse/lighthouse-signup.png)

#### Log In

![Lighthouse-login](/documentation/media/images/testing/lighthouse/lighthouse-login.png)


#### Log Out

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-logout.png)


#### Profile

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-profile.png)


#### Basket

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-basket.png)


#### Books

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-books.png)


#### Book Detail

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-book-detail.png)


#### Offers

![Lighthouse-](/documentation/media/images/testing/lighthouse/)


#### Authors

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-authors.png)


#### Checkout

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-checkout.png)



#### Contact Page

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-contact.png)


#### FAQs Page

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-faqs.png)


#### About Us

![Lighthouse-](/documentation/media/images/testing/lighthouse/lighthouse-about.png)

## Devices used for Manual Testing
Paige's Books was tested on the following desktop and mobile browsers:

### Desktop
- Chrome Version 130.0.6723.92
- Firefox Version 132.0

### Mobile
- Safari iOS 17.2
- Chrome Version 130.0.6723.86

[<< Back to ReadMe](README.md)