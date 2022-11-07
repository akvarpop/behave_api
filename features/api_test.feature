Feature: test API Hillel

  Scenario: First, check if the site is working, confirm the status code 200
    Given open site "https://www.aqa.science/users/" and send data admin login "admin" password "admin123"

  Scenario: create new user in admin panel
    Given create new user: USER_POPRAVKA "https://www.aqa.science/users/" auth= login "admin" password "admin123"
    And check user create USER_POPRAVKA

  Scenario: find all users and create a jason file with them
    Given log in and get a file json with all users "https://www.aqa.science/users/" login "admin" password "admin123"
    Then checking the user "Popravka" creation in the json file
    And assert checking the user "Popravka"

  Scenario: change user url and check this
    Given to change the user data in the file, we get his url from the file new_user_page.json
    Then change user USER_POPRAVKA_CHANGE (url take in Given) auth= login "admin" password "admin123"
    And check change url USER_POPRAVKA_CHANGE

  Scenario: delete user
    Given to change the user data in the file, we get his url from the file new_user_page.json
    Then delete user USER_POPRAVKA_CHANGE (url take in Given) auth= login "admin" password "admin123"

  Scenario: check delete user
    Given log in and get a file json with all users "https://www.aqa.science/users/" login "admin" password "admin123"
    Then checking the user "Popravka" creation in the json file
    And assert delete the user "Popravka"