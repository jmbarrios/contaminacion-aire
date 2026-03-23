import pandas as pd


def from_ppb_to_ppm(data: pd.Series[float]) -> pd.Series[float]:
    """Convierte una concentracion de ppb a ppm.

    Args:
        data (pd.Series[float]): valores de concentracion en ppb

    Returns:
        (pd.Series[float]) regresa los valores de concentracion en ppm
    """
    return data / 1_000.0


def convert_column_from_ppb_to_ppm(
    data: pd.DataFrame, columns: list[str]
) -> pd.DataFrame:
    """Convierte las columnas de datos en concentraciones en ppb a ppm

    Args:
        data (pd.DataFrame): datos de contaminacion atmosferica en formato
                             ancho
        columns (list[str]): lista de columnas a convertir sus concentraciones

    Returns:
        (pd.DataFrame) Regresa los datos con las columnas seleccionadas
        transformadas.
    """

    converted_data = data.copy()

    converted_data[columns] = converted_data[columns].apply(from_ppb_to_ppm, axis=0)

    return converted_data
