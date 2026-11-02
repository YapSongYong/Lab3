import Lab2.bmi as BMI

def test_calc_bmi_normal():
    expected = 0
    result = BMI.calculate_bmi(weight=65, height=1.85)
    assert(result == expected)

def test_calc_bmi_under():
    expected = -1
    result = BMI.calculate_bmi(weight=35, height=1.85)
    assert(result == expected)

def test_calc_bmi_over():
    expected = 1
    result = BMI.calculate_bmi(weight=95, height=1.85)
    assert(result == expected)