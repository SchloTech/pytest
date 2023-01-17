from pytest import mark

@mark.smoke
@mark.body
class BodyTest:
    @mark.door
    def test_body(self, chrome_browser):
        chrome_browser.get('https://www.google.com')
        assert True
    
    def test_bumper(self):
        assert True
    
    def test_windshield(self):
        assert True()