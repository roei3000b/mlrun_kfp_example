import time

# Define inline function for 'get-data'
def get_data(context):
    time.sleep(5)  # Simulate work by sleeping for 5 seconds
    context.log_result("get_data_result", "10")