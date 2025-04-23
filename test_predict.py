import joblib
import pandas as pd


model = joblib.load('model.pkl')
data = {"Weight": 9.3,
        "ProductVisibility": 0.016047301,
        "MRP": 249.8092,
        "EstablishmentYear": 1999,
        "ProductID": "FDX07",
        "FatContent": "Low Fat",
        "ProductType": "Snack Foods",
        "OutletID": "OUT045",
        "OutletSize": "Medium",
        "LocationType": "Tier 2",
        "OutletType": "Supermarket Type1"
        }
input_df = pd.DataFrame([data])
prediction = model.predict(input_df)

print("predicted OutletSales", prediction)

