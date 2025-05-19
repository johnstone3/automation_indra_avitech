Feature: Testing GMail Fundamental Functionalities

  Scenario: Successfully sending an email with an attachment
    Given the user navigates to the GMail login page

    When the user enters valid email of GMail account to 'Email or phone' field
    And the user clicks the next button
    And the user enters valid password for used email
    And the user clicks the next button
    Then the user is successfully logged in

    When the user clicks the Compose button in the left sidebar
    Then a New Message panel appears at the bottom

    When the user clicks on 'To' button in the New Message panel
    Then a popup window with contacts appears

    When the user selects recipients from the contacts:
      | John Stone | john.stone.pytest@gmail.com |
    And clicks Insert on the popup window with contacts
    Then the popup window with contacts disappears
    And the panel at the bottom contains the selected recipients in the 'Recipients' field

    When the user fills in the subject "Test Message with Attachment"
    And the user fills in the body "This is a test email with an attachment."
    And the user uploads the file "resources/gmail_functionality/attachment.txt" as an attachment
    And the user clicks the Send button
    Then the alert popover with text "Message sent" appears in bottom left corner

    When the user clicks on avatar icon in top right corner
    And the user clicks the Sign out button
    Then the user is successfully logged out

