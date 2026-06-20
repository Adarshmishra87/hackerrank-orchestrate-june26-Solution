import pandas as pd
from main import process_claims

def evaluate():
    process_claims("dataset/sample_claims.csv", "dataset/user_history.csv", "dataset/evidence_requirements.csv", "evaluation/sample_output.csv")
    print("Evaluation complete. Check evaluation/sample_output.csv")

if __name__ == "__main__":
    evaluate()
