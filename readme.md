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

## Usage
The app can be used with Postman or from the command line using the curl command

### Functionality, Endpoints and Accessiblity
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
<td>Get all items in this bucket list</td>
<td>GET /bucketlists/{id}/items </td>
<td>False</td>
</tr>

<tr>
<td>Create new item in this bucket list</td>
<td>POST /bucketlists/{id}/items </td>
<td>False</td>
</tr>

<tr>
<td>Get this bucket list item</td>
<td>GET /bucketlists/{id}/items/{item_id} </td>
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
