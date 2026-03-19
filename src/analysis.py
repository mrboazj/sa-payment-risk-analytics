import pandas as pd

def merchant_risk_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["merchant_id", "merchant_category"], as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            failed_transactions=("is_failed", "sum"),
            successful_transactions=("is_successful", "sum"),
            avg_risk_score=("risk_score", "mean"),
            high_risk_transactions=("risk_band", lambda s: (s == "high").sum()),
            total_amount=("amount", "sum"),
        )
    )
    summary["failure_rate"] = (summary["failed_transactions"] / summary["transaction_count"]).round(2)
    return summary

def failure_reason_summary(df: pd.DataFrame) -> pd.DataFrame:
    failures = df[df["status"] == "failed"].copy()
    return failures.groupby("failure_reason", as_index=False).agg(failed_count=("transaction_id", "count"))

def high_risk_transactions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["risk_band"] == "high"].sort_values(by=["risk_score", "amount"], ascending=[False, False])
