Feature: A registered user wants to shop online
  Background:
    Given the website is launched
    Then a user logs in with "vmansur@abc.com" and "123456"
  Scenario: Successfully buying one t-shirt
    Given a logged user goes to products page
    When they search for "tshirt"
    When two products are added to cart
    Then user can remove the ones they didn't like

    When user proceeds to checkout
    Then they can review the order
    And proceed to payment

    When payment is completed
    Then order is confirmed
    And an invoice is downloaded
