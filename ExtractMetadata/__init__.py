from PIL import Image
import io
import os
from azure.storage.blob import BlobServiceClient

def main(blob_name: str) -> dict:
    print("ExtractMetadata收到的blob_name:", blob_name, flush=True)  # 日志
    blob_name = os.path.basename(blob_name)  # 关键修正，保证只有文件名
    
    connection_string = os.environ["AzureWebJobsStorage"]
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container="images-input", blob=blob_name)
    blob_data = blob_client.download_blob().readall()
    
    with Image.open(io.BytesIO(blob_data)) as img:
        return {
            "FileName": blob_name,
            "FileSizeKB": len(blob_data) / 1024,
            "Width": img.width,
            "Height": img.height,
            "Format": img.format
        }