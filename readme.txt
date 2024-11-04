Project: Employee Management Backend
- A set of REST APIs allowing a company to efficiently manage their employees' records


NOTE:
- The API documentation is mentioned under 'api_doc.md' file for your quick reference
- Please refer the postman collection for API examples and documentation
  -- Employee_Management_REST_APIs.postman_collection.json
- ADMIN PORTAL: (HEADLESS CMS)
  -- Please refer admin portal: http://localhost:8000/admin/
  to manage the employee records and users

Creating users who will manage the employees:
- To create a new user, run the below command from the terminal and enter the username and password.
NOTE: email is an optional field
  -- Command: py -m manage createsuperuser

Running the app on the local server:
- Setting up the virtual environment: Execute the below commands on the terminal from the project root directory
  -- Create Command: py -m venv .venv
  -- Activate Command (Windows): .\.venv\Scripts\activate
  -- For Mac OS please refer the following link:
    --- https://python.land/virtual-environments/virtualenv
- Ensure all the dependencies in the requirements.txt file are installed
- To run the app, open the terminal and execute the below command:
  -- Command: py -m manage runserver
- Running tests:
  -- Open the terminal and execute the below command:
    --- Executing all the tests:
      ---- Command: pytest
    --- Executing tests from a specific module
      ---- Command: pytest employee_mgmt/tests/test_models.py
    --- Executing a specific test
      ---- Command: pytest employee_mgmt/tests/test_views.py::test_accessing_employees_endpoint_requires_authentication
  -- NOTE:
    --- Live logging is enabled in pytest settings.
    --- Disabling live log: Refer <project_root>/pytest.ini file and update the below flag
      ---- log_cli = 0

Endpoints:
- employees: [SECURED]
  -- list: GET api/employees/
    --- returns a list of all the employees
  -- create: POST api/employees/
    --- creates a new employee
  -- retrieve: GET api/employees/<int:id>/
    --- retrieves the details of an employee by its id, specified in the path parameter
  -- update: PUT api/employees/<int:id>/
    --- updates the details of an employee, identified by the given id
    --- All the mandatory fields (i.e., name, email) are required
  -- partial_update: PATCH api/employees/<int:id>/
    --- partially updates the details of an employee, identified by the given id
  -- delete: DELETE api/employees/<int:id>/
    --- Soft delete of an employee record

- hr_portal:
  -- token_obtain_pair: GET api/token/
    --- returns a pair of access and refresh token if the given user credentials are valid
  -- token_refresh: GET api/token/refresh/
    --- returns a new access token if the given refresh token is valid
