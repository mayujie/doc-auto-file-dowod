import yaml


# Load the YAML configuration
def load_config(config_file: str):
    if config_file.endswith('.yaml') or config_file.endswith('.yml'):
        with open("", "r") as file:
            config = yaml.safe_load(file)
        return config
    else:
        raise ValueError("Invalid configuration file format. Use either '.yaml' or '.yml'.")
