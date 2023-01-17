from pytest import mark


@mark.entertainment
def test_entertainment(chrome_browser):
    chrome_browser.get('https://www.google.com')
    assert True
