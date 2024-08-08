import time

# Define inline function for 'train-model'
def train_model(context, param1):
    time.sleep(5)  # Simulate work by sleeping for 5 seconds
    context.log_result("train_model_result", "11")