"""Daily Leads and Partners by Date and Make Name example."""
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """Daily Leads and Partners by Date and Make Name

    Args:
        daily_sales (pd.DataFrame): DataFrame containing daily sales data with columns 'date_id', 'make_name', 'lead_id', and 'partner_id'.

    Returns:
        pd.DataFrame: DataFrame with columns 'date_id', 'make_name', 'unique_leads', and 'unique_partners'.
    """
    # Group the daily sales data by 'date_id' and 'make_name', without setting the index.
    daily_sales_grouped = daily_sales.groupby(
        by=['date_id','make_name'], as_index=False
    )
    # Aggregate the grouped data to calculate the number of unique leads and unique partners for each group.
    daily_sales_grouped = daily_sales_grouped.agg(
        unique_leads=("lead_id", "nunique"),
        unique_partners=("partner_id", "nunique")
    )
    return daily_sales_grouped

# Sample Data
data = {
    'date_id': [
        pd.Timestamp('2020-12-8'),
        pd.Timestamp('2020-12-8'),
        pd.Timestamp('2020-12-8'),
        pd.Timestamp('2020-12-7'),
        pd.Timestamp('2020-12-7'),
        pd.Timestamp('2020-12-8'),
        pd.Timestamp('2020-12-8'),
        pd.Timestamp('2020-12-7'),
        pd.Timestamp('2020-12-7'),
        pd.Timestamp('2020-12-7'),
    ],
    'make_name': [
        'toyota',
        'toyota',
        'toyota',
        'toyota',
        'toyota',
        'honda',
        'honda',
        'honda',
        'honda',
        'honda'],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1],
}
daily_sales = pd.DataFrame(data)

# Call the function
daily_leads_and_partners(daily_sales)
