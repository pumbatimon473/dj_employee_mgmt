# Endpoints: hr_portal

## API Token Request
This endpoint is used to authenticate and obtain a token for accessing protected resources.

### Request Body
- `username` (string) - The username of the user.
- `password` (string) - The password of the user.

### Response
The response is in JSON format and includes the following fields:
- `refresh` (string) - The refresh token for obtaining a new access token.
- `access` (string) - The access token for accessing protected resources.

### JSON Schema
```JSON
{
    "type": "object",
    "properties": {
        "refresh": {
            "type": "string"
        },
        "access": {
            "type": "string"
        }
    }
}
```

## API Refresh Token Request
This endpoint is used to refresh an access token by sending a POST request to the specified URL. The request should include a JSON payload with a "refresh" key containing the refresh token.

### Request Body
- `refresh` (string, required): The refresh token used to obtain a new access token.

### Response
The response to this request is a JSON object with the "access" key, which contains the new access token.

### JSON Schema
```JSON
{
    "type": "object",
    "properties": {
        "access": {
            "type": "string"
        }
    }
}
```


# Endpoints: employee_mgmt
> **NOTE:** All the below endpoints are **secured** and requires authorization.
> **Authorization:** `Bearer Token`

## Get Employee Data
This endpoint makes a GET request to retrieve employee data.

### Request
- Method: GET
- URL: `http://localhost:8000/api/employees/`

### Query Params
- `department`: applicable values `HR`, `ENGINEERING`, `SALES`
- `role`: applicable values `DEVELOPER`, `MANAGER`, `ANALYST`
- `department__in`: inclusive filter to allow filtering the results on multiple values e.g., `HR, SALES`
- `role_in`: inclusive filter to allow filtering the results on multiple values e.g., `MANAGER, ANALYST`
- `department__not`: allows filtering the results not having the mentioned department
- `role__not`: allows filtering the results not having the mentioned role
- `department__not__in`: exclusive filter to allow filtering the results not having the mentioned values
e.g., `HR, SALES`
- `role__not__in`: exclusive filter to allow filtering the results not having the mentioned values
e.g., `ANALYST, MANAGER`
- `page`: allows you to retrieve the mentioned page number from the paginated resultset e.g., `2` or `last`

### Response Body
The response returns a JSON object with the following structure:
- `count` (number): The total count of employees.
- `next` (string): Link to the next page of results.
- `previous` (string): Link to the previous page of results.
- `results` (array): An array of employee objects containing the following fields:
  - `id` (number): The unique identifier of the employee.
  - `created_at` (string): The date and time when the employee record was created.
  - `updated_at` (string): The date and time when the employee record was last updated.
  - `name` (string): The name of the employee.
  - `email` (string): The email address of the employee.
  - `department` (string): The department of the employee.
  - `role` (string): The role of the employee.
  - `date_joined` (string): The date when the employee joined.

A successful response will have a `200 OK` status.


## Create New Employee
This endpoint is used to create a new employee by submitting a POST request to the specified URL.

### Request
- Method: POST
- URL: `http://localhost:8000/api/employees/`

### Input
The request body should be in JSON format and include the following parameters:
- `name` (string): The name of the employee.
- `email` (string): The email address of the employee.
- `department` (string): Optional. The department to which the employee belongs.
- `role` (string): Optional. The role or designation of the employee.

Example request body:
```JSON
{
  "name": "Joe Dalton",
  "email": "joe@dalton.com",
  "department": "SALES",
  "role": "ANALYST"
}
```

### Output
Upon successful creation of the employee, the API will respond with a JSON object containing the details of
the newly created employee, including:
- `id`: The unique identifier of the employee.
- `created_at`: The date and time when the employee record was created.
- `updated_at`: The date and time when the employee record was last updated.
- `name`: The name of the employee.
- `email`: The email address of the employee.
- `department`: The department to which the employee belongs.
- `role`: The role or designation of the employee.
- `date_joined`: The date when the employee joined.

Example response body:
```JSON
{
    "id": 420,
    "created_at": "2024-11-04T06:44:42.717331Z",
    "updated_at": "2024-11-04T06:44:42.717331Z",
    "name": "Joe Dalton",
    "email": "joe@dalton.com",
    "department": "SALES",
    "role": "ANALYST",
    "date_joined": "2024-11-04T06:44:42.717331Z"
}
```


The response of this request can be documented as a JSON schema:
```JSON
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "created_at": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "department": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "date_joined": {
      "type": "string"
    }
  }
}
```
A successful POST request will typically return a status code of `201 (Created)`.


## GET Employee Details
This endpoint is used to retrieve the details of a specific employee.

### Request
- Method: GET
- URL: `{{base_url}}/api/employees/:id/`

### Response
The response will be in JSON format and will have the following schema:

```JSON
{
  "id": "number",
  "created_at": "string",
  "updated_at": "string",
  "name": "string",
  "email": "string",
  "department": "string",
  "role": "string",
  "date_joined": "string"
}
```
A successful response will have a `200 OK` status.


## Update Employee Data
This endpoint is used to overwrite the information of an employee identified by the given `id`.
The request should include the updated data in the request body.

### Request
- Method: PUT
- URL: `{{base_url}}/api/employees/:id/`

### Request Body
The request body should be in raw format and include the following parameters:
- `name`: (string) The updated name of the employee.
- `email`: (string) The updated email address of the employee.
- `department`: (string) Optional. Permissible values `HR`, `ENGINEERING`, `SALES`
- `role`: (string) Optional. Permissible values `DEVELOPER`, `MANAGER`, `ANALYST`

### Response
The response will be in JSON format and will have the following schema:
```JSON
{
  "id": "number",
  "created_at": "string",
  "updated_at": "string",
  "name": "string",
  "email": "string",
  "department": "string",
  "role": "string",
  "date_joined": "string"
}
```
A successful response will have a status code of `200 OK` and a Content-Type of `application/json`.
The response body will contain the updated information of the employee, including their id, created_at, updated_at,
name, email, department, role, and date_joined.


## Partial Update Employee
This endpoint is used to partially update the details of an employee (one or more attributes).

### Request
- Method: PATCH
- URL: `{{base_url}}/api/employees/:id/`

### Request Body
The request body should be a JSON payload with the updated attribute(s) information and
may include any combination of the following parameters:
- `name`: (string) The updated name of the employee.
- `email`: (string) The updated email address of the employee.
- `department`: (string) Permissible values `HR`, `ENGINEERING`, `SALES`
- `role`: (string) Permissible values `DEVELOPER`, `MANAGER`, `ANALYST`

### Response
The response of the request is a JSON object with the following schema:
```JSON
{
  "id": "number",
  "created_at": "string",
  "updated_at": "string",
  "name": "string",
  "email": "string",
  "department": "string",
  "role": "string",
  "date_joined": "string"
}
```

## Delete Employee
This DELETE request is used to delete data that was previously created via a POST request.
You can identify the specific employee to be deleted by including the employee's `id` in the URL
(e.g. `/api/employees/123/`).
> **Note:** It's a **SOFT Delete** to allow data restore in the future or audit purpose.

### Request Body
This request does not require a request body.

### Response Body
The response for this request does not include a body.

### Response
- Status: 204
- Content-Type: text/xml

> A successful DELETE request typically returns a `200 OK`, `202 Accepted`, or `204 No Content` response code.

