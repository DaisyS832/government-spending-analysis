import pandas as pd
import matplotlib.pyplot as plt

CLEANED_PATH = "../data/processed/cleaned_data.csv"

df = pd.read_csv(CLEANED_PATH)

spending_by_state = df.groupby("State")["Award_Value"].sum().sort_values(ascending=False)
top_agencies = df.groupby("Agency")["Award_Value"].sum().sort_values(ascending=False).head(10)
top_recipients = df.groupby("Recipient")["Award_Value"].sum().sort_values(ascending=False).head(10)
top_industries = df.groupby("Industry")["Award_Value"].sum().sort_values(ascending=False).head(10)

spending_by_state.to_csv("../outputs/spending_by_state.csv")
top_agencies.to_csv("../outputs/top_agencies.csv")
top_recipients.to_csv("../outputs/top_recipients.csv")
top_industries.to_csv("../outputs/top_industries.csv")

plt.figure(figsize=(8, 5))
(spending_by_state / 1_000_000_000).sort_values().plot(kind="barh", color="steelblue")
plt.title("Federal Contract Spending by DMV State")
plt.xlabel("Total Award Value (Billions USD)")
plt.ylabel("State")
plt.savefig("../images/spending_by_state.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
(top_agencies / 1_000_000_000).sort_values().plot(kind="barh", color="darkorange")
plt.title("Top 10 Awarding Agencies by Contract Value")
plt.xlabel("Total Award Value (Billions USD)")
plt.ylabel("Agency")
plt.savefig("../images/top_agencies.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
(top_recipients / 1_000_000_000).sort_values().plot(kind="barh", color="indianred")
plt.title("Top 10 Contract Recipients by Award Value")
plt.xlabel("Total Award Value (Billions USD)")
plt.ylabel("Recipient")
plt.savefig("../images/top_recipients.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
(top_industries / 1_000_000_000).sort_values().plot(kind="barh", color="seagreen")
plt.title("Top 10 Industries by Contract Value")
plt.xlabel("Total Award Value (Billions USD)")
plt.ylabel("Industry")
plt.savefig("../images/top_industries.png", bbox_inches="tight")
plt.show()

print("Analysis outputs and visualizations created successfully.")