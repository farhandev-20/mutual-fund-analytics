from pathlib import Path
import logging
import pandas as pd


# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# LOGGING
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------------
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning applied to every CSV."""
    
    # Remove completely empty rows/columns
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Strip leading/trailing spaces from text columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    return df


# ---------------------------------------------------------
# PROCESS ONE CSV
# ---------------------------------------------------------
def process_file(file_path: Path) -> None:
    """Read, clean and save one CSV file."""
    
    try:
        logger.info("Processing: %s", file_path.name)

        df = pd.read_csv(file_path)

        original_rows = len(df)

        df = clean_dataframe(df)

        removed_rows = original_rows - len(df)

        output_path = PROCESSED_DIR / file_path.name

        df.to_csv(output_path, index=False)

        logger.info(
            "Saved: %s | Rows: %d | Columns: %d | Duplicates/empty rows removed: %d",
            output_path.name,
            df.shape[0],
            df.shape[1],
            removed_rows,
        )

    except Exception as exc:
        logger.error("Failed to process %s: %s", file_path.name, exc)


# ---------------------------------------------------------
# MAIN ETL
# ---------------------------------------------------------
def main() -> None:
    """Run the complete ETL pipeline automatically."""
    
    if not RAW_DIR.exists():
        raise FileNotFoundError(
            f"Raw data folder not found: {RAW_DIR}"
        )

    csv_files = sorted(RAW_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in: {RAW_DIR}"
        )

    logger.info("=" * 60)
    logger.info("BLUESTOCK MUTUAL FUND ETL PIPELINE")
    logger.info("=" * 60)
    logger.info("CSV files found: %d", len(csv_files))

    for file_path in csv_files:
        process_file(file_path)

    logger.info("=" * 60)
    logger.info("ETL PIPELINE COMPLETED")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()