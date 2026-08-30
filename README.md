# 🛡️ AI Customer Feedback & Review Categorizer (Structured Data Pipeline)

An automated AI data pipeline built in Python using **Google Gemini 3.5 Flash Lite** and **Pydantic**. It transforms raw, unstructured customer reviews into deterministic, categorized JSON schemas and exports structured datasets directly to CSV.

---

## 📌 Project Overview
- **The Problem:** Processing thousands of customer reviews manually is slow and error-prone, while standard LLMs return messy, conversational paragraphs that cannot be parsed by backend databases or analytics tools.
- **The Solution:** A deterministic data pipeline enforcing strict Pydantic schemas (`Literal` constraints) to categorize feedback, score operational urgency, and recommend actionable resolutions in batch requests.

---

## 🚀 Key Technical Features
* **Deterministic Schema Validation:** Utilizes Pydantic `BaseModel` and `Field` definitions to guarantee 100% structured JSON outputs with zero hallucination (`temperature=0.0`).
* **Batch Request Optimization:** Processes multiple reviews in a single API call to reduce latency and eliminate rate-limit bottlenecks.
* **Automated Data Export:** Automatically parses JSON responses into Pandas DataFrames and generates clean `.csv` files ready for downstream databases or BI tools.
* **Security Best Practices:** API keys and sensitive environment variables are kept isolated via `python-dotenv` and `.gitignore`.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **LLM Engine:** Google Gemini API (`gemini-3.5-flash-lite`)
- **Schema Validation:** Pydantic
- **Data Manipulation:** Pandas
- **Environment Management:** `python-dotenv`

---

## 💻 Local Setup & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/lakshmi-192/AI_Feedback_Analyzer.git
cd AI_Feedback_Analyzer
2. Create and activate virtual environment:Bash# Windows
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies:Bashpip install google-genai pydantic pandas python-dotenv
4. Configure API Key:Create a .env file in the root directory:Code snippetGEMINI_API_KEY=your_gemini_api_key_here
5. Run the pipeline:Bashpython main.py
📊 Sample OutputCategorySentimentUrgencyKey Issue SummarySuggested ActionDelivery IssueNegativeHighOrder delayed by 90 mins; rider unreachable.Contact rider & process refund/compensation.Payment/BillingNegativeHighDouble deduction for failed order #49281.Verify gateway log & initiate ₹650 refund.Positive ExperiencePositiveLowPraised packaging, food quality, and temperature.Forward appreciation to restaurant partner.App BugNegativeMediumMobile app crashed repeatedly on coupon apply.Escalate bug report to mobile engineering.
# 🛡️ AI Customer Feedback & Review Categorizer (Structured Data Pipeline)

An automated AI data pipeline built in Python using **Google Gemini 3.5 Flash Lite** and **Pydantic**. It transforms raw, unstructured customer reviews into deterministic, categorized JSON schemas and exports structured datasets directly to CSV.

---

## 📌 Project Overview
- **The Problem:** Processing thousands of customer reviews manually is slow and error-prone, while standard LLMs return messy, conversational paragraphs that cannot be parsed by backend databases or analytics tools.
- **The Solution:** A deterministic data pipeline enforcing strict Pydantic schemas (`Literal` constraints) to categorize feedback, score operational urgency, and recommend actionable resolutions in batch requests.

---

## 🚀 Key Technical Features
* **Deterministic Schema Validation:** Utilizes Pydantic `BaseModel` and `Field` definitions to guarantee 100% structured JSON outputs with zero hallucination (`temperature=0.0`).
* **Batch Request Optimization:** Processes multiple reviews in a single API call to reduce latency and eliminate rate-limit bottlenecks.
* **Automated Data Export:** Automatically parses JSON responses into Pandas DataFrames and generates clean `.csv` files ready for downstream databases or BI tools.
* **Security Best Practices:** API keys and sensitive environment variables are kept isolated via `python-dotenv` and `.gitignore`.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **LLM Engine:** Google Gemini API (`gemini-3.5-flash-lite`)
- **Schema Validation:** Pydantic
- **Data Manipulation:** Pandas
- **Environment Management:** `python-dotenv`

---

## 💻 Local Setup & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/lakshmi-192/AI_Feedback_Analyzer.git
cd AI_Feedback_Analyzer
2. Create and activate virtual environment:Bash# Windows
python -m venv venv
.\venv\Scripts\activate
3. Install dependencies:Bashpip install google-genai pydantic pandas python-dotenv
4. Configure API Key:Create a .env file in the root directory:Code snippetGEMINI_API_KEY=your_gemini_api_key_here
5. Run the pipeline:Bashpython main.py

## 📊 Sample Output

| Category | Sentiment | Urgency | Key Issue Summary | Suggested Action |
| :--- | :--- | :--- | :--- | :--- |
| `Delivery Issue` | **Negative** | `High` | Order delayed by 90 mins; rider unreachable | Contact rider & process refund/compensation |
| `Payment/Billing` | **Negative** | `High` | Double deduction for failed order #49281 | Verify gateway log & initiate ₹650 refund |
| `Positive Experience` | **Positive** | `Low` | Praised packaging, food quality, and temperature | Forward appreciation to restaurant partner |
| `App Bug` | **Negative** | `Medium` | Mobile app crashed repeatedly on coupon apply | Escalate bug report to mobile engineering |

