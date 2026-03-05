import pandas as pd
import numpy as np

np.random.seed(42)

num_patients = 5000

data = {
    "patient_id": range(1, num_patients + 1),

    "age": np.random.randint(18, 42, num_patients),

    "risk_level": np.random.choice(
        ["low", "moderate", "high"],
        num_patients,
        p=[0.55, 0.30, 0.15]
    ),

    "gestational_diabetes": np.random.choice(
        [0,1],
        num_patients,
        p=[0.85,0.15]
    ),

    "hypertension": np.random.choice(
        [0,1],
        num_patients,
        p=[0.88,0.12]
    ),

    "therapy_sessions": np.random.poisson(1.2, num_patients),

    "nutrition_visits": np.random.poisson(2.0, num_patients),

    "messages_sent": np.random.poisson(8, num_patients),

    "response_time_hours": np.random.normal(3.5,1.0,num_patients).clip(0.5,10),

    "no_show": np.random.choice(
        [0,1],
        num_patients,
        p=[0.90,0.10]
    )
}

df = pd.DataFrame(data)

# Outcome probabilities influenced by risk
df["preterm_birth"] = (
    (df["risk_level"]=="high")*np.random.binomial(1,0.25,num_patients) +
    (df["risk_level"]=="moderate")*np.random.binomial(1,0.12,num_patients) +
    (df["risk_level"]=="low")*np.random.binomial(1,0.06,num_patients)
)

df["nicu_admission"] = (
    df["preterm_birth"] *
    np.random.binomial(1,0.6,num_patients)
)

df["postpartum_depression_screened"] = np.random.choice(
    [0,1],
    num_patients,
    p=[0.2,0.8]
)

df["cost_of_care"] = (
    9000 +
    df["nicu_admission"]*25000 +
    df["preterm_birth"]*10000 +
    np.random.normal(0,2000,num_patients)
)

df.to_csv("maternal_population_data.csv", index=False)

print("Dataset created: maternal_population_data.csv")
