class MainPage:
    def __init__(self, page):
        self.page = page

    #web Elements
    header: str = 'h1'
    more_info_link:str = 'More information'

    #load condition
    def check_header(self):
        assert self.page.inner_text('h1') == 'Example Domain'

    def select_more_information_link(self):
        self.page.click("text=More information")