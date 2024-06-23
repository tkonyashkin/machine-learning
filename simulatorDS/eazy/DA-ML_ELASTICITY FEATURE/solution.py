import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:
    results = []

    skus = df['sku'].unique()

    for sku in skus:
        sku_data = df[df['sku'] == sku]
        
        if len(sku_data) > 1:
            log_price = np.log(sku_data['price'].values).reshape(-1, 1)
            log_qty = np.log(sku_data['qty'].values + 1).reshape(-1, 1)

            model = LinearRegression().fit(log_price, log_qty)
            
            log_qty_pred = model.predict(log_price)

            r2 = r2_score(log_qty, log_qty_pred)
            results.append({'sku': sku, 'elasticity': r2})

    results_df = pd.DataFrame(results)
    
    return results_df
