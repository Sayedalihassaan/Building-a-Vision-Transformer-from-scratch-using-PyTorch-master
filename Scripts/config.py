from pathlib import Path


def get_config() :
    return {
        "batch_size" : 64 , 
        "pin_memory" : True ,
        "num_worker" : 0 ,


        "img_size" : 28 , 
        "patch_size" : 4 , 
        "in_channnels" : 1 ,
        "num_classes" : 10 , 


        "lr" : 0.001 , 
        "epochs" : 5 , 


        "preload" : "latest" , 
        "model_folder" : "model_weights" , 
        "model_basename" : "t_model_"

    }



def get_weights_file_path(config, epoch: str):
    model_folder = f"Vit_{config['model_folder']}"
    model_filename = f"{config['model_basename']}{epoch}.pt"
    return str(Path('.') / model_folder / model_filename)

# Find the latest weights file in the weights folder
def latest_weights_file_path(config):
    model_folder = f"Vit_{config['model_folder']}"
    model_filename = f"{config['model_basename']}*"
    weights_files = list(Path(model_folder).glob(model_filename))
    if len(weights_files) == 0:
        return None
    weights_files.sort()
    return str(weights_files[-1])
