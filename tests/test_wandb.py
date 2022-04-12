import os
print("api key: {}".format(os.getenv('WANDB_API_KEY')))
print("api key: {}".format(os.getenv('WANDB_API_KEY')))
os.environ["WANDB_API_KEY"] = os.getenv('WANDB_API_KEY')