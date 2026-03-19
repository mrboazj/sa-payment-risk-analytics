import pandas as pd
from src.risk_model import calculate_risk_score

def test_calculate_risk_score_assigns_high_band():
    df = pd.DataFrame([{
        "is_high_amount": True,
        "has_multiple_attempts": True,
        "inactive_customer": True,
        "new_customer": True,
        "off_hours_debit": False,
    }])
    result = calculate_risk_score(df)
    assert int(result.iloc[0]["risk_score"]) == 4
