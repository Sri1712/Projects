## dbt (Data Build Tool)

* Tool for transforming data within data warehouse.
* It's a development framework that combines modular SQL with software engineering practices to make data transformation fast and reliable.
* It allows writing and deploying analytical code using SQL or Python.
* The primary function is to transform raw data from multiple sources into meaningful formats for analysis.


#### Installation:

1. Install virtualenv:
In Command Prompt, run the following command to install virtualenv:
        pip install virtualenv

2. Verify virtualenv Installation:
After installation, check if virtualenv is installed:
        py -m virtualenv --version
If it shows a version number, the installation is successful.

3. Create a Virtual Environment for dbt
Now that virtualenv is installed, we can create a virtual environment for the dbt installation.
    a. Navigate to Your Project Directory:
        First, move to the directory where you want to create your virtual environment. You can create a new directory if needed:
            mkdir dbt_project
            cd dbt_project
    b. Create a Virtual Environment:
        Create the virtual environment by running:
            python -m venv dbt-env
        This will create a new folder called dbt-env in your project directory containing a clean Python environment.

4. Activate the Virtual Environment
Before installing dbt, you need to activate the virtual environment.
    * Activate the Virtual Environment:
        In Command Prompt, run the following command to activate the virtual environment:
        For Command Prompt:
            ecomm_env\Scripts\activate

    After activation, you’ll notice that your command prompt now shows (dbt-env) before your command line, indicating that the virtual environment is active.

5. Install dbt in the Virtual Environment
    With the virtual environment activated, you can now install dbt.
        1. Install dbt-core:
            In the activated environment, install dbt using the following command:
                pip install dbt-core
        2. Install a dbt Adapter:
            Install the appropriate adapter depending on your platform:
                For Snowflake:
                    pip install dbt-snowflake
                For BigQuery:
                    pip install dbt-bigquery
                For Redshift:
                    pip install dbt-redshift
                For Postgres:
                    pip install dbt-postgres
If this installation process failed check this steps for resolution.

6. Verify dbt Installation
1. Check dbt Version:
After installation, verify that dbt is installed correctly by running:
        css
        dbt --version
This command should display the installed versions of dbt-core and any other installed adapters (e.g., dbt-snowflake).
Step 8: Set Up Your First dbt Project
1. Initialize a New dbt Project:
In the activated virtual environment, navigate to the directory where you want to create your project and run:
        csharp
        dbt init my_project
This will create a new dbt project folder called my_project with the necessary dbt structure.
2. Configure dbt Profiles:
After creating the project, configure the profiles.yml file, which contains your connection details to your data warehouse (e.g., Snowflake, BigQuery).


python -m pip install -r requirements.txt
