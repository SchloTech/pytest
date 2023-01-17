from pytest import mark

@mark.parametrize('tv_brand', [('Samsung'), ('Sony'), ('LG')])
def test_tv_turns_on(tv_brand):
	print(f"{tv_brand} turns on as expected")

@mark.skip(reason="Do not have webdrivers set up on my desktop")
def test_browser_can_navigate_to_training_ground():
	browser.get("http://techstepacademy.com/training-ground")

def test_tv_turns_on(test_data):
	print(f"{test_data } turns on as expected")