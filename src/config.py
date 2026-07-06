from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Raw Data
TRAIN_DATA = BASE_DIR / "data" / "raw" / "train.txt"
VAL_DATA = BASE_DIR / "data" / "raw" / "val.txt"
TEST_DATA = BASE_DIR / "data" / "raw" / "test.txt"

# Processed Data
PROCESSED_DATA = BASE_DIR / "data" / "processed"

# Models
MODEL_DIR = BASE_DIR / "models"

# Output
OUTPUT_DIR = BASE_DIR / "outputs"
FIGURE_DIR = OUTPUT_DIR / "figures"
REPORT_DIR = OUTPUT_DIR / "reports"
PREDICTION_DIR = OUTPUT_DIR / "predictions"