import logging
import azure.functions as func
import azure.durable_functions as df

async def main(myblob: func.InputStream, starter: str):
    logging.info(f"Blob uploaded: {myblob.name}")
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("ImageOrchestrator", None, myblob.name)
    logging.info(f"Started orchestration: {instance_id}")