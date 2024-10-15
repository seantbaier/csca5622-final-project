import pandas as pd
from pathlib import Path

BASE_PATH = Path.cwd().joinpath("../../data/")


def load_excel(file_path: str, names: list[str]) -> pd.DataFrame:
    """
    Load an Excel file into a pandas DataFrame with specified column names.

    This function reads an Excel file, skips the top rows used for formatting,
    assigns the provided column names, removes empty columns, and deletes specific
    rows that contain metadata or irrelevant information.

    Parameters:
    ----------
    file_path : str
        The relative or absolute path to the Excel file to be loaded.

    names : list[str]
        A list of column names to assign to the DataFrame. The length of this list
        should match the number of columns in the Excel file after skipping the
        specified rows.

    Returns:
    -------
    pd.DataFrame
        A pandas DataFrame containing the data from the Excel file, with the specified
        column names and unnecessary rows and columns removed.

    Raises:
    ------
    FileNotFoundError
        If the specified file_path does not exist.

    ValueError
        If the number of names provided does not match the number of columns
        in the loaded DataFrame after processing.

    Notes:
    -----
    - The function skips the first five rows (0 to 4) of the Excel file to
      exclude any formatting information.
    - The function specifically drops the column labeled "C0" and rows 52 to 55,
      which are assumed to contain metadata or other irrelevant data.
    - Ensure that the pandas library is imported as pd before calling this function.

    Example:
    --------
    >>> column_names = ['Column1', 'Column2', 'Column3']
    >>> df = load_excel('data.xlsx', column_names)
    """

    df = pd.read_excel(
        BASE_PATH.joinpath(file_path),
        # -- Exclude the top rows of formatting
        skiprows=[0, 1, 2, 3, 4],
        names=names,
    )

    # -- Remove empty NaN column values
    df.drop(["C0"], axis=1, inplace=True)

    # -- Delete metadata text
    df.drop([52, 53, 54, 55], inplace=True)

    return df
