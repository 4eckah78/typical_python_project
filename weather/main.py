import argparse
from typing import Tuple

import pandas as pd


def read_file(filename: str) -> pd.DataFrame:  
    with open(filename) as f:
        df = pd.read_csv(f, parse_dates=["dt"])
    return df


def get_hottest_temp(df: pd.DataFrame, year: int) -> Tuple[str, int]:
    group = df[df.dt.dt.year == year]
    group = group[group.AverageTemperature == group.AverageTemperature.max()]
    city = group.City.values[0]
    month = group.dt.dt.month.values[0]
    return city, month


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="This is the name of a file with weather data")
    parser.add_argument("year", default=8000, help="This is a port")
    args = parser.parse_args()
    filename = args.filename
    year = int(args.year)

    df = read_file(filename)
    city, month = get_hottest_temp(df, year)
    print(f"The hottest temperature in {year} was in {city} in {month} month")
