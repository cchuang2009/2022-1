# 1. Library imports

from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 2. Create the app object
app = FastAPI()

# . Load trained Pipeline
model = load_model('deployment_20221101_1')
l = [1., 4., 25., 1., 2., 4., 3., 32., 2., 0., 0., 0., 10., 90., 0.]
#features = [Company_of_laptop, TypeName_of_laptop, Cpu_brand_of_laptop, CPU_vel, GPU_of_laptop, ram_in_gb,
#          first_type_of_laptop, first_size, second_type_of_laptop, second_size,
#          touchscreen, Ips, size_in_inches, ppi, os_of_laptop]


class price_metrics(BaseModel):
    Company_of_laptop: float
    TypeName_of_laptop: float
    Cpu_brand_of_laptop : float
    CPU_vel : float
    GPU_of_laptop : float
    ram_in_gb : float
    first_type_of_laptop : float
    first_size : float
    second_type_of_laptop : float
    second_size : float
    touchscreen : float
    Ips : float
    size_in_inches : float
    ppi : float
    os_of_laptop : float
	
# Define predict function
@app.post('/predict')
def get_potability(data: price_metrics):
    received = data.dict()
    Company_of_laptop=received['Company_of_laptop']
    TypeName_of_laptop=received['TypeName_of_laptop']
    Cpu_brand_of_laptop=received['Cpu_brand_of_laptop']
    CPU_vel=received['CPU_vel']
    GPU_of_laptop=received['GPU_of_laptop']
    ram_in_gb=received['ram_in_gb']
    first_type_of_laptop=received['first_type_of_laptop']
    first_size=received['first_size']
    second_type_of_laptop=received['second_type_of_laptop']
    second_size=received['second_size']
    touchscreen=received['touchscreen']
    Ips=received['Ips']
    size_in_inches=received['size_in_inches']
    ppi=received['ppi']
    os_of_laptop=received['os_of_laptop']
    
    predition = model.predict([features]).tolist()[0]
    return {'Predicted Price of the Laptop is about NT$': predition}
     

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
