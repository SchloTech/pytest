from pytest import mark

@mark.smoke
@mark.engine
def test_engine(chrome_browser):
    chrome_browser.get('https://www.google.com')
    assert True
