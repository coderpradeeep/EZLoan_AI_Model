import uvicorn
import pickle
from DataType import DataType
from fastapi import FastAPI

app = FastAPI()
pickle_in = open("model-0.1.0.pkl", "rb")
model = pickle.load(pickle_in)


@app.get('/')
async def index():
    return {'message': 'Hello Ji'}


@app.post('/predict')
async def predict_approval(data: DataType):
    data = data.dict()

    no_of_dependents = data['no_of_dependents']
    education = data['education']
    self_employed = data['self_employed']
    income_annum = data['income_annum']
    loan_amount = data['loan_amount']
    loan_term = data['loan_term']
    cibil_score = data['cibil_score']
    residential_assets_value = data['residential_assets_value']
    commercial_assets_value = data['commercial_assets_value']
    luxury_assets_value = data['luxury_assets_value']
    bank_asset_value = data['bank_asset_value']

    prediction = model.predict([[no_of_dependents,
                                 education,
                                 self_employed,
                                 income_annum,
                                 loan_amount,
                                 loan_term,
                                 cibil_score,
                                 residential_assets_value,
                                 commercial_assets_value,
                                 luxury_assets_value,
                                 bank_asset_value]])
    return prediction[0]


# if __name__ == "__main__":
#     uvicorn.run(app, host='0.0.0.0', port=8000)
