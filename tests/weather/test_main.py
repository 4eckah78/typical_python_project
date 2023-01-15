from weather.main import get_hottest_temp, read_file


def test_main():
    df = read_file("GlobalLandTemperaturesByMajorCity.csv")
    assert df is not None
    assert get_hottest_temp(df, 1985) == ("Riyadh", 8)
