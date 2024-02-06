Feature: API
    As a developer
    I want to interact with the API
    So that I can manage products, categories, and users

    Scenario: Get all products
        When I send a GET request to "/products"
        Then I should receive a 200 status code of all products

    Scenario: Create a new product
        When I send a POST request to "/products" with the following product:
            | name     | category | stock |
            | Product1 | clothes  | 10    |
        Then I should receive a 201 status code

    Scenario: Get a product
        When I send a GET request to "/products/c1e4db67-f958-4779-9fd1-1e7680a6d3dd" to specify the product
        Then I should receive a 200 status code of the product
    
    Scenario: Update a product
        When I send a PUT request to "/products/c1e4db67-f958-4779-9fd1-1e7680a6d3dd" with the following product:
            | name     | category | stock |
            | Product1 | Category1| 20    |
        Then I should receive a 200 status code of the product updated
    
    Scenario: Delete a product
        When I send a DELETE request to "/products/c1e4db67-f958-4779-9fd1-1e7680a6d3dd"
        Then I should receive a 200 status code of the product deleted
