Feature: A registered user wants to shop online
  Background:
    Given the website is launched
    Then a user inputs valid credentials
  Scenario: Successfully buying one t-shirt
    Given a logged user goes to products page
    When they search for t-shirts
    Then all available t-shirts are displayed

    When two t-shirts are added to cart
    Then the products are shown on cart
    Then user can remove the ones they didn't like

    When user proceeds to checkout
    Then they can review the order
    And proceed to payment

    When card details are entered
    Then order is payed
    And an Invoice is downloaded
