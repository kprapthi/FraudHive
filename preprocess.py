import pandas as pd


def preprocess_data(data, scaler):
    """
    Convert API input into model-ready format
    """

    # Convert JSON to dataframe
    df = pd.DataFrame([data])

    # Scale only Time and Amount
    df[["Time", "Amount"]] = scaler.transform(
        df[["Time", "Amount"]]
    )

    return df