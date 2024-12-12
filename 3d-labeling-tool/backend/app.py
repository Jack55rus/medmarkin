from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pydicom
import nibabel as nib
import os

app = FastAPI()


# Endpoint to serve DICOM files
@app.get("/dicom")
async def get_dicom(file_name: str):
    file_path = os.path.join("dicom", file_name)  # Assume your DICOM files are stored in the `dicom/` folder
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    dicom_file = pydicom.dcmread(file_path)
    pixel_data = dicom_file.pixel_array.tolist()
    return {"pixels": pixel_data}


# Endpoint to serve NIfTI files
# @app.get("/nifti")
# async def get_nifti(file_name: str):
#     file_path = os.path.join("nifti", file_name)  # Assume your NIfTI files are stored in the `nifti/` folder
#     if not os.path.exists(file_path):
#         return {"error": "File not found"}
#     nifti_image = nib.load(file_path)
#     nifti_data = nifti_image.get_fdata().tolist()
#     return {"data": nifti_data}