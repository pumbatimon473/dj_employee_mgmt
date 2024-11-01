Project: Employee Management Backend
- A set of REST APIs allowing a company to efficiently manage their employees' records


Endpoints:
- employees:
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
    --- Hard delete of an employee record

