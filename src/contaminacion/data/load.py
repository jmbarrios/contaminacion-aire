import pandas as pd

COLS: list[str] = ["date", "id_station", "id_parameter", "valor"]

DTYPES_COLS: list[str] = ["category", "category", "float"]


def load_compressed_pollution_data(
    file_path: str, skiprows: int = 9, to_wide: bool = True
) -> pd.DataFrame:
    """ Carga el archivo de datos de conatminantes atmosfericos

    Se carga a un DataFrame de pandas los datos del archivo descargado de
    contaminantes en formato comprimido (zip)

    Args:
        file_path (str): ruta al archivo de datos comprimido
        skiprows(int): número de lineas a escapar del inicio del archivo
        to_wide (bool): regresa las concentranciones en formato ancho

    Returns:
        (pd.DataFrame) Regresa el archivo de contaminantes atmosféricos en
        un DataFrame de pandas.
    """
    df = pd.read_csv(
        file_path,
        skiprows=skiprows,
        encoding="utf-8",
        compression="zip",
        # usecols=COLS,
        dtype=dict(zip(COLS[1:], DTYPES_COLS, strict=True)),
        parse_dates=True,
    )

    df = df.dropna(subset=["valor"])
    if not to_wide:
        return df

    return df.pivot(
        index=["date", "id_station"], columns="id_parameter", values="valor"
    ).reset_index()
