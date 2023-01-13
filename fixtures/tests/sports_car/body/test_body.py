from pytest import mark

@mark.smoke
@mark.body
class BodyTest:
    @mark.door
    def test_body(selfzzz):
        assert True
    
    def test_bumper(self):
        assert True
    
    def test_windshield(self):
        assert True()