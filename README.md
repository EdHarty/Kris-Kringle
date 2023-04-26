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
    -   [1.4. Surface](#surface)
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













