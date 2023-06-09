Feature: A registered user wants to shop online
  Background:
    Given the website is launched
    Then a user logs in with valid credentials
      | email           | password |
      | vmansur@abc.com | 123456   |
  Scenario: Successfully buying one t-shirt
    Given a logged user goes to products page
    When they search for "tshirt"
    And "2" products are added to cart
    Then user removes "1" product that they did not like

    When user proceeds to checkout
    Then they can review the order
    And proceed to payment

    When payment is completed
    Then order is confirmed
    And an invoice is downloaded
