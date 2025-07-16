import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    blob_name = context.get_input()
    metadata = yield context.call_activity("ExtractMetadata", blob_name)
    yield context.call_activity("StoreMetadata", metadata)
    return "Done"

main = df.Orchestrator.create(orchestrator_function)