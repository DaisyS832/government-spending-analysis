import pandas as pd

RAW_PATH = "../data/raw/raw_federal_spending.csv"
CLEANED_CSV_PATH = "../data/processed/cleaned_data.csv"
CLEANED_XLSX_PATH = "../data/processed/cleaned_data.xlsx"
SAMPLE_CSV_PATH = "../data/processed/cleaned_data_sample.csv"
SAMPLE_XLSX_PATH = "../data/processed/cleaned_data_sample.xlsx"

df = pd.read_csv(RAW_PATH, low_memory=False)

columns_needed = {
    "recipient_name": "Recipient",
    "awarding_agency_name": "Agency",
    "funding_agency_name": "Funding_Agency",
    "primary_place_of_performance_state_code": "State",
    "primary_place_of_performance_city_name": "City",
    "action_date": "Action_Date",
    "period_of_performance_start_date": "Start_Date",
    "current_total_value_of_award": "Award_Value",
    "naics_description": "Industry",
    "award_description": "Award_Description"
}

existing_columns = [col for col in columns_needed if col in df.columns]

df_clean = df[existing_columns].copy()
df_clean = df_clean.rename(columns={col: columns_needed[col] for col in existing_columns})

df_clean = df_clean[df_clean["State"].isin(["VA", "MD", "DC"])]

df_clean["Action_Date"] = pd.to_datetime(df_clean["Action_Date"], errors="coerce")
df_clean["Start_Date"] = pd.to_datetime(df_clean["Start_Date"], errors="coerce")
df_clean["Award_Value"] = pd.to_numeric(df_clean["Award_Value"], errors="coerce")

df_clean = df_clean.dropna(subset=["Recipient", "Agency", "State", "Award_Value"])
df_clean = df_clean[df_clean["Award_Value"] > 0]
df_clean = df_clean.drop_duplicates()

df_clean.to_csv(CLEANED_CSV_PATH, index=False)
df_clean.to_excel(CLEANED_XLSX_PATH, index=False)

sample_df = df_clean.head(100)
sample_df.to_csv(SAMPLE_CSV_PATH, index=False)
sample_df.to_excel(SAMPLE_XLSX_PATH, index=False)

print("Cleaned DMV dataset created successfully.")
print(f"Rows: {df_clean.shape[0]}")
print(f"Columns: {df_clean.shape[1]}")