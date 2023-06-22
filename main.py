import subprocess

def setup(obj):
    for i in obj:
        print(type(i["cmd"]))
        result = subprocess.run(i["cmd"], shell=True, capture_output=True, text=True)
        print(result.stdout)
    return


obj =[{"cmd":["pip", "install", "virtualenv"]},
      {"cmd":["virtualenv", "env"]},
      {"cmd":["D:\FastAPIDemo\venv\Scripts\Activate"]},
      {"cmd":["pip", "install", "fastapi"]},
      {"cmd":["pip", "install", "django"]},
      {"cmd":["pip", "list"]}
      # {"cmd":["D:\FastAPIDemo\venv\Scripts\deactivate"]}
      ]
# print(obj)
# result= (["pip","install","virtualenv"], shell=True, capture_output=True, text=True)
print(setup(obj))