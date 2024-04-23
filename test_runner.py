# import os
# import sys
# import configparser
# import pytest

# def load_env(env):
#     global env_vars
#     # Read configurations from the .env file
#     config = configparser.ConfigParser()
#     config.read('.env')

#     # Load configurations from the [COMMON] section
#     if 'COMMON' in config:
#         for key, value in config['COMMON'].items():
#             os.environ[key] = value

#     # Load configurations for the specified environment
#     if env.upper() in config:
#         for key, value in config[env.upper()].items():
#             os.environ[key] = value

#     # Initialize an empty dictionary to store environment variables
    
#     env_vars = {}

#     # Load common variables into the 'common' sub-object
#     if 'COMMON' in config:
#         env_vars['common'] = dict(config.items('COMMON'))

#     # Load environment-specific variables at the top level
#     if env.upper() in config:
#         env_vars.update(dict(config.items(env.upper())))

#     return env_vars

# def main():
#     # Check if the script is named "local_test.py" or "local_dev.py"
#     scriptName = os.path.basename(sys.argv[0])
#     environment = 'default'
#     if scriptName == 'local_dev.cmd':
#         environment = 'dev'      
#     elif scriptName == 'local_test.cmd':
#         environment = 'test'
#     elif scriptName == 'local_stage.cmd':
#         environment = 'stage' 
#     elif scriptName == 'dev.cmd':
#         environment = 'dev'      
#     elif scriptName == 'test.cmd':
#         environment = 'test'
#     elif scriptName == 'stage.cmd':
#         environment = 'stage'  
#     load_env(environment)

#     # Run your tests here
#     print("Running tests on: ", environment)
    
#     # Specify the path for the JUnit XML report
#     junit_xml_path = 'test-results.xml'
    
#     # Run pytest with the --junitxml option
#     pytest.main(['--junitxml=' + junit_xml_path])

# if __name__ == "__main__":
#     main()


import os
import sys
import configparser
import pytest

# def load_env(env,scriptName):
#     global env_vars
#     # Read configurations from the .env file
#     config = configparser.ConfigParser()
#     if scriptName.startswith('local_'):
#         config.read('.local.env')
#     else:
#         config.read('.env')

#     # Load configurations from the [COMMON] section
#     if 'COMMON' in config:
#         for key, value in config['COMMON'].items():
#             os.environ[key] = value

#     # Load configurations for the specified environment
#     if env.upper() in config:
#         for key, value in config[env.upper()].items():
#             os.environ[key] = value

#     # Initialize an empty dictionary to store environment variables
#     env_vars = {}

#     # Load common variables into the 'common' sub-object
#     if 'COMMON' in config:
#         env_vars['common'] = dict(config.items('COMMON'))

#     # Load environment-specific variables at the top level
#     if env.upper() in config:
#         env_vars.update(dict(config.items(env.upper())))

#     return env_vars

def load_env(env, scriptName):
    global env_vars
    # Read configurations from the .env file
    config = configparser.ConfigParser()
    if scriptName.startswith('local_'):
        config.read('.local.env')
    else:
        config.read('.env')

    # Load configurations from the [COMMON] section
    if 'COMMON' in config:
        env_vars = dict(config.items('COMMON'))

    # Load configurations for the specified environment
    if env.upper() in config:
        env_vars.update(dict(config.items(env.upper())))

    return env_vars

def main():
    # Check if the script is named "local_test.py" or "local_dev.py"
    scriptName = os.path.basename(sys.argv[0])
    environment = 'default'
    if scriptName.endswith('dev.cmd'):
        environment = 'dev'      
    elif scriptName.endswith('test.cmd'):
        environment = 'test'
    elif scriptName.endswith('stage.cmd'):
        environment = 'stage'   
    load_env(environment, scriptName)

    # Run your tests here
    print("Running tests on: ", environment)
    
    # Run pytest with the --junitxml option
    junit_xml_path = 'test-results.xml'
    
    pytest.main(['--junitxml=' + junit_xml_path])

if __name__ == "__main__":
    main()