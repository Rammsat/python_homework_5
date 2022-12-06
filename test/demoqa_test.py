from selene import have, command
from selene.support.shared import browser
import os


def test_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id=firstName]').type('World')
    browser.element('[id=lastName]').type('Peace')
    browser.element('[id=userEmail]').type('qwe@mail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('[id=userNumber]').type('9998887755')
    browser.element('[id=dateOfBirthInput]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="4"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="2004"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--014"]').click()
    browser.element('[id=subjectsInput]').type('English').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[id=uploadPicture]').send_keys(os.path.abspath('image/image.PNG'))
    browser.element('[id=currentAddress]').perform(command.js.scroll_into_view)
    browser.element('[id=currentAddress]').type('some address')
    browser.element('[id=state]').click()
    browser.element('[id=react-select-3-option-0]').click()
    browser.element('[id=city]').click()
    browser.element('[id=react-select-4-option-0]').click()
    browser.element('[id=submit]').press_enter()
    assert browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    assert browser.all("tbody tr td:last-child").should(have.texts(
         'World Peace',
         'qwe@mail.com',
         'Male',
         '9998887755',
         '14 May,2004',
         'English',
         'Sports',
         'image.PNG',
         'some address',
         'NCR Delhi'))