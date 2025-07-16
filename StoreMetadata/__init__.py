import pyodbc
import os

def main(metadata: dict):
    conn_str = os.environ["SqlConnectionString"]
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.ImageMetadata (FileName, FileSizeKB, Width, Height, Format)
            VALUES (?, ?, ?, ?, ?)
        """, (metadata['FileName'], metadata['FileSizeKB'], metadata['Width'], metadata['Height'], metadata['Format']))
        conn.commit()
    return "Metadata inserted manually"