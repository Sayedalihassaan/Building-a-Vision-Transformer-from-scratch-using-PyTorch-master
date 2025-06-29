from pathlib import Path
import os
import logging




list_of_files = [
    "README.md" , 
    "requiremets.txt" , 
    "images" , 
    "Notebookes/main.ipynb" , 
    "Notebookes/train.py" , 
    "Scripts/architecture.py" , 
    "Scripts/config.py" , 
    "Scripts/inferance.py" , 
    "Scripts/main.py" , 
    "Scripts/trainer.py"
]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")