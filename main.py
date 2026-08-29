import os
import json
from typing import List, Literal
import pandas as pd
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# ---------------------------------------------------------
# STEP 1: INITIALIZE CLIENT
# ---------------------------------------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

client = genai.Client(api_key=api_key)

# ---------------------------------------------------------
# STEP 2: DEFINE PYDANTIC SCHEMAS (BATCH WRAPPER)
# ---------------------------------------------------------
class SingleReviewAnalysis(BaseModel):
    original_review: str = Field(description="The exact text of the review analyzed.")
    category: Literal[
        "Delivery Issue", 
        "Food Quality", 
        "Payment/Billing", 
        "App Bug", 
        "Positive Experience", 
        "Other"
    ] = Field(description="Primary issue category.")
    sentiment: Literal["Positive", "Neutral", "Negative"] = Field(description="Emotional tone.")
    urgency_level: Literal["Low", "Medium", "High"] = Field(description="Operational urgency.")
    key_issue_summary: str = Field(description="1-sentence summary of the main point.")
    suggested_action: str = Field(description="Action item for the support or operations team.")

# Wrapper to receive all reviews at once in a list
class BatchReviewResponse(BaseModel):
    reviews: List[SingleReviewAnalysis]

# ---------------------------------------------------------
# STEP 3: SAMPLE DATASET
# ---------------------------------------------------------
customer_reviews = [
    "I ordered biryani 90 minutes ago. It still hasn't arrived and the delivery partner is not answering calls!",
    "My money got debited twice for order #49281, but the app shows order failed. Please refund my 650 rupees immediately.",
    "The packaging was neat, and the pasta was hot and fresh. Loved the extra cheese!",
    "The app crashed three times when I tried to apply the flat 50% discount coupon at checkout."
]

# ---------------------------------------------------------
# STEP 4: SINGLE-CALL BATCH EXECUTION
# ---------------------------------------------------------
def main():
    print("🚀 Sending batch reviews to Gemini (1 single call)...")
    
    # Format the reviews into a numbered list
    formatted_input = "\n".join([f"{i+1}. {r}" for i, r in enumerate(customer_reviews)])
    
    # Using 'gemini-3.5-flash-lite' for instant, low-latency execution
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Analyze and categorize each of the following customer reviews:\n\n{formatted_input}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=BatchReviewResponse,
            temperature=0.0
        )
    )

    # Parse JSON
    parsed_json = json.loads(response.text)
    data = parsed_json.get("reviews", [])

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Print summary table
    print("\n" + "="*80)
    print("✅ ANALYSIS COMPLETE - SUMMARY TABLE:")
    print("="*80)
    print(df.to_string(index=False))

    # Save to CSV
    output_filename = "customer_feedback_analysis.csv"
    df.to_csv(output_filename, index=False)
    print(f"\n✓ Saved results to: {output_filename}")

if __name__ == "__main__":
    main()