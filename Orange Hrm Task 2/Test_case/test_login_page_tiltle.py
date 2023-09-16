from Test_utilities.login_page_utilities import LoginPageActions


class TestLoginTitle:

    def __init__(self):
        pass

    def test_login_page_title(self):

        _expected_title = "OrangeHRM"

        LoginPageActions().login_to_orangehrm()

TestLoginTitle().test_login_page_title()
