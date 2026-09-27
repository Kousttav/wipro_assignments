Feature: Login Functionality

  Scenario: Successful Login

    Given User launches SauceDemo website

    When User enters username "standard_user"

    And User enters password "secret_sauce"

    And User clicks login button

    Then User should be redirected to inventory page