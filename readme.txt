Project: Employee Management Backend
- A set of REST APIs allowing a company to efficiently manage their employees' records


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
