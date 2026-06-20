# Multi-Modal Evidence Review System

A modular Python-based pipeline for validating insurance claims using
conversation text, image evidence, user history, and evidence requirements.

The system processes each claim, analyzes supporting evidence, evaluates
potential risks, and generates a structured decision in CSV format.

---

# Project Structure

```text
code/
│── main.py
│── requirements.txt
│── README.md
│
├── dataset/
│   ├── claims.csv
│   ├── sample_claims.csv
│   ├── user_history.csv
│   ├── evidence_requirements.csv
│   └── images/
│
├── modules/
│   ├── claim_parser.py
│   ├── image_checker.py
│   ├── risk_analyzer.py
│   └── decision_engine.py
│
├── evaluation/
│   ├── evaluate.py
│   ├── evaluation_report.md
│   └── sample_output.csv
│
└── output.csv
```

---

# Features

- Modular architecture
- Rule-based claim parsing
- Image evidence validation
- User history analysis
- Risk flag generation
- Claim decision engine
- Severity estimation
- CSV output generation

---

# Requirements

- Python 3.9+
- pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Dataset

Place the following files inside the `dataset/` folder.

```
dataset/
│── claims.csv
│── sample_claims.csv
│── user_history.csv
│── evidence_requirements.csv
└── images/
```

---

# Running the Project

Generate predictions:

```bash
python main.py
```

Output:

```
output.csv
```

---

# Evaluation

Run evaluation on the provided sample dataset:

```bash
python evaluation/evaluate.py
```

Evaluation results will be generated as:

```
evaluation/sample_output.csv
```

---

# System Workflow

```
Claims CSV
      │
      ▼
Claim Parser
      │
      ▼
Image Checker
      │
      ▼
Risk Analyzer
      │
      ▼
Decision Engine
      │
      ▼
output.csv
```

---

# Module Description

## claim_parser.py

Extracts structured information from customer conversations.

Outputs:

- Issue Type
- Object Part

Example:

```
Customer:
Rear bumper has a dent.
```

Result:

```
issue_type = dent
object_part = rear_bumper
```

---

## image_checker.py

Validates submitted images against evidence requirements.

Checks:

- Required images available
- Claimed object visible
- Image validity
- Evidence completeness

Outputs:

- evidence_standard_met
- valid_image
- evidence_standard_met_reason

---

## risk_analyzer.py

Analyzes claim risks using:

- User history
- Image validation
- Evidence completeness

Possible risk flags:

- none
- manual_review_required
- insufficient_evidence
- repeat_claim

---

## decision_engine.py

Combines information from previous modules to determine:

- Claim Status
- Justification
- Supporting Images
- Severity

Possible claim status:

- supported
- contradicted
- not_enough_information

Severity levels:

- low
- medium
- high
- unknown

---

# Output Format

The generated CSV contains:

| Column |
|---------|
| user_id |
| image_paths |
| user_claim |
| claim_object |
| evidence_standard_met |
| evidence_standard_met_reason |
| risk_flags |
| issue_type |
| object_part |
| claim_status |
| claim_status_justification |
| supporting_image_ids |
| valid_image |
| severity |

---

# Design Highlights

- Modular and maintainable architecture
- Single responsibility for each module
- Cached loading of user history and evidence rules
- Rule-based deterministic processing
- Easy to extend with computer vision or LLM models
- Reproducible outputs

---

