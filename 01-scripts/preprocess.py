from contaminacion.data.load import load_compressed_pollution_data
from contaminacion.data.transform import convert_column_from_ppb_to_ppm


def main() -> None:
    pollution_2025_data: str = "00-data/raw/contaminantes_2025.csv.gz"

    data = load_compressed_pollution_data(pollution_2025_data)

    data = data.pipe(convert_column_from_ppb_to_ppm, columns=["O3"])
    print(data.head())
    print(data.describe())


if __name__ == "__main__":
    main()