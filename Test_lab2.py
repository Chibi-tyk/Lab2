import lab2

def test_find_min_max():
    expected_result = (1,6)
    test_list = [1, 6, 4, 3, 5, 2]
    result = lab2.min_max_temp(test_list)
    assert (result == expected_result)

def test_calc_average():
    test_list = [1,6,4.245,3,5,2]
    expected_result = 3.540833333
    result = lab2.calc_average(test_list)
    assert (round(result,4) == round(expected_result,4))

def test_median_temp():
    test_list = [1,2,3,4,5,6]
    expected_result = 3.5
    result = lab2.median_temperature(test_list)
    assert ( result == expected_result)