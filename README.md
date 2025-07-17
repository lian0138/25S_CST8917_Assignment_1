
# CST8917 Assignment 1: Durable Workflow for Image Metadata Processing

**Due:** July 19, 2025  
**Submission:** GitHub repository with code, documentation, and demo video link

---

## Demo Video

- [Demo Video Link](https://your-youtube-demo-link-here)

---

## Project Overview

This project implements a cloud-based, serverless workflow for automatic image metadata processing using Azure Durable Functions (Python). When an image is uploaded to Azure Blob Storage, the system extracts image metadata and stores it in Azure SQL Database, supporting scalable and reliable data processing for content management scenarios.

---

## Workflow and Implementation

**Azure Blob Storage**  
Azure Blob Storage is used as the system’s entry point, where images (`.jpg`, `.png`, `.gif`) are uploaded by users to the `images-input` container. This service supports scalable, event-driven storage for new content.

**Blob Trigger Function**  
A Blob-triggered Azure Function monitors the `images-input` container for new uploads. When a file is detected, this function automatically starts a Durable Function orchestration, enabling immediate and automated response to each upload.

**Durable Orchestrator Function**  
The orchestrator function, running inside the Azure Function App, reliably manages the processing sequence. It coordinates two activity functions—extracting metadata first, then storing it—while ensuring tasks are executed in order with error handling.

**Extract Metadata Activity Function**  
This activity downloads the uploaded image using storage APIs, then analyzes it with the Pillow library. It extracts the file name, file size (KB), image dimensions (pixels), and format, creating a standardized metadata record for each image.

**Store Metadata Activity Function**  
Once metadata extraction is complete, another activity function writes this data into an `ImageMetadata` table in Azure SQL Database. Storing metadata centrally allows for easy retrieval, analysis, or further automated review.

**Azure SQL Database**  
The Azure SQL Database serves as persistent storage for all image metadata records. Centralized storage in a relational database supports efficient queries and integration with downstream systems.

**Summary**  
By combining Blob Storage, Durable Functions, and SQL Database, this design provides a robust, serverless image metadata pipeline. It automates the entire content ingestion and indexing process for efficient cloud-based data handling.

---

## Workflow Diagram

```
+------------------------+
|    Azure Blob Storage  |
|  (images-input bucket) |
+------------------------+
             |
             v
+-----------------------------+
|  Blob Trigger Function      |
|(detects new image upload)   |
+-----------------------------+
             |
             v
+-----------------------------+
| Durable Orchestrator        |
|  (controls processing flow) |
+-----------------------------+
       |                    |
       v                    v
+-----------------+   +----------------------+
| ExtractMetadata |   | StoreMetadata        |
| Activity        |   | Activity             |
| (extract fields)|   | (write to SQL table) |
+-----------------+   +----------------------+
             |                |
             +----------------+
                            |
   +--------------------------+
   |  Azure SQL Database      |
   |(stores image metadata)   |
   +--------------------------+
```

---

## Project File Structure

```
.
├── BlobTriggerStarter/
│   └── __init__.py           # Starts orchestration on new blob upload
├── ImageOrchestrator/
│   └── __init__.py           # Controls workflow sequence
├── ExtractMetadata/
│   └── __init__.py           # Extracts image metadata
├── StoreMetadata/
│   └── __init__.py           # Stores metadata in SQL database
├── requirements.txt          # Python dependency list
├── local.settings.json       # Local development settings (connections)
└── README.md                 # Assignment documentation
```

Each function is organized into its own folder for deployment as an Azure Function. Supporting files define dependencies, connections, and documentation.

---

## References

- [Azure Durable Functions (Python)](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-python-overview)
- [Azure Functions Blob Trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger)
- [Python and Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/connect-query-python)

---

**Author:** [Your Name]  
**Course:** CST8917  
**Date:** July 2025
```