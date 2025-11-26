from tempfile import SpooledTemporaryFile
from fastapi import APIRouter,UploadFile,File
from csv_handler import load_and_save_data_from_scv_and_return_data

router = APIRouter(prefix="/csv",tags= ["csv"])

@router.post("/assignWithCsv")
def upload_csv(file: UploadFile = File(...)):
    temp_file = SpooledTemporaryFile()
    temp_file.write(file.file.read())
    temp_file.seek(0)
    return load_and_save_data_from_scv_and_return_data(temp_file)







