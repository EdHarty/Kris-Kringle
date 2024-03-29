# E-Commerce Store

## Introduction

Welcome to the Kris Kringle gift store. This e-commerce store is perfect for those searching for the ideal gift for the people nearest and dearest to them. I got the idea for this store while partaking in the family tradition of Kris Kringle (aka Secret Santa). This store is focused toward customers that are looking for the ultimate gift within their budget. The store offers quality gifts at fantastic prices.

A live website can be found [here](https://kriskringle.herokuapp.com/).

<img width="939" alt="AMIRESPPRO5" src="https://user-images.githubusercontent.com/88341568/235745695-8780f384-0f12-4b71-8bdc-62382d675c09.png">


# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
            -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Design](#design)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Deployment](#deployment)
-   [6. SEO](#seo)
-   [7. Marketing](#marketing)
-   [8. Social Media](#social-media)
-   [9. End Product](#end-product)
-   [10. Known Bugs](#known-bugs)
-   [11. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

The main focus for this E-commerce store was to make it intuitive and easy to navigate. It lends itself to all shoppers in need of a gift for friends or loved ones. Whether you are an organised or a last minute shopper, this store provides products that are suitable and relevant to Christmas.

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals

-   Responsive design to make the website accessible on different screen sizes.

-   Ensure that the navigation of the store is effortless and intuitive.

-   The website design and colours are easy on the eye.

-   The website payment system is secure and easy to use.

### User Goals:

-   As a customer, I want to be able to view a list of products so that I can select some to purchase.
-   As a customer, I want to view a specific category of products so that I can quickly find products of interest.
-   As a customer, I want to quickly identify deals so that I can take advantage of savings on products I'd like to purchase.
-   As a customer, I want to search for a product by name or description so that I can find a product I'd like to purchase.
-   As a customer, I want to view individual product details so that I can identify the price, description, product rating, product image and available sizes.
-   As a customer, I want to easily view the total cost of my purchases so that I can avoid over-spending.
-   As a customer, I want to be able to sort through the available products so that I can easily identify the best rated, best priced products.
-   As a customer, I want to be able to sort through a specific category of products so that I can find the best-priced or best-rated products in a specific category.
-   As a customer, I want to add items to my basket so that I can view the products I would like to purchase before making payment.
-   As a customer, I want to remove items and update quantities from my basket so that I can remove/update products before checking out.
-   As a customer, I want to select the size of a product before purchasing so that I can ensure that I purhcase the correct product.
-   As a customer, I want to enter and save my payment information before checking out so that I can checkout effortlessly.
-   As a customer, I want to know that my personal/payment information is secure so that I can confidently make a purchase .
-   As a customer, I want to be able to checkout as a guest shopper.

Registered User Goals
-   As a registerd user, I want to create an account.
-   As a registerd user, I want to view my order history.
-   As a registerd user, I want to update my user profile.
-   As a registerd user, I want to log in or logout.
-   As a registerd user, I want to register for an account to view my profile.

Frequent Visitor Goals
-  I want to be able to see the latest blog posts and reviews.

### User Expectations:
The website should be easy to navigate.

-   The  menu is clear.
-   The website is responsive on all devices.
-   The products are conspicuous.
-   The total payment is clearly displayed before completing a purchase.
-   The website responds quickly to user requests.

### User Stories

I used the GitHub projects board to manage my project. This ensured that I kept on track as I moved issues from to do, to in progress and finally to done.

<img width="956" alt="AG1 (2)" src="https://user-images.githubusercontent.com/88341568/234377636-70b4efd7-0170-46f3-b1cc-d670e83f35a1.png">

<img width="956" alt="AG3 (2)" src="https://user-images.githubusercontent.com/88341568/234379593-34ee84fd-13b3-4efd-a6d5-ff0411d8f924.png">

<img width="960" alt="AG5 (2)" src="https://user-images.githubusercontent.com/88341568/234379730-84d7d6ea-4fed-44e7-9de8-2f295c3f954c.png">

<img width="956" alt="AG6 (2)" src="https://user-images.githubusercontent.com/88341568/234379983-5b0afdb9-6a86-4dfc-8602-d7b4ca779c96.png">

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Ability to search for products | 5 | 5
Account signup | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Contact form | 5 | 5
Adding products to the shopping bag | 5 | 5
Making payment for the selected products | 5 | 5
Ability to rate products | 5 | 5
To view blog posts | 5 | 5
To make a review |5 | 5
Filters on the products page | 5 | 5
Subscription based items | 5 | 5

Total | 60 | 60

## Scope
This project will be conducted in two phases. Phase 1 will be the core functionality of the website. Phase 2 will be an augmented and improved version of the website.

### Phase 1
- Show a range of christmas related products.
- Ability to register for an account.
- Ability to create and edit a personal profile.
- Responsive design.
- Contact form.
- Add, edit and delete funtionality.
- Add and edit blog posts.
- Ability to subscribe and unsubscribe to a newsletter.
- Secure payment functionality.

### Phase 2
- Add more christmas related products.
- Ability for users to rate and review products.
- Filter the products by price, rating and category.

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

The website has a responsive design to ensure a pleasant user experience whilst using different devices. The design is simple and user friendly.

- The header, footer and navigation are consistent through all pages.
- The footer is at the bottom of the each page and contains links to social media websites and a newsletter subscription.
- Additional features are provided for the shopper once they register an account.
- A 404-error page is included to direct the user back to the website to continue shopping.

### Database Model

Checkout model structure:

```python
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)  # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

```



Newsletter model structure:

```python
class UserContact(models.Model):
    """ A model for user contact form """

    name_surname = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    details = models.CharField(max_length=55, null=False, blank=False)
    enquiry = models.TextField(max_length=220, null=False, blank=False)


class NewsLetter(models.Model):
    """ A model for subscription to newsletter """

    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.email

```
        
Blog model structure:

```python
class Post(models.Model):
    """
    Blog Model
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-status', '-created_on']

    def __str__(self):
        return self.title       
```

Product Review model structure:

```python
class ProductReview(models.Model):
    """ Product review model """
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_review')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='product_review')
    title = models.CharField(max_length=220)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.product} review by {self.author}'
```

Product model structure:

```python

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```
Profile model structure:

```python

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
    
```

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames

<img width="960" alt="2023-05-02 (2)" src="https://user-images.githubusercontent.com/88341568/235652914-5a84c693-94d3-4c23-b9e0-4125d761c687.png">
<img width="960" alt="2023-05-02 (1)" src="https://user-images.githubusercontent.com/88341568/235652996-37fa54e0-f4b3-457a-b39d-7278c49098d6.png">




<a name="design"></a>

## 1.4. Design

[Go to the top](#table-of-contents)

### Colours

I got the inspiration for my colour palatte from [here](https://coolors.co/)

### Typography

I sourced the font for the website from [here](https://fonts.google.com/specimen/Roboto)

<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages

- The navigation bar is located at the top of all of the pages. This contains the product search bar, the my account icon and the shopping bag icon. Another section contains the navigation for the products. The navigation bar is dynamic. The site user options change when logged in or out.

<img width="960" alt="AdminLoggedIn" src="https://user-images.githubusercontent.com/88341568/235657652-798d7bea-2f8b-4cfa-8b89-719a71e08702.png">

<img width="956" alt="LoginNav" src="https://user-images.githubusercontent.com/88341568/235666171-c77547a8-8f69-4188-8c04-e0ffae2af3bf.png">





- The footer is located at the bottom of all pages. This contains social media links, a form to subscribe/unsubscribe to the newsletter and has store links.
- The store logo is also placed at the top of all pages. Clicking on it will direct the user to the home page.

### Sign Up Page
- Site users signup entering their email address and password. There is password confirmation, the password must be identical to the one entered above.

<img width="960" alt="register" src="https://user-images.githubusercontent.com/88341568/235666356-d8027f92-c22a-4ba5-bc23-08b214a343f3.png">



### Login Page
- To log in, site users must enter their email address and password to enter.
- The site user must activate their account via email to log in.
- If an account has not been created. The user can click a link to be directed to the signup page.
- If the site user details are entered incorrectly, a message is displayed.

<img width="960" alt="Login" src="https://user-images.githubusercontent.com/88341568/235666533-d8cbb3ad-1dcb-479f-b7c2-89390450d04e.png">
<img width="956" alt="LoginIncor" src="https://user-images.githubusercontent.com/88341568/235666624-080b1d05-ce75-4574-8e29-261ba7f4790a.png">



### Logout Page
- When logging out using the navigation bar, the site user is directed to a sign-out page to confirm.

<img width="956" alt="signout" src="https://user-images.githubusercontent.com/88341568/235666737-d03c96b2-c984-47d0-8b08-6823c1c5e697.png">


### Landing Page
- A shop now button directs the customer to the all products page. This gives the customer access to all of the available products.

<img width="956" alt="LoginNav" src="https://user-images.githubusercontent.com/88341568/235666845-f7500322-d206-46c6-a329-17fc1cfe1055.png">



### Products Page
- The site user can locate specific products by category, using the navigation bar.
- A count of the search results within the category is displayed.
- The site user can filter products by price, rating, name and category.
- All products have an image, product name, price, category and rating.
- A back to top button, directs the site user to the top of the page.
- The edit and delete buttons are available to the site administrator, allowing products to be edited or deleted quickly.

### Products Details Page
- Each product will display an image, product name, description, price, size, category, rating, quantity selector, keep shopping button and an add to bag button.
- The edit and delete buttons can be seen and used by a site administrator.
- The minus button is disabled when the quantity selected is one.
- A success message will pop up to confirm the product has been added to the bag.

<img width="960" alt="Shoppingb" src="https://user-images.githubusercontent.com/88341568/235667019-aa08b2b9-c22c-45c7-87b3-920415c7b696.png">



### Shopping bag Page
- Products are displayed as line items, showing an image, a product name, the size if relevant, a SKU, the price of item, the quantity, the quantity selector and a subtotal.
- The minus button is disabled when the quantity selected is one.
- A sum total of the contents of the bag is displayed with the shopping bag total, delivery fee.
- If the free delivery threshold has not been met an alert message is shown informing the user that they can get free delivery if they spend more.

### Checkout Page
- The customer can fill out the delivery details form that has Stripe integration.
- The customer can select a checkbox to save their details for the next time that they visit the site. The card details are not saved.
- The customers order summary is shown, this ensures the order is correct before continuing and checking out.
- An alert is displayed to the customer informing them of the amount they will be charged.

### Checkout Success Page
- Displays order summary, with an order number.
- Shows that an email has been sent to confirm order.

### My Profile Page
- The site user can update their delivery details and this will then be upadated on the checkout page.
- The site user can view their order history. The order number can be selected to view all previous orders.

<img width="960" alt="Orderh" src="https://user-images.githubusercontent.com/88341568/235667122-8dd6239c-8253-4ebc-b766-4416f3152ff6.png">



### Product Management Page
- This is for site admin only.
- Displays a form to add more products to the store.

### Blog Management Page
- This is for site admin only.
- Displays a form to add more blog posts.

### My Reviews Page
- Site users can review different products.
- They can leave a review and edit or delete it.
- Once a review has been left and the user decides to edit it. They are directed to the edit review page where they update their review accordingly.

<img width="960" alt="Review" src="https://user-images.githubusercontent.com/88341568/235667212-61e9de58-2c52-4b5e-abe4-53ea8640b0f6.png">


### Newsletter Subscribe Page
- Site users enter their email address to subscribe to the newsletter.
- Once they have successfully subscribed to the newsletter, they will be redirected to the home page. A success alert message will be displayed confirming successful subscription to the newsletter.
- An error message will be displayed if the user has already subscribed.

<img width="960" alt="Newssub" src="https://user-images.githubusercontent.com/88341568/235667281-8c3e488f-c429-4326-a848-2d4ee37c0d19.png">



### Newsletter Unsubscribe Page
- The site user must enter thier email address to unsubscribe from the newsletter.
- Once unsubscribed from the newsletter, the site user will be redirected to the home page. A success alert message will be displayed confirming successful unsubscription to the newsletter

<img width="956" alt="NewsUnsub" src="https://user-images.githubusercontent.com/88341568/235667358-dfe6ea4b-ffe9-4a9f-9686-7730daef46b4.png">


<a name="technologies-used"></a>
## 3. Technologies Used
[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project uses HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project uses Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project uses JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project uses Python.
-   [Django](https://www.djangoproject.com/)
    -   The project uses Django as the main framework.
-   [Boostrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    -   The project uses Bootstrap 4.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project uses PostgreSQL as a database.
-   [AWS](https://aws.amazon.com/)
    -   The project uses Amazon Web Services to host all static and media files.
-   [Gitpod](https://www.gitpod.io/)
    -   The project uses Gitpod.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project uses Chrome to debug and test the source code using HTML5.
-   [Heroku](https://www.heroku.com/)
    -   The project is deployed and hosted by Heroku.
-   [Balsamiq](https://balsamiq.com/)
    -   Balsamiq was used to create the wireframes during the design process.


-   [Google Fonts](https://fonts.google.com/)
    -   Google fonts were used to import the **"Roboto"** font into the style.css file which is used on all pages throughout the project.
-   [GitHub](https://github.com/)
    -   GitHub was used to store the project's code after being pushed from Git.

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)
### Responsive Tools
I used [Am I Responsive](http://ami.responsivedesign.is) to check if site was reponsive on other devices.

### W3C Validator Tools

#### HTML:
I used [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) to check for any errors within the HTML pages.

![html](https://user-images.githubusercontent.com/88341568/234749973-471e80a5-a56e-4bce-bce3-48da0987be96.png)


#### CSS:
I used [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to check for any errors within CSS stylesheets.

![css](https://user-images.githubusercontent.com/88341568/234749908-972a7864-ef10-4d4b-8188-5c12866a414a.png)


### JavaScript:
I used [JS Hint](https://jshint.com/) to check for any errors within all my JavaScript script files. JS Hint showed warnings but no errors.

![jshint](https://user-images.githubusercontent.com/88341568/234749811-aae6ccfb-4915-450f-80a1-16fb5ad495e2.png)


### Python:
To check my Python files I used the command python3 -m flake8 in the terminal. The validator showed multiple "line too long" errors. 

## Manual Testing

I have tested my site on Safari and google chrome on multiple devices:

-   iPhone X
-   iPhone XS Max
-   iPad Pro
-   MacBook Pro

Please find below my testing process for mobile and web:

### Navigation Bar

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | By clicking the "home" link in the navigation bar or on the store logo, the browser redirects me to the home page. | PASS
All products page | By clicking the "All Products" link in the navigation bar, the category shows a dropdown list with sort/filter options. | PASS
Kris Kringle page | By clicking the "Kris Kringle" link in the navigation bar, the browser directs me to the Kris Kringle landing page. | PASS
Christmas Gifts page | By clicking the "Christmas Gifts" link in the navigation bar, it directs me to the Christmas Gifts product page. | PASS
Christmas Lighting page | By clicking the "Christmas Lighting" link in the navigation bar, the browser directs me to the Christmas Lighting product page. | PASS
Special Offers page | By clicking the "Special Offers" link in the navigation bar, the category shows a dropdown list to sort/filter options. | PASS
Register page | By clicking the "Register" link in the navigation bar, the browser directs me to the register page. | PASS
Login / Logout page | By clicking the "Login" or "Logout" links in the navigation bar, the browser directs me to the login or logout page. | PASS
Shopping Bag page | By clicking the "Shopping Bag" icon in the navigation bar, the browser directs me to the basket page. | PASS
My Profile page | By clicking the "My Profile" link in the navigation bar, the browser directs me to my profile page. | PASS
Product Management page | By clicking the "Product Management" link as a site admin in the navigation bar, I am directed to the product management page. | PASS
Blog Management page | By clicking the "Blog Management" link as a site admin in the navigation bar, the browser directs me to the blog management page. | PASS
My Reviews page | By clicking the "My Reviews" link as a site admin in the navigation bar, the browser directs me to the my reviews page. | PASS
Search bar | When searching for a keyword, the results will show products that contain the keyword in the product name or description. | PASS
Foreground & background colour | Checked foreground information is not effected by background elements. | PASS
Text | Checked that all fonts and colours used are consistent. | PASS


### Footer

All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Subscribe to Newsletter | By inputting my email in the newsletter form in the footer, I am directed to the home page. A success message pop up is visible. | PASS
Unsubscribe to Newsletter page | By clicking the "unsubscribe" link in the footer, I am directed to the newsletter unsubscribe page. | PASS
Contact Us page | By clicking the "contact us" link in the footer, I am directed to the contact page. | PASS
Register page | By clicking the "Register" link in the footer, I am directed to the register page.| PASS
Login page | By clicking the "login" link in the footer, I am directed to the login page. | PASS
Facebook page | By clicking the Facebook icon, a new tab opens and redirects the user to the Kris Kringle Facebook page. | PASS
Twitter | By clicking the Twitter icon, a new tab opens to the Twitter website. | PASS
Instagram | By clicking the Instagram icon, a new tab opens to the Instagram website. | PASS

### Home page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly and are responsive on all devices. | PASS
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views. | PASS

### Products page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | Media assets are displayed properly and are responsive on all devices. | PASS
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Sort filter | Check the filter functionality by selecting each option. | PASS
Edit Button/Delete Button (Site Admin) | Check the edit/delete button is only accessible to the Site Admin. | PASS


### Products details page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly and are responsive on all devices. | PASS
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Size Selector | Check the size selector functionality by adding each option to the shopping bag. | PASS
Quantity Selector | Check the plus and minus function. | PASS
Edit Button/Delete Button (Site Admin) | Check the edit/delete button is only accessible to the Site Admin. | PASS

### Shopping bag page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly and are responsive on all devices. | PASS
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Remove item/s from bag | Clicking the remove link on a product removes the product from the bag. | PASS
Quantity Selector | Check the plus and minus function. | PASS
Free delivery threshold | Adding products that are under/over the €50 threshold for free shipping. An alert message displayed if under. | PASS

### Checkout page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly and are responsive on all devices. | PASS
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Checkout form | Filling in the form with the correct/incorrect details. If incorrect, an error message displayed | PASS
Save details checkout | Check if saving my details using the checkbox saves/updates my profile details. | PASS
Card authentication | Used the valid Stripe test card details and invalid details to see alert messages. | PASS

### Checkout success page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Order history | Clicking on the order number, I am directed to all past order confirmations summaries. | PASS
Updating my profile | When updating my delivery information, this is seen on the checkout page. | PASS

### Product management page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Adding a product | When adding a new product, the product is added to the correct category and can found using the search bar. | PASS
Uploading an image | When uploading a new image, the uploaded file name is displayed. | PASS

### Blog management page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check the element on the page for scalability in mobile, tablet and desktop view.| PASS
Adding a Blog post | When adding a blog post, the blog post is added to the main blog section. | PASS
Uploading an image | When uploading an image to a blog post, the site shows the name of the file that will be uploaded. When checking the all blog posts page, the image is also shown. | PASS

### My Reviews page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check the element on the page for scalability on mobile, tablet and desktop views.| PASS
Adding a Review | When adding a review, the review is added to the main review section. | PASS
Uploading an image | When uploading an image to a review, the site shows the name of the file that will be uploaded. When checking the all reviews page, the image also shows. | PASS

<a name="deployment"></a>

# 5. Deployment
[Go to the top](#table-of-contents)

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:

1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to localhost address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, I had to:

1. Create Heroku App
2. Install dj_database_url and psycopg2-binary in my local environment
3. Freeze requirements.txt file
4. In settings.py import dj_database_url
5. Back up the local database using "./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json" in the terminal window.
6. Comment out the local default database
7. Add the Heroku database url via dj_database_url.parse()
8. Run migrations to the Postgres database
9. Restore the database using this command "./manage.py loaddata db.json" in the terminal windows.
10. Create a SuperUser for the Postgres database
11. Configure the database so that when the app is running on Heroku it uses the Postgres database and when it's running locally it uses the SQLite database
12. Create Procfile so that Heroku creates a web dyno so that it will run gunicorn and serve the Django app
13. Disable Heroku collect static
14. Add the Heroku hostname to allowed hosts in settings.py
15. Generate a new Django secret key and add this to the Heroku config variables
16. Replace the secret key in settings.py to grab it from the environment
17. Set debug to True only if the environment is a development environment
18. Commit changes and deploy to GitHub and Heroku
19. Create an AWS account
20. Create an S3 bucket
21. Configure the S3 bucket settings and policies
22. Create and configure the IAM service
23. In the terminal install Boto3 and Django-storages
24. Freeze requirements.txt file
25. Add a statement to the AWS bucket if the environment is "USE_AWS"
26. Add AWS keys to the Heroku config variables
27. Create custom storage classes for media and static files
28. In settings.py add a statement to use the static and media storage class and locations
29. Commit and push to GitHub and Heroku
30. In the S3 bucket create a new folder for media
31. Upload all used images to the media file in the S3 bucket
32. Add the Stripe keys to the Heroku config variables
33. Create a new webhook endpoint from the Stripe dashboard
34. Add all the Stripe keys to the Heroku config variables

<a name="seo"></a>

# 6. SEO
[Go to the top](#table-of-contents)

To improve the search engine optimisation (SEO) of the website:

- I added keywords in a meta tag to my base.html. The keywords were researched using [WordTracker](https://www.wordtracker.com/), there are a number of short-tail and long-tail keywords.

- The list of keywords are as follows:
    - Christmas gift.
    - Christmas gift ideas.
    - Christmas gifts for men.
    - Christmas gifts for women.
    - Good christmas gift.
    - Christmas last minute gifts.

```python

{% block meta %}
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="keywords" content="christmas gift, christmas gift ideas, christmas gifts for men, christmas gifts for women, good christmas gift, christmas last minute gifts">
    {% endblock %}

```

<a name="marketing"></a>

# 7. Marketing
[Go to the top](#table-of-contents)

I decided to use content marketing, Social media and email marketing as marketing strategies. As these are free and effective forms of marketing for an E-commerce store.

- Content marketing - Posting content that contains blog posts will be my primary source to display content.

- Social Media - The Facebook platform will help develop a customer base. This will make people aware of the store and the products available. The accumulation of followers will also help and they will hopefully share and like the posts from Kris Kringle . 

- Email marketing - The newsletter is a free source of marketing. The people that subscribe to the newsletter will probably translate into paying customers. This will increase sales and will provide steady traffic of loyal customers.

<a name="social-media"></a>

# 8. Social Media Business Page
[Go to the top](#table-of-contents)

<img width="939" alt="2023-04-26 (6)" src="https://user-images.githubusercontent.com/88341568/234634165-8997cc3d-938c-43fc-b36f-8d943383f24e.png">

<a name="end-product"></a>

# 9. End Product
[Go to the top](#table-of-contents)

<img width="956" alt="LoginNav" src="https://user-images.githubusercontent.com/88341568/235669331-4aa13fee-7a71-42f0-b8b0-dc71cc672f96.png">
<img width="956" alt="2023-05-02 (17)" src="https://user-images.githubusercontent.com/88341568/235669112-7b070583-5639-4a35-a35a-4fed90aff4d5.png">
<img width="960" alt="Shoppingb" src="https://user-images.githubusercontent.com/88341568/235669571-3233f3b9-7a9f-4ec5-93fc-825b840b914b.png">
<img width="960" alt="Review" src="https://user-images.githubusercontent.com/88341568/235669448-fc18d8c7-f385-4e75-b831-1efe67aa4c25.png">
<img width="956" alt="blog" src="https://user-images.githubusercontent.com/88341568/235669729-ba8e45f1-01ec-4f17-a4bb-160f258efd9c.png">
<img width="960" alt="Newssub" src="https://user-images.githubusercontent.com/88341568/235669802-d95e3ff8-4c6a-439d-aec4-d5f87e2f2673.png">
<img width="960" alt="Orderh" src="https://user-images.githubusercontent.com/88341568/235669957-34099fc1-1e81-442a-adf3-3fa97f807a79.png">
<img width="956" alt="404" src="https://user-images.githubusercontent.com/88341568/235939947-a068b058-4f0e-45a6-a58f-5669f6a58a0e.png">











<a name="known-bugs"></a>

# 10. Known Bugs
[Go to the top](#table-of-contents)

- The quantity selector for the products had a bug where the minus button was not disabled on mobile devices. This was rectified with Code Institute guidance.

<a name="credits"></a>
# 11. Credits
[Go to the top](#table-of-contents)

### Code

- The carousel on the landing page came from [CodePen](https://codepen.io/)

### Content

- I got the logo [Adobe Creative Cloud Express logo maker](https://www.adobe.com/)
- I got the image urls from [imgbb](https://imgbb.com/) and [amazon](https://www.amazon.co.uk/)


### Project Acknowledgements

- My Mentor
- Code Institue Tutor Support

















