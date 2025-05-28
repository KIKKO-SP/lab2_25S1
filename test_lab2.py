import lab2 as LAB2

def test_find_min_max():
    datalist = [1,5,3,6,8,2,4]
    expected_result = (1, 8)
    test_result = LAB2.find_min_max(datalist)
    assert (test_result == expected_result)


def test_calc_average():
    datalist = [1,5,3,6,8,2,4]
    expected_result = 4.143
    test_result = LAB2.calc_average(datalist)
    test_result = round(test_result, 3)
    assert (test_result == expected_result)


def test_calc_median_temperature():
    datalist = [1,5,3,6,8,2,4]
    expected_result = 4.0
    test_result = LAB2.calc_median_temperature(datalist)
    assert (test_result == expected_result)