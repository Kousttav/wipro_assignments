Feature: Login Functionality Using POM

  Scenario: Successful Login

    Given User launches SauceDemo website

    When User logs in with username "standard_user" and password "secret_sauce"

    Then User should be redirected to inventory page