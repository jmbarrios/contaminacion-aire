from pathlib import Path

import numpy as np
import pandas as pd

from contaminacion.utils import aggregations


def main():
    interim_data_path: Path = Path("00-data/interim")
    interim_data_path.mkdir(exist_ok=True, parents=True)

    test_station = "AJM"
    test_data_file: Path = (
        interim_data_path
        /f'data_2025_station_{test_station}.parquet'
    )
    data = pd.read_parquet(test_data_file)
    data = data.set_index('date')

    daily_data = (
        data
        .resample('D')
        .agg(
            O3 = ("O3", lambda s: aggregations.agg_compliance(s, np.max)),
            NO2 = ("NO2", lambda s: aggregations.agg_compliance(s, np.max)),
            SO2 = ("SO2", lambda s: aggregations.agg_compliance(s, np.max)),
            PM10 = ("PM10", lambda s: aggregations.agg_compliance(s, np.mean)),
            PM25 = ("PM2.5", lambda s: aggregations.agg_compliance(s, np.mean)),
            CO = ("CO", aggregations.daily_co_indicator)
        )
    )
    print(daily_data.head(15))

if __name__ == '__main__':
    main()