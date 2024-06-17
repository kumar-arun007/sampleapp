from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Dummy list of medicines (replace with actual data if available)
medicines = [
    {"name": "Humalog", "description": "Insulin lispro, used to treat diabetes mellitus."},
    {"name": "Humulin", "description": "Various formulations of insulin for diabetes treatment."},
    {"name": "Trulicity", "description": "Dulaglutide, used for the treatment of type 2 diabetes."},
    {"name": "Taltz", "description": "Ixekizumab, used to treat autoimmune conditions such as psoriasis."},
    {"name": "Cyramza", "description": "Ramucirumab, used to treat various types of cancer."},
    {"name": "Verzenio", "description": "Abemaciclib, used for the treatment of breast cancer."},
    {"name": "Olumiant", "description": "Baricitinib, used for the treatment of rheumatoid arthritis."},
    {"name": "Alimta", "description": "Pemetrexed, used for the treatment of lung cancer."},
    {"name": "Cymbalta", "description": "Duloxetine, used primarily as an antidepressant."},
    {"name": "Zyprexa", "description": "Olanzapine, used to treat schizophrenia."}
]

# Model to define the structure of a medicine
class Medicine(BaseModel):
    name: str
    description: str

# Endpoint to list all medicines
@app.get("/medicines", response_model=list[Medicine], tags=["medicines"])
def list_medicines():
    return medicines

# Endpoint to get medicine by name
@app.get("/medicine/{medicine_name}", response_model=Medicine, tags=["medicines"])
def get_medicine(medicine_name: str):
    for med in medicines:
        if med["name"].lower() == medicine_name.lower():
            return med
    raise HTTPException(status_code=404, detail="Medicine not found")

# Include OpenAPI tags metadata for grouping in Swagger UI
tags_metadata = [
    {"name": "medicines", "description": "Operations related to medicines."},
]

# Include additional metadata for OpenAPI docs (optional)
app.openapi_tags = tags_metadata

# Run the application with uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
