Feature:
  Scenario Outline: User is able to add/ update delivery address
    Given I have registered my account in shopizer
#    And I have logged in
    When I click on Delivery Address dropdown
    And I enter <first name>, <last name>,<street address>, <country>, <state>, <city>, <zip>, and <phone number>
    And I click on continue button
    Then my delivery address should successfully add

    Examples:
    | First Name | Last Name | Company Name | Street Address | Country        |  State | City   |  Zip  |    Phone   | Update |
    | empty      | Hassan    | Educative    | street no 2    | American Samoa | Punjab | Lahore | 54000 | 0333231116 | NO     |
    | Malik      | empty     | Educative    | street no 2    | American Samoa | Punjab | Lahore | 54000 | 0333231116 | NO     |
    | Malik      | Hassan    | Educative    | street no 2    | American Samoa | Punjab | Lahore | 54000 | 0333231116 | YES    |