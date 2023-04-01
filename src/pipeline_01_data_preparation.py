import os
import argparse
import yaml
import logging

def read_params(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)



if __name__=='__main__':
    arg = argparse.ArgumentParser()
    default_config_path = os.path.join("config","params.yaml")
    arg.add_argument("--config",default=default_config_path)
    arg.add_argument("--datasource",default=None)

    parsed_arg = arg.parse_args()
    print(parsed_arg.config, parsed_arg.datasource)
    main(config_path = parsed_arg.config, datasource = parsed_arg.datasource )