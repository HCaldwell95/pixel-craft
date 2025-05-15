
# The PixelCraft E-Commerce Store

## Introduction

**Pixel Craft** is a web application designed to offer a suite of creative services, including logo design, website design, stationery design, business cards, social media graphics, custom prints, flyer design, and packaging design. The platform provides users with a seamless experience to explore and acquire these services.

[Visit the Website Here]()

[Visit the Project's GitHub Repository Here](https://github.com/HCaldwell95/pixel-craft)


# Table of Contents

- [User Experience (UX)](#user-experience)
   - [Strategy](#strategy)
      - [Purpose](#purpose)
      - [User Stories](#user-stories)
         - [For This Sprint](#for-this-sprint)
         - [For Future Sprints](for-future-sprints)
   - [Scope](#scope)
      - [Sprint 1](#sprint-one)
      - [Sprint 2](#sprint-two)
      - [Future Sprints](#future-sprints)
   - [Structure](#structure)
      - [Project Applications](#project-applications)
      - [Project Database](#project-database)
         - [Models](#models)
      - [Skeleton](#skeleton)
         - [Wireframes](#wireframes)
      - [Surface](#surface)
         - [Font](#font)
         - [Icons](#icons)
         - [Colours](#colours)
         - [Responsive Screens](#responsive-screens)
- [Features](#features)
   - [Existing Features](#existing-features)
      - [Landing Page](#landing-page)
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
      - 
   - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
   - [Languages](#languages)
   - [Tools](#tools)
   - [Styling](#styling)
   - [Validation](#validation)
   - [Databases](#databases)
- [Testing](#testing)
   - [Code Validation](#code-validation)
      - [W3C HTML Validator](#html-validator)
      - [W3C CSS Validator](#css-validator)
      - [Python Syntax Checker PEP8 Validation](#python-validation)
      - [Lighthouse](#lighthouse)
      - [Responsiveness](#responsiveness)
      - [Manual Testing](#manual-testing)
- [Bugs](#bugs)
   - [Resolved](#resolved)
   - [Unresolved](#unresolved)
- [Deployment](#deployment)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)
\
&nbsp;


# User Experience (UX)
User Experience (UX) is all about how intuitive, accessible, and user-friendly a website is. It's a crucial factor that determines how effectively a website meets users’ needs and encourages engagement.

To guide the design and development of this project, the UX approach was built around the Five Planes of UX Design:
* The Strategy Plane
* The Scope Plane
* The Structure Plane
* The Skeleton Plane
* The Surface Plane
\
&nbsp;

## Strategy
To ensure the website design aligns with the five UX planes, it’s essential to keep the intended audience at the heart of every design and development decision.

#### 🎯 Target Audience
The website is built with a specific demographic in mind:

* Age Group: 25–45 years old

* Location: Primarily urban environments and built-up city areas

* Income Level: Middle to high income, with disposable income available

* Occupation: Professionals, students, freelancers, and creative industry workers

* Lifestyle: Digitally savvy individuals who value aesthetics, craftsmanship, and intentional design

* Interests: This audience appreciates personalised branding, visual storytelling, and high-quality digital products. They are likely to follow design trends, support independent creatives, and value sustainability, authenticity, and originality in the brands they engage with.

#### 🌐 User Expectations
Based on these insights, users of Pixel Craft expect:

* Seamless Navigation – A site that is intuitive, fast, and flows logically from one section to another.

* Clear Presentation of Services – Information about digital design offerings (logos, packaging, social media content, etc.) should be accessible and well-structured.

* Easy Booking or Inquiry Process – Users should be able to upload briefs, make requests, or get in touch without friction.

* Mobile-Friendly Design – With a mobile-first mindset, users expect smooth performance across all screen sizes.

* Visual Appeal – As a creative portfolio and service-based site, users anticipate a polished, on-brand aesthetic with consistent typography, colour, and spacing.

By keeping these user expectations and behaviours in mind, Pixel Craft ensures a purposeful and rewarding user journey that aligns with modern design standards and client needs.

### Purpose

The purpose of the PixelCraft website is to showcase and promote high-quality design services, offering a professional portfolio of creative assets, while providing a seamless, responsive, and mobile-friendly user experience for clients to view, inquire, and purchase designs, all aimed at establishing trust and brand identity.

### User Stories
#### For This Sprint

#### For Future Sprints

## Scope

n order to ensure that the current sprint are completed, the focus was as follows:

#### Sprint 1

This sprint focuses on the “Must Haves” and the marking criteria:

* A homepage with basic details on the ecommerce website and the products available to buy.

* A Navbar enabling the user to easily navigate through the website.

* The ability of the user to login and create a profile.

* Applications that allow the user to put products into their shopping basket and place that order.

#### Sprint 2

* Stripe Integration: Implement Stripe API to enable users to successfully complete purchases through the website.

* Order Confirmation: Ensure users receive order confirmations both via their profile page and through in-site notifications.

* Blog Page Launch: Create a blog section to showcase relevant and engaging content for the Pixelcraft community.

* Blog Enhancements: Add interactive elements to the blog, such as allowing users to select and save their favourite roast preferences.

## Future Sprints

Elements to add to the site in the future:

* Incorporate email confirmation.
* Use profile data to build a product recommendation model that helps tailor promotions, advertising, and sales strategies.

## Structure

Establishing a clear and well-structured project layout ensures that development progresses logically and that sprint steps are easier to follow. To support this, the project content was divided into distinct applications to manage specific tasks and responsibilities. Additionally, database tables were designed to organise and structure user data effectively for storage and future use.

## Project Applications

For this project, four core applications were developed to structure the website’s functionality:

* Home: A static application that introduces users to the eCommerce store and guides them to other sections of the site. It contains no dynamic models.

* Products: Displays all available items in the store and allows the site owner to add, edit, or remove products as needed.

* Accounts: Enables users to input and manage their personal details, streamlining the checkout process through pre-filled forms and enhancing the overall user experience.

* Orders: Manages the shopping cart functionality, allowing users to add products, review their selections, and proceed to checkout for final purchase.

## Project Database
### Accounts Model

#### CustomUser
The CustomUser model extends Django’s built-in AbstractUser to provide flexibility for future customizations. At present, it inherits all default fields such as username, email, password, first_name, and last_name, with the potential to expand the user model as the project evolves.

#### UserProfile Model
The UserProfile model is designed to store additional details about each user beyond what is captured in the default authentication model. It enriches the user's account with personal preferences and contact details, which can be used to tailor services, support, and marketing efforts.

It can be broken down as follows:

* user – A one-to-one relationship linking the profile to a specific user account.

* favorite_category – A field allowing users to choose their preferred design category (e.g., logo designs, packaging design), useful for personalized content and product recommendations.

* phone – The user's contact number.

* picture – An optional profile picture uploaded by the user.

* updated_at – Timestamp for the last update made to the profile.

* created_at – Timestamp indicating when the profile was created.


#### Design Categories
The DESIGN_CATEGORIES list defines the available design types that users can select as their favorite category. These are used in the favorite_category field of the UserProfile model to personalise the user's experience. The available categories include:

* Logo Designs
* Website Design
* Stationary Design
* Business Cards
* Social Media Graphics
* Flyer Design
* Packaging Design
* Custom Prints

### Order Model



### Products Model

#### Product Model
The Product model represents the core item available for purchase in the store. It captures essential and extended information about each product and serves as the parent for associated options and images.

It can be broken down as follows:

* id – Auto-incremented primary key to uniquely identify the product internally.

* guid – A globally unique identifier (UUID) for the product, useful for referencing across systems.

* about – A detailed text description providing in-depth information about the product.

* tags – A JSON field storing a list of tags to support filtering and categorization (e.g., "minimal", "bold", "modern").

* name – Optional name of the product, displayed on listings and detail pages.

* description – Additional optional product description for extended detail.

* price – The base price of the product. If no specific options are added, this price is used.

* image_url – Optional URL pointing to a product image.

#### Custom Method:

* get_minimum_price() – Retrieves the lowest price available from associated product options. If no options exist, it defaults to the base product price.

#### ProductImage Model

The ProductImage model allows multiple images to be associated with a single product, improving visual presentation and giving users more context when browsing.

* product – A foreign key linking the image to its associated product.

* image – An image file uploaded to the product_images/ directory.

#### ProductOption Model
The ProductOption model allows variations of a product to be created, each with its own price, image, and description. This is useful for products with different sizes, formats, or bundled features.

* product – A foreign key linking the option to its parent product.

* name – The name of the option (e.g., "Premium Package", "Digital Only", "With Print").

* price – Optional custom price for the specific option.

* description – An optional text field to provide details about what the option includes.

* image – An optional image URL specifically for the option, useful if it differs visually from the base product.

#### Custom Method:

* __str__() – Returns the name of the product option for admin and display purposes.

* has_options() – Checks whether this product option has nested options (although this method assumes a potential future structure and may be redundant in the current model layout).

### Skeleton
The initial skeleton offers a broad foundation that can be progressively refined and developed. It serves as a strategic starting point for planning features that align with user stories and sprint goals. Based on this structure, wireframes can be created to guide the design process and visually represent the layout and flow of the website.

#### Wireframes
Balsamiq was used to design the initial concept for the website’s layout and user flow. Following a mobile-first approach, the wireframes were first created for mobile devices, then adapted for medium and large screen sizes. This ensured the design remained responsive and functional across different screen types.

Basic wireframes are provided below, though it’s worth noting that some elements may differ slightly from the final implemented design.

### Surface
The surface plane focuses on the visual aesthetics and user interface of the website. Choosing the right colours, typography, and icons is essential to creating an engaging and visually appealing experience for users.

### Font

To establish a distinct and creative visual identity for the graphic design website, a combination of unique and elegant typefaces was selected from Google Fonts. These fonts were chosen to reflect the brand’s modern, artistic tone while maintaining readability and aesthetic balance.

* Audiowide Regular – Used for headings and logo elements, this geometric, tech-inspired font adds a bold, contemporary flair that captures attention and reinforces the creative edge of the brand.

* Cormorant VariableFont & Cormorant Italic VariableFont – These sophisticated serif fonts bring a touch of elegance and refinement to the design. They are primarily used for body text and callouts, offering a high-contrast and classical feel that balances well with the modernity of other elements.

* Italiana Regular – Applied to subtle accents and subheadings, this sleek and graceful font adds a high-fashion, editorial tone, supporting the brand's professional and design-focused image.

Together, this font combination creates a striking yet cohesive visual identity, aligning with the brand values of creativity, quality, and style.

#### Icons

### Colours
   #### Responsive Screens

## Features

   ### Existing Features
      #### Landing Page
   ### Navigation Bar
   ### Menu Selections
      #### Footer
      #### Blog Page
      #### Products Page
      #### Create and Edit Product Page
      #### Shopping Bag Page
      #### Checkout Page
      #### Profile Page
      #### Django Template Pages
      #### Messages
      #### Error Pages

- **User Authentication**: Secure user registration and login functionality.
- **Service Catalog**: Browse a variety of design services with detailed descriptions and pricing.
- **Product Showcase**: View detailed information and images of available products.
- **Order Management**: Place orders for desired services and track order status.
- **Responsive Design**: Optimised for various devices, ensuring a seamless user experience across desktops, tablets, and smartphones.


## Technologies Used

### Frontend:
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### Backend:
- Python3
- Django
- PostgreSQL

### Other Tools:
- Git & GitHub for version control
- Docker for containerisation
- Gitpod for cloud-based development environments
- Stripe for payment processing

## Usage

- **Browse Services**: Navigate to the "Services" section to explore the design services offered.
- **View Products**: Visit the "Products" section to see detailed information about available products.
- **Place an Order**: After selecting a service or product, follow the prompts to place an order.
- **User Dashboard**: Registered users can access their dashboard to view and manage their orders.

## Testing

   ### Code Validation
      #### W3C HTML Validator
         ##### First Attempt of HomePage
         ##### Final Attempt of HomePage

      #### W3C CSS Validator
         ##### First Attempt of CSS Files

      #### Python Syntax Checker PEP8 Validation
         ##### First Attempt
         ##### Final Attempt

      #### Lighthouse
      #### Responsiveness
      #### Web Aim Contrast Checker
      #### Browser Compatability
      #### Manual Testing

   ### Bugs
      #### Resolved
      #### Unresolved

Comprehensive testing has been conducted to ensure the platform's functionality and responsiveness:

Unit Tests: Django's testing framework was used to test models, views, and forms.

Integration Tests: Simulated user interactions to ensure different components work together seamlessly.

Manual Testing: Performed across various devices and browsers to verify responsiveness and compatibility.

Payment Processing: Tested Stripe integration using test card numbers to ensure secure transactions.

## Deployment

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/HCaldwell95/pixel-craft.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd pixel-craft
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

4. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.



## Contributing

We welcome contributions to enhance Pixel Craft. To contribute:

1. **Fork the repository**.

2. **Create a new branch**:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make your changes**.

4. **Commit your changes**:

   ```bash
   git commit -m 'Add some feature'
   ```

5. **Push to the branch**:

   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a pull request**.

Please ensure your code follows the project's coding standards and includes relevant tests.

## Credits

## Licence

## Contact

For questions or suggestions, please contact the project maintainer:

- **Name**: H. Caldwell
- **Email**: [hade_caldwell@msn.com](mailto:hade_caldwell@msn.com)
- **GitHub**: [HCaldwell95](https://github.com/HCaldwell95)


























Logo Icon - <a href="https://www.flaticon.com/free-icons/logo" title="logo icons">Logo icons created by Freepik - Flaticon</a>

Web Design - <a href="https://www.flaticon.com/free-icons/graphic-design" title="graphic design icons">Graphic design icons created by Freepik - Flaticon</a>

Sationary Design - <a href="https://www.flaticon.com/free-icons/agenda" title="agenda icons">Agenda icons created by Freepik - Flaticon</a>

Busines Cards - <a href="https://www.flaticon.com/free-icons/business-card" title="business card icons">Business card icons created by Freepik - Flaticon</a>

Social Media - <a href="https://www.flaticon.com/free-icons/marketing" title="marketing icons">Marketing icons created by Freepik - Flaticon</a>

Brochure Design - <a href="https://www.flaticon.com/free-icons/brochure" title="brochure icons">Brochure icons created by juicy_fish - Flaticon</a>

Flyer Design - <a href="https://www.flaticon.com/free-icons/flyers" title="flyers icons">Flyers icons created by andinur - Flaticon</a>

Packaging Design - <a href="https://www.flaticon.com/free-icons/product-design" title="product design icons">Product design icons created by Uniconlabs - Flaticon</a>