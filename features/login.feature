Feature: Login

  Scenario: As a user with valid creds I can log in
     Given I go to my login form
      When I enter correct login information
      Then I should be logged in
