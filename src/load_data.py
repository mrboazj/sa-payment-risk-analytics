from pathlib import Path
import pandas as pd

def load_transactions(file_path: str | Path) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    df = pd.read_csv(path)
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    return df
