import yaml
from yaml import Loader

config_a_yaml = """
service-a-1:
  script:
    - echo 'job 1 for service A'
service-a-2:
  script:
    - echo 'job 2 for service A'
"""

config_b_yaml = """
service-b-1:
  script:
    - echo 'job 1 for service B'
service-b-2:
  script:
    - echo 'job 2 for service B'
"""

config_a = yaml.load(config_a_yaml, Loader=Loader)
config_b = yaml.load(config_b_yaml, Loader=Loader)

with open("service-a-config.yaml", 'w') as yamlfile:
    data = yaml.dump(config_a, yamlfile)
    print("config_a write successful")

with open("service-b-config.yaml", 'w') as yamlfile:
    data = yaml.dump(config_b, yamlfile)
    print("config_b write successful")
