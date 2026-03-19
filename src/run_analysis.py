from pathlib import Path
from load_data import load_transactions
from features import engineer_features
from risk_model import calculate_risk_score
from analysis import merchant_risk_summary, failure_reason_summary, high_risk_transactions

def main() -> None:
    root = Path(__file__).resolve().parents[1]
    input_file = root / "data" / "synthetic_transactions.csv"
    output_dir = root / "output"
    output_dir.mkdir(exist_ok=True)

    df = load_transactions(input_file)
    enriched = engineer_features(df)
    scored = calculate_risk_score(enriched)

    merchant_risk_summary(scored).to_csv(output_dir / "risk_summary_by_merchant.csv", index=False)
    failure_reason_summary(scored).to_csv(output_dir / "failure_reason_summary.csv", index=False)
    high_risk_transactions(scored).to_csv(output_dir / "high_risk_transactions.csv", index=False)

if __name__ == "__main__":
    main()
