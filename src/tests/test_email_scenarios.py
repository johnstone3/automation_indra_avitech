import os.path
from dataclasses import dataclass
from typing import List

import pytest
from playwright.sync_api import Page
from pytest_bdd import scenario, given, when, then, parsers

from src.services.gmail import GMailLocators
from src.utils.environment import GmailLogin, decrypt_secret


@dataclass
class ScenarioDataStore:
    login: GmailLogin | None = None
    recipients: List | None = None


@pytest.fixture(scope="module")
def scenario_data_store() -> ScenarioDataStore:
    return ScenarioDataStore()


@scenario('../../features/gmail_functionality/email_scenarios.feature', "Successfully sending an email with an attachment")
def test_email_scenarios():
    pass


@given(parsers.parse('the user navigates to the Gmail {webpage}'))
def navigate_to_login_page(webpage: str, page: Page, env_config):
    url = env_config.gmail.urls[webpage]
    page.goto(url)


@when(parsers.parse("the user enters {credentials_type} of Gmail account to 'Email or phone' field"))
def enter_valid_credentials(credentials_type: str, page: Page, env_config, scenario_data_store):
    login = env_config.gmail.login[credentials_type]
    scenario_data_store.login = login
    page.fill(GMailLocators.IDENTIFIER_ID_FIELD, login.email)


@when("the user clicks the next button")
def click_next_button(page: Page):
    page.click(GMailLocators.NEXT_BUTTON)


@when('the user enters valid password for used email')
def enter_password(page: Page, env_config, scenario_data_store):
    page.fill(
        GMailLocators.PASSWORD_FIELD,
        decrypt_secret(scenario_data_store.login.password),
    )


@then('the user is successfully logged in')
def verify_user_is_logged_in(page: Page):
    page.wait_for_selector(GMailLocators.INBOX_LINK)


@when('the user clicks on avatar icon in top right corner')
def click_avatar_icon(page: Page):
    page.click(GMailLocators.AVATAR_ICON)


@when('the user clicks the Sign out button')
def click_sign_out_button(page: Page):
    frame = page.frame(GMailLocators.SIGN_OUT_BUTTON_FRAME)
    frame.click(GMailLocators.SIGN_OUT_BUTTON)


@then('the user is successfully logged out')
def verify_user_is_logged_out(page: Page):
    page.is_visible(GMailLocators.CHOOSE_ACCOUNT_TEXT)


@when('the user clicks the Compose button in the left sidebar')
def click_compose_button(page: Page):
    page.click(GMailLocators.COMPOSE_BUTTON)


@then("a New Message panel appears at the bottom")
def verify_new_editor_panel_appears(page: Page):
    page.is_visible(GMailLocators.NEW_MESSAGE_PANEL)


@when("the user clicks on 'Recipients' field in the New Message panel")
def click_recipients_field(page: Page):
    page.click(GMailLocators.RECIPIENTS_FIELD)


@when("the 'To' button appears next to 'Recipients' field")
def verify_to_button_appears(page: Page):
    page.is_visible(GMailLocators.TO_RECIPIENTS_BUTTON)


@when("the user clicks on 'To' button in the New Message panel")
def click_to_button(page: Page):
    page.click(GMailLocators.TO_RECIPIENTS_BUTTON)


@then("a popup window with contacts appears")
def verify_contacts_popup_appears(page: Page):
    page.is_visible(GMailLocators.CONTACTS_IFRAME)


@when("the user selects recipients from the contacts:")
def select_recipients_from_contacts(page: Page, datatable: List, scenario_data_store: ScenarioDataStore):
    for item in datatable:
        (
            page
            .frame_locator(GMailLocators.CONTACTS_IFRAME)
            .locator(GMailLocators.CONTACT_ITEM.format(name=item[0], email=item[1]))
            .click()
        )

    scenario_data_store.recipients = datatable


@when("clicks Insert on the popup window with contacts")
def click_insert_on_contacts_popup(page: Page):
    page.frame_locator(GMailLocators.CONTACTS_IFRAME).locator(GMailLocators.INSERT_RECIPIENTS_BUTTON).click()


@then("the popup window with contacts disappears")
def verify_contacts_popup_disappears(page: Page):
    page.wait_for_selector(GMailLocators.CONTACTS_IFRAME, state="hidden")


@then("the panel at the bottom contains the selected recipients in the 'Recipients' field")
def verify_recipients_in_panel(page: Page, scenario_data_store):
    recipients = [r.text_content() for r in page.locator(GMailLocators.RECIPIENTS_FIELD_ITEMS).all()]
    assert len(recipients) == len(scenario_data_store.recipients)

    for used_recipient in scenario_data_store.recipients:
        assert used_recipient[0] in recipients


@when(parsers.parse('the user fills in the subject "{subject}"'))
def fill_subject(page: Page, subject: str):
    page.fill(GMailLocators.SUBJECT_FIELD, subject)


@when(parsers.parse('the user fills in the body "{body}"'))
def fill_body(page: Page, body: str):
    page.fill(GMailLocators.BODY_FIELD, body)


@when(parsers.parse('the user uploads the file "{file_path}" as an attachment'))
def upload_attachment(page: Page, file_path):
    with page.expect_file_chooser() as fc_info:
        page.click(GMailLocators.ADD_ATTACHMENT_BUTTON)

    fc_info.value.set_files(file_path)
    page.wait_for_selector(GMailLocators.ATTACHMENT_LOADED.format(fname=os.path.basename(file_path)))


@when("the user clicks the Send button")
def click_send_button(page: Page):
    page.click(GMailLocators.SEND_EMAIL_BUTTON)


@then(parsers.parse("the alert popover with text \"{text}\" appears in bottom left corner"))
def verify_email_sent_alert_appears(page: Page, text):
    page.wait_for_selector(GMailLocators.ALERT_POPOVER.format(text=text))
