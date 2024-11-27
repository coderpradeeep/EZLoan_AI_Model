from pydantic import BaseModel

class DataType(BaseModel):
    no_of_dependents : int
    education : int
    self_employed : int
    income_annum : int
    loan_amount : int
    loan_term : int
    cibil_score : int
    residential_assets_value : int
    commercial_assets_value : int
    luxury_assets_value : int
    bank_asset_value : int