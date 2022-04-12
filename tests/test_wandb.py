import os
import wandb
os.environ["WANDB_API_KEY"] = os.getenv('WANDB_API_KEY')
def test_wandb():
    wandb.login()
    wandb.init(project="my-awesome-hello")
    wandb.alert(
    title="Low accuracy"
    )  
    wandb.log({'loss': 11111})
    return True

if __name__ == '__main__':
    test_wandb()