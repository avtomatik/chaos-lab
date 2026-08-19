import pandas as pd


def build_cobweb_points(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert a time series into cobweb plot coordinates.
    The input series is normalized against its initial value.
    The resulting dataframe contains consecutive pairs:
        Y_t -> Y_(t+1)
    Parameters
    ----------
    df:
        Original dataset containing the observed series.
    Returns
    -------
    pd.DataFrame
        Two-column dataframe containing cobweb coordinates.
    """
    normalized = df / df.iloc[0]
    series = normalized.iloc[:, 0]
    cobweb_series = series.repeat(2).iloc[1:].reset_index(drop=True)
    return pd.DataFrame(
        {
            "Y_t": cobweb_series[:-1].to_numpy(),
            "Y_t_plus_1": cobweb_series[1:].to_numpy(),
        }
    )
