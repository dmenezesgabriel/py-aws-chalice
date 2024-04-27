import logging

from chalice import Chalice, Rate

app = Chalice(app_name="py-aws-chalice")
app.log.setLevel(logging.DEBUG)


@app.route("/")
def index():
    return {"hello": "world"}


@app.route("/hello")
def hello():
    return {"message": "hello"}


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduler(event):
    app.log.info("Schedule triggered")


@app.lambda_function()
def boto3_import(event, context):
    import boto3

    return {"boto3": boto3.__file__}


@app.lambda_function()
def duckdb_import(event, context):
    import duckdb

    return {"duckdb": duckdb.sql("SELECT 42").fetchall()}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
