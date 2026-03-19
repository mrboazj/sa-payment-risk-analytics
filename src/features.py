import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["is_failed"] = enriched["status"].eq("failed")
    enriched["is_successful"] = enriched["status"].eq("successful")
    enriched["is_high_amount"] = enriched["amount"] > 1500
    enriched["has_multiple_attempts"] = enriched["attempt_count"] >= 2
    enriched["inactive_customer"] = enriched["days_since_last_success"] > 20
    enriched["new_customer"] = enriched["customer_tenure_months"] < 6
    enriched["off_hours_debit"] = (enriched["debit_hour"] < 7) | (enriched["debit_hour"] > 18)
    return enriched
