import sys
import yaml
from yaml import Loader

config_all_yaml = """
service-a-1:
  script:
    - echo 'job 1 for service A'
service-a-2:
  script:
    - echo 'job 2 for service A'
service-b-1:
  script:
    - echo 'job 1 for service B'
service-b-2:
  script:
    - echo 'job 2 for service B'
"""

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

print(sys.argv)
print(sys.argv[0])
if sys.argv[0] == "a":
    selected_config = config_a_yaml
elif sys.argv[0] == "b":
    selected_config = config_b_yaml
else:
    selected_config = config_all_yaml

config = yaml.load(selected_config, Loader=Loader)

with open("config.yaml", 'w') as yamlfile:
    data = yaml.dump(config, yamlfile)
    print("config write successful")
