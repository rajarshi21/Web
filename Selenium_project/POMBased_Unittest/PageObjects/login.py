# Identify locators for all the elements.
class LoginPage:
    # Elements.
    user_ele = "Email"
    pass_ele = "Password"
    login_ele = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    logout_link_text = "Logout"

    # Action.
    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.user_ele).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.pass_ele).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_ele).click()

    def click_logout(self):
        self.driver.find_element_by_linktext(self.logout_link_text).click()

