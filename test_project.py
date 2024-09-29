# final project for CS50 Python
# Author: Jerome Schmutz

from project import get_kiteometer, convert_wind, convert_temp, color_scale


def test_get_kiteometer():
    assert get_kiteometer(0) == color_scale[0]
    assert get_kiteometer(1.2) == color_scale[0]
    assert get_kiteometer(2.2999) == color_scale[0]
    assert get_kiteometer(2.3) == color_scale[1]
    assert get_kiteometer(3.8) == color_scale[1]
    assert get_kiteometer(10) == color_scale[4]
    assert get_kiteometer(11.4999) == color_scale[4]
    assert get_kiteometer(18) == color_scale[7]
    assert get_kiteometer(18.399) == color_scale[7]
    assert get_kiteometer(18.4) == color_scale[7]
    assert get_kiteometer(21) == color_scale[7]
    assert get_kiteometer(421) == color_scale[7]

def test_convert_wind():
    assert convert_wind(0, "ft/s") == 0.0
    assert convert_wind(0.7, "ft/s") == 2.3
    assert convert_wind(1.6, "ft/s") == 5.25
    assert convert_wind(19.9, "ft/s") == 65.29
    assert convert_wind(1200, "ft/s") == 3937.01
    assert convert_wind(0, "knt") == 0.0
    assert convert_wind(0.7, "knt") == 1.36
    assert convert_wind(1.6, "knt") == 3.11
    assert convert_wind(19.9, "knt") == 38.68
    assert convert_wind(1200, "knt") == 2332.61
    assert convert_wind(0, "mph") == 0.0
    assert convert_wind(0.7, "mph") == 1.57
    assert convert_wind(1.6, "mph") == 3.58
    assert convert_wind(19.9, "mph") == 44.52
    assert convert_wind(1200, "mph") == 2684.33
    assert convert_wind(0, "m/s") == 0.0
    assert convert_wind(0.7, "m/s") == 0.7
    assert convert_wind(1.6, "m/s") == 1.6
    assert convert_wind(19.9, "m/s") == 19.9
    assert convert_wind(1200, "m/s") == 1200.0

def test_convert_temp():
    assert convert_temp(-0, "F") == 32.0
    assert convert_temp(-5.7, "F") == 21.7
    assert convert_temp(-14.6, "F") == 5.7
    assert convert_temp(-19.9, "F") == -3.8
    assert convert_temp(0, "F") == 32.0
    assert convert_temp(5.7, "F") == 42.3
    assert convert_temp(14.6, "F") == 58.3
    assert convert_temp(19.9, "F") == 67.8
    assert convert_temp(35, "F") == 95.0
    assert convert_temp(2000, "F") == 3632.0
    assert convert_temp(-0, "C") == 0
    assert convert_temp(-5.7, "C") == -5.7
    assert convert_temp(-14.6, "C") == -14.6
    assert convert_temp(-19.9, "C") == -19.9
    assert convert_temp(0, "C") == 0
    assert convert_temp(5.7, "C") == 5.7
    assert convert_temp(14.6, "C") == 14.6
    assert convert_temp(19.9, "C") == 19.9
    assert convert_temp(35, "C") == 35
    assert convert_temp(2000, "C") == 2000