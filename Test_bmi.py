import Lab2.bmi as bmi

print("Test_Lab2")

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.7, 60)  # BMI ≈ 20.76
    assert result == "Normal weight"

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.7, 80)  # BMI ≈ 27.68
    assert result == "Overweight"

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.7, 45)  # BMI ≈ 15.57
    assert result == "Underweight"