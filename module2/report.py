import pandas as pd

def generate_report():
    data = {
        "users": 50,
        "active_users": 35,
        "inactive_users": 15
    }

    df = pd.DataFrame([data])

    df.to_csv("report.csv", index=False)

    return "Report generated"