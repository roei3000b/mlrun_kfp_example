from kfp import dsl
import mlrun

@dsl.pipeline(
    name="batch-pipeline-academy",
    description="Example of batch pipeline for Iguazio Academy"
)
def pipeline():
    
    # Ingest the data set
    ingest = mlrun.run_function(
        'get-data',
        handler='get_data',
        outputs=["get_data_result"]
    )
    
    # Train a model   
    train = mlrun.run_function(
        "train-model",
        handler="train_model",
        params={"param1": ingest.outputs["get_data_result"]},
        outputs=["train_model_result"]
    )
    
    # Deploy the model as a serverless function
    deploy = mlrun.run_function(
        "deploy-model",
        handler="deploy_model",
        params={"param2": train.outputs["train_model_result"]},
    )
