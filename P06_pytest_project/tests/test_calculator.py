from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

        # arrange
    def test_subtract(self):
        a = 20
        b = 5
        cal = Calculator()

        #act
        result = cal.subtract(a,b)

        #assert
        expected = 15
        assert result == expected

        
        # arrange
    def test_multiply(self):
        a = 2
        b = 3
        cal = Calculator()

        #act
        result = cal.multiply(a,b)

        #assert
        expected =  6
        assert result == expected

        # arrange
    def test_divide(self):
        a = 10
        b = 5
        cal = Calculator()

        #act
        result = cal.divide(a,b)

        #assert
        expected =  2
        assert result == expected



