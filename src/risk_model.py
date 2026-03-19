import pandas as pd

def calculate_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    scored = df.copy()
    scored["risk_score"] = (
        scored["is_high_amount"].astype(int)
        + scored["has_multiple_attempts"].astype(int)
        + scored["inactive_customer"].astype(int)
        + scored["new_customer"].astype(int)
        + scored["off_hours_debit"].astype(int)
    )
    scored["risk_band"] = pd.cut(scored["risk_score"], bins=[-1, 1, 3, 5], labels=["low", "medium", "high"])
    return scored
