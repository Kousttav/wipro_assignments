Feature: Login Validation

  Scenario Outline: Login with multiple credentials

    Given User launches SauceDemo website
    When User enters username "<username>"
    And User enters password "<password>"
    And User clicks login button
    Then Verify login result "<result>"

    Examples:
      | username        | password     | result  |
      | standard_user   | secret_sauce | success |
      | locked_out_user | secret_sauce | error   |
      | test            | test123      | error   |