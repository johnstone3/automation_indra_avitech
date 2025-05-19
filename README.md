# Requirements

- Python>=3.11
- Poetry>=1.6.1
 
## Project structure
```
Project root
│
├── .gitignore            # Specifies intentionally untracked files that Git should ignore
├── .python-version       # Specifies the Python version to use
├── conftest.py           # Pytest configuration file
├── Makefile              # Automation of common tasks (e.g., running tests, building documentation)
├── poetry.lock           # Records the exact versions of dependencies used in the project
├── pyproject.toml        # Poetry configuration file for project metadata and dependencies
├── README.md             # Provides information about the project
├── environment/          # Contains environment-specific configuration files
│   ├── test.yaml         # Example environment configuration file for testing
│   ...
├── features/             # Contains BDD feature definitions
│   ├── featureA/         
│       ├── featureName.feature 
├── resources/            # Contains non-code resources used by the tests
│   ├── featureA/         
│       ├── resource.txt    
└── src/                  # Main source code directory
```

# Preparation

If you have both Python and Poetry installed, you can run the following command:

```bash
poetry install
```

Make sure you have installed Playwright and the required browsers. You can do this by running:

```bash
poetry run playwright install
```

To run the tests, the following environment variables need to be set:

```
SECRETS_DECRYPTION_KEY=xxxxxxxxxx
ENV_NAME=test
```

* `SECRETS_DECRYPTION_KEY`: This key is used to decrypt sensitive data (such as passwords) during tests. It must be set to the same value that was used to encrypt this data. If this variable is not defined, the raw, encrypted value defined as the secret will be used directly, and no decryption will be performed. This is suitable for local development. The value for `SECRETS_DECRYPTION_KEY` can be obtained from the secrets holder.
* `ENV_NAME`: This variable specifies the environment in which the tests are run. In this case, it is set to "test", which means that the tests will use the configuration designated for the test environment. Test environments are stored in the `./environment` directory, and the value of this variable should match the name of the file in that directory (without the file extension).

# Execution in Intellij

The tests were created in IntelliJ IDEA, therefore this manual describes running tests from IntelliJ IDEA.

## Setting Environment Variables for Pytest in IntelliJ
This guide describes how to set environment variables for your Pytest test configurations in IntelliJ. This is useful for passing configuration values, such as API keys or environment settings, to your tests.

**Steps:**

1. **Open Run/Debug Configurations:**
   - Go to Run > Edit Configurations...
2. **Select Edit configuration templates...:**
   - In the "Run/Debug Configurations" dialog, select the Edit configuration templates... in bottom left corner.
3. **Set working directory:**
   - In the configuration settings, locate the "Working directory" field.
   - Set it to your project root directory. This ensures that Pytest is executed from the project root, which is important for resolving file paths and project resources correctly.
3. **Set Environment Variables:**
    - In the configuration settings, locate the "Environment variables" field.
    - Click the browse button (it looks like three dots "...").
4. **Add your variables:**
    - In the "Environment Variables" dialog, click the "+" button to add a new variable.
    - Enter the variable name (e.g., SECRETS_DECRYPTION_KEY) in the "Name" column.
    - Enter the variable value (e.g., your_secret_key_value) in the "Value" column.
    - Repeat this step for any other environment variables you need to set (e.g., ENV_NAME=test).
5. **Apply and OK:**
    - Click OK to close the "Environment Variables" dialog.
    - Click OK again to save the changes to your Run/Debug configuration.

Now you can run tests directly by clicking the green "Play" button in the editor's left-hand gutter when you have a *.py file containing tests open. IntelliJ will automatically use the appropriate run configuration.

# Using the Makefile

The Makefile provides convenient commands for running tests, generating decryption keys, encrypting secrets, and decrypting secrets.

**Prerequisites**
- Poetry: Ensure you have Poetry installed for managing Python dependencies.

**Variables**

The following variables are used in the Makefile:
- `DECRYPTION_KEY`:  This variable stores the decryption key.  Important: Replace  <placeholder>  with your actual decryption key.  This should be kept secure.
- `ENCRYPTION_STR`:  This variable stores the string to be encrypted or decrypted.  Replace  <placeholder>  with the string you want to process.

**Commands**

The following commands are available:

- `make runTests`: Execute the project's Pytest test suite with specific environment configuration. The environment variables mentioned in [Preparation](#Preparation) section needs to be set before execution.
- `make generateDecryptionKey`:  Generates a new decryption key using  cryptography  and  Fernet. The key is printed to the console.
- `make encryptSecret`:  Encrypts the string stored in  `ENCRYPTION_STR`  using the  `DECRYPTION_KEY`. The encrypted output is printed to the console. The `SECRETS_DECRYPTION_KEY`  environment variable is set temporarily for the Python script.
- `make decryptSecret`:  Decrypts the `ENCRYPTION_STR`  using the  `DECRYPTION_KEY`.  The decrypted output is printed to the console. The `SECRETS_DECRYPTION_KEY` environment variable is set temporarily for the Python script.