class GMailLocators:
    # Login page
    IDENTIFIER_ID_FIELD = "#identifierId"
    NEXT_BUTTON = "//button[string()='Next']"
    PASSWORD_FIELD = "//input[@type='password']"

    # Inbox page
    INBOX_LINK = "//div[@role='navigation']//a[string()='Inbox']"
    AVATAR_ICON = "//a[contains(@aria-label,'Google Account')]"
    SIGN_OUT_BUTTON_FRAME = "account"
    SIGN_OUT_BUTTON = "//a[string()='Sign out']"
    ALERT_POPOVER = "//div[@role='alert']//span[text()='{text}']"

    # Inbox page / Left sidebar
    COMPOSE_BUTTON = "//div[@role='navigation']//div[text()='Compose']"

    # Inbox page / New Message panel
    NEW_MESSAGE_PANEL = "//div[@role='dialog']//span[text()='New Message']"
    RECIPIENTS_FIELD = "//div[@role='dialog']//div[text()='Recipients']"
    TO_RECIPIENTS_BUTTON = "//div[@role='dialog']//span[text()='To']"
    RECIPIENTS_FIELD_ITEMS = "//div[@role='dialog']//div[@role='listbox' and @aria-label='Search Field']//div[@role='option']"
    SUBJECT_FIELD = "//div[@role='dialog']//input[@placeholder='Subject']"
    BODY_FIELD = "//div[@role='dialog']//div[@aria-label='Message Body']"
    ADD_ATTACHMENT_BUTTON = "//div[@role='dialog']//div[@role='button' and @aria-label='Attach files']"
    ATTACHMENT_LOADED = "//div[contains(@aria-label,'Attachment: {fname}. Press enter to view the attachment and delete to remove it')]"
    SEND_EMAIL_BUTTON = "//div[@role='dialog']//div[@role='button' and text()='Send']"

    # Inbox page / Contact modal window
    CONTACTS_IFRAME = "//div[@role='dialog']//iframe"
    CONTACT_ITEM = "//div[contains(@aria-label,'{name}') and contains(@aria-label, '{email}')]//div[text()='{name}']"
    INSERT_RECIPIENTS_BUTTON = "//button[string()='Insert']"

    # After-logout page
    CHOOSE_ACCOUNT_TEXT = "//span[text()='Choose an account']"
