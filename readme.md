<snippet>
<content>
# Bucketlist API

[![Build Status](https://travis-ci.org/andela-hoyeboade/bucketlist-api.svg?branch=develop)](https://travis-ci.org/andela-hoyeboade/bucketlist-api) [![Coverage Status](https://coveralls.io/repos/github/andela-hoyeboade/bucketlist-api/badge.svg?branch=develop)](https://coveralls.io/github/andela-hoyeboade/bucketlist-api?branch=develop) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/andela-hoyeboade/bucketlist-api/badges/quality-score.png?b=develop)](https://scrutinizer-ci.com/g/andela-hoyeboade/bucketlist-api/?branch=develop) [![Code Climate](https://codeclimate.com/github/andela-hoyeboade/bucketlist-api/badges/gpa.svg)](https://codeclimate.com/github/andela-hoyeboade/bucketlist-api)

## Description
This is a Python Checkpoint2 project for D0B fellows in Andela. It's a flask application designed to manage bucketlists. A bucket list is a list of things that one has not done before but wants to do before dying. Users can register, login and can manage their bucketlists by making requests to the API endpoints.

## Installation
1. Clone the repo
`git clone https://github.com/andela-hoyeboade/buckelist-api.git/` and navigate to the project directory

2. Create and activate a virtual environment

3. Install dependencies
```pip install -r requirements.txt```

4. Run the app
  * Make migrations by running `python manage.py db upgrade` to create necessary tables needed for the app.
  * Run ```python server.py``` to get the app running

## Functionality, Endpoints and Accessiblity
  <table>
  <tr>
  <th> Functionality </th>
  <th> Endpoint</th>
  <th> Public Access</th>
  </tr>
  <tr>
  <td>Logs a user in</td>
  <td>POST /auth/login</td>
  <td>True</td>
  </tr>
  <tr>
   <td>Register a user</td>
   <td>POST /auth/register</td>
   <td> True</td>
  </tr>

  <tr>
  <td>Create a new bucket list</td>
  <td>POST /bucketlists/ </td>
  <td>False</td>
  </tr>

  <tr>
  <td>List all the created bucket lists</td>
  <td>GET /bucketlists/ </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Get single bucket list</td>
  <td>GET /bucketlists/{id} </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Update this bucket list</td>
  <td>PUT /bucketlists/{id} </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Delete this single bucket list</td>
  <td>DELETE /bucketlists/{id} </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Create new item in this bucket list</td>
  <td>POST /bucketlists/{id}/items </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Update a bucketlist item </td>
  <td>PUT /bucketlists/{id}/items/{item_id} </td>
  <td>False</td>
  </tr>

  <tr>
  <td>Delete this item in this bucket list</td>
  <td>DELETE /bucketlists/{id}/items/{item_id} </td>
  <td>False</td>
  </tr>
  </table>

## Usage
The app can be used with Postman or from the command line using the curl command
#### Sample requests and responses
Before making requests, make sure the server is running by running python server.py. Open a new terminal and navigate to the project directory. Then make your requests. See some sample requests below.

1A. Request to register with the username `hassan` and password `hassan`
```
 curl -i -X POST -d "username=hassan&password=hassan" http://127.0.0.1:5000/api/v1/auth/register
```
1B. Response to request in 1A
```
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 87
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 16 Jun 2016 20:40:49 GMT

{
    "date_created": "2016-06-16 20:40:49",
    "id": 1,
    "username": "hassan"
}
```

2A. Request to login with the username `hassan` and password `hassan`
```
curl -i -X POST -d "username=hassan&password=hassan" http://127.0.0.1:5000/api/v1/auth/login
```
2B. Response to request in 2A
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 156
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 16 Jun 2016 20:43:19 GMT

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
}
```

3A. Request to create a new bucketlist
```
curl -i -X POST -d "name=Learn new languages" http://127.0.0.1:5000/api/v1/bucketlists/ -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
3B. Response to request in 3A
```
{HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 181
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 16 Jun 2016 20:52:10 GMT

{
    "created_by": 1,
    "date_created": "2016-06-16 20:52:10",
    "date_modified": "2016-06-16 20:52:10",
    "id": 1,
    "items": [],
    "name": "Learn new languages"
}
```

4A. Request to get all bucketlists
```
curl -X GET http://127.0.0.1:5000/api/v1/bucketlists/ -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
4B. Response to request in 4A
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 338
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Thu, 16 Jun 2016 21:01:42 GMT

{
    "data": [
        {
            "created_by": 1,
            "date_created": "2016-06-16 20:57:20",
            "date_modified": "2016-06-16 20:57:20",
            "id": 1,
            "items": [],
            "name": "Learn new languages"
        }
    ],
    "next_page": null,
    "pages": 1,
    "previous_page": null
}
```

5A. Request to update a bucketlist name
```
curl -i -X PUT -d "name=Learn new foreign languages" http://127.0.0.1:5000/api/v1/bucketlists/1 -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
5B. Response to request in 5A
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 189
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Fri, 17 Jun 2016 08:13:17 GMT

{
    "created_by": 1,
    "date_created": "2016-06-16 20:57:20",
    "date_modified": "2016-06-17 08:13:17",
    "id": 1,
    "items": [],
    "name": "Learn new foreign languages"
}
```

6A. Request to create a bucketlist item
```
curl -i -X POST -d "name=Learn French" http://127.0.0.1:5000/api/v1/bucketlists/1/items -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
6B. Response to request in 6A
```
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 158
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Fri, 17 Jun 2016 08:15:22 GMT

{
    "date_created": "2016-06-17 08:15:22",
    "date_modified": "2016-06-17 08:15:22",
    "done": false,
    "id": 1,
    "name": "Learn French"
}
```

7A. Request to update a bucketlist item
```
curl -i -X PUT -d "name=Learn German" http://127.0.0.1:5000/api/v1/bucketlists/1/items/1 -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
7B. Response to request in 7A
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 154
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Fri, 17 Jun 2016 08:18:25 GMT

{
    "date_created": "2016-06-17 08:15:22",
    "date_modified": "2016-06-17 08:18:25",
    "done": false,
    "id": 1,
    "name": "Learn German"
}
```

8A. Request to delete a bucketlist item
```
curl -i -X DELETE http://127.0.0.1:5000/api/v1/bucketlists/1/items/1 -H "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imhhc3NhbiIsInBhc3N3b3JkIjoiaGFzc2FuIn0.0QLDv1CISkSH65KAFu1rY58UbGsC06mw89ykAFjY2og"
```
8B. Response to request in 8A
```
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Content-Length: 0
Server: Werkzeug/0.10.4 Python/2.7.11
Date: Fri, 17 Jun 2016 08:20:39 GMT
```

## Running tests
1. Navigate to the project direcory
2. Run nosetests --with-coverage to run test and check coverage

##Project Demo
Click <a href='https://youtu.be/-Gcau1z1lUU'>here </a> to view the project demo

## References
http://blog.miguelgrinberg.com/ <br />
https://docs.python.org <br />
http://flask.pocoo.org/ <br />

## Author
Hassan Oyeboade

## License
<a href='https://github.com/andela-hoyeboade/bucketlist-api/blob/develop/LICENSE'>MIT </a>

</content>
</snippet>