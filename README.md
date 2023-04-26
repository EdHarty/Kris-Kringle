# E-Commerce Store

## Introduction

Welcome to Kris Kringle gift store. This an e-commerce store perfect for those searching for the ideal gift for the people nearest and dearest to them. I got the idea for this store while partaking in the family tradition of Kris Kringle (aka Secret Santa). This store is focused towards consumers that are looking for the ultimate gift within their budget. The store offers quality gifts at fantastic prices.

A live website can be found [here](https://kriskringle.herokuapp.com/).

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
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

The main focus for this E-commerce store was to make it instinctive an
d easy to navigate. It lends itself to all shoppers in need of a gift for the friends or loved ones. Whether you are an organised or last minute customer this store provides products that are suitable and relevant to Christmas.

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals

* Responsive design to make the website accessible on different screen sizes.

* Ensure  that the navigation of the store is effortless and intuitive.

* The website design and colours are easy on the eye.

* The website payment system is secure and easy to use.

### User Goals:

-   As a customer, I want to be able to view a list of products so that I can select some to purchase.
-   As a customer, I want to view a specific category of products so that I can quickly find products of interest.
-   As a customer, I want to quickly identify deals so that I can take advantage of savings on products I'd like to purchase.
-   As a customer, I want to search for a product by name or description so that I can find a product I'd like to purchase.
-   As a customer, I want to view individual product details so that I can identify the price, description, product rating, product image and available sizes.
-   As a customer, I want to easily view the total of my purchases at a time so that I can avoid over-spending.
-   As a customer, I want to sort through the available products so that I can easily identify the best rated, best priced products.
-   As a customer, I want to sort a specific category of products so that I can find the best-priced or best-rated products in a specific category.
-   As a customer, I want to add items to my basket so that I can view the products I would like to purchase before making payment.
-   As a customer, I want to remove items and update quantities from my basket so that I can remove products I do not want before checking out.
-   As a customer, I want to select the size and quantity of a product when purchasing it so that I can ensure I purhcase the correct product.
-   As a customer, I want to enter my payment information at the checkout page so that I can checkout effortlessly.
-   As a customer, I want to know that my personal/payment information is secure so that I can confidently make a purchase .
-   As a customer, I want to be able to checkout as a guest.

Registered User Goals
-   As a registerd user, I want to create an account.
-   As a registerd user, I want to view my order history.
-   As a registerd user, I want to update my user profile.
-   As a registerd user, I want to log in or logout.
-   As a registerd user, I want to register for an account to view my profile.

Frequent Visitor Goals
-  I want to be able to see the latest blog posts.

### User Expectations:
The website should be easy to navigate.

-   The  menu is clear.
-   The website is responsive on all devices.
-   The products are conspicuous.
-   The total payment is clearly evident before making completing a purchase.
-   The website responds quickly to any action made.

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
Contact form | 4 | 5
Add products to the shopping bag | 5 | 5
Make payment for the selected products | 5 | 5
Ability to rate products | 5 | 4
To view blog posts | 5 | 4
Filters on the products page | 3 | 2
Subscription based items | 2 | 1

Total | 49 | 46

## Scope
I will phase this project in multiple phases. Phase 1 will be what I have identified as a minimum viable product. Please find below the plans I have for each phase.

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
- Footer at the bottom of the each page that links to the social media websites, newsletter subscription.
- Additional features are provided for the shopper once they register an account.
- 404-error page is included.

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

<a name="design"></a>

## 1.4. Design

[Go to the top](#table-of-contents)

### Colours
### Typography

<a name="features"></a>

# 2. Features

[Go to the top](#table-of-contents)

### All Pages

- The navigation bar is located at the top of all pages. This contains the product search bar, my account icon and the shopping bag icon. Another section contains the navigation for the products. The navigation bar is dynamic. The site user options change when logged in or out.

- The footer is located at the bottom of all pages. This contains social media links, a form to subscribe/unsubscribe to the newsletter and store links.
- The store logo is also placed at the top of all pages. Clicking on it will also direct the user to the home page.

### Sign Up Page
- Site users signup entering thier email address and password. There is password confirmation, the password must be identical to the one entered above.

### Login Page
- To log in site users must enter their email address and password to enter.
- The site user must activate their account via email to log in.
- If an account has not been created. The user can click a link to be redirected to the signup page.
- If the site user details are entered incorrectly, a message is displayed.

### Logout Page
- When logging out using the navigation bar, the site user is redirected to a sign-out page to confirm.

### Landing Page
- A explore the collection button directs the customer to the all products page. This gives the customer access to all of the available products.

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

### Shopping bag Page
- Products are displayed as line items, showing an image, a product name, the size if relevant, a SKU, the price of item, the quantity, the quantity selector and a subtotal.
- The minus button is disabled when the quantity selected is one.
- A sum total of the contents of the bag is also shown with the shopping bag total, delivery fee.
- If the free delivery threshold has not been met an alert message is shown, informing the user that they can get free delivery if they spend more .

### Checkout Page
- The customer can fill out the delivery details form that has Stripe integration.
- The customer can select a checkbox to save their details for next time. The card details are not saved.
- The customers order summary is shown, this ensure the order is correct before continuing and checking out.
- An alert is displayed to the customer informing them of the amount they will be charged.

### Checkout Success Page
- Displays order summary, with an order number.
- Shows that an email has been sent to confirm order.

### My Profile Page
- The site user can update their delivery details and this will then be upadated on the checkout page.
- The site user can view their order history. The order number can be selected to view any previous orders. 

### Product Management Page
- This is for site admin only.
- Displays a form to add more products to the store.

### Blog Management Page
- This is for site admin only.
- Displays a form to add more blog posts.

### Newsletter Subscribe Page
- Site users enter their email address to subscribe to the newsletter.
- Once they are successfully subscribed to the newsletter, they are redirected to the home page. A success alert message will be displayed confirming successful subscription to the newsletter
- An error message will appear if user has already subscribed.

### Newsletter Unsubscribe Page
- The site user must enter thier email address to unsubscribe from the newsletter.
- Once unsubscribed from the newsletter, the site user will be redirected to the home page. A success alert message will be displayed confirming successful unsubscription to the newsletter

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















