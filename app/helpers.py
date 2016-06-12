import jwt, json

from flask import current_app
from flask_restful import abort

from .models import User, BucketListItem, db


def get_current_user_id(token):
    '''Returns current user_id based on the token supplied
    '''
    try:
        secret_key = current_app.config.get('SECRET_KEY')
        decoded = jwt.decode(token, secret_key)
        return User.query.filter_by(username=decoded['username']).first().id
    except:
        abort(401, message='Cannot authenticate user. Invalid Token')

def get_bucketlist(bucketlist):
    '''Returns the result of getting a single bucketlist
    '''
    return {'id': bucketlist.id,
            'name': bucketlist.name,
            'items': get_all_bucketlist_item(bucketlist.id),
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified,
            'created_by': bucketlist.created_by}

def get_single_bucketlist_item(bucketlist_item):
    '''Returns the result of getting a single bucketlist item
    '''
    return {'id': bucketlist_item.id,
            'name': bucketlist_item.name,
            'date_created': bucketlist_item.date_created,
            'date_modified': bucketlist_item.date_modified,
            'done': bucketlist_item.done}

def get_all_bucketlist_item(bucketlist_id):
    '''Returns the result of getting all bucketlist items
    '''
    all_bucketlist_item = BucketListItem.query.filter_by(
        bucketlist_id=bucketlist_id).all()
    bucketlist_item_output = [get_single_bucketlist_item(bucketlist_item) \
        for bucketlist_item in all_bucketlist_item]
    return bucketlist_item_output

def update_database():
    '''
    Updates and commit updated changes to the database
    Returns True if done successfully and False if otherwise
    '''
    try:
        db.session.commit()
        return True
    except:
        return False

def delete_model(model):
    '''
    Delete the given model from the database
    Returns True if done successfully and False if otherwise
    '''
    try:
        db.session.delete(model)
        db.session.commit()
        return True
    except:
        return False

def save_model(model):
    '''
    Add a new model to the database
    Returns True if done successfully and False if otherwise
    '''
    try:
        db.session.add(model)
        db.session.commit()
        return True
    except:
        return False

def save_resource_msg(data):
    msg = {'message': 'Saved'}
    msg.update(data)
    return msg

messages = {'username_not_found': {'message': 'username does not exist'},
            'password_incorrect': {'message': 'Password incorrect'},
            'authentication_failed': {'message': 'Authentication Failed. Please try again'},
            'bucketlist_updated': {'message': 'Bucketlist updated'},
            'bucketlist_not_updated': {'message': 'Bucketlist not updated'},
            'bucketlist_not_exist': {'message': 'Bucketlist does not exist'},
            'bucketlist_exist': {'message': 'Bucketlist already exist'},
            'no_bucketlist': {'message': 'Cannot locate any bucketlist'},
            'user_pass_blank': {'message': 'Username or Password cannot be blank'},
            'registered': {'message': 'You have been registered. Please login'},
            'not_registered': {'message': 'Unable to register user. Please try again'},
            'user_exist': {'message': 'Username already exists'},
            'bucketlist_not_saved':{'message' 'Unable to save bucketlist. Please try again'},
             'no_bucketlist_name':{'message': 'Please supply bucketlist name'},
             'bucketlist_not_deleted': {'message': 'Unable to delete the bucketlist'},
              'bucketlist_deleted': {'message': 'Bucketlist deleted'},
              'bucketlist_updated': {'message': 'Bucketlist updated'},
            'bucketlist_item_not_updated': {'message': 'Bucketlist item not updated'},
            'bucketlist_item_not_exist': {'message': 'Bucketlist item does not exist'},
            'bucketlist_item_exist': {'message': 'Bucketlist item already exist'},
            'no_bucketlist_item': {'message': 'Cannot locate any bucketlist items'},
            'bucketlist_item_not_saved':{'message' 'Unable to save bucketlist item. Please try again'},
             'no_bucketlist_item_name':{'message': 'Please supply name for your bucketlist item'},
             'bucketlist_item_not_deleted': {'message': 'Unable to delete bucketlist item'},
              'bucketlist_item_deleted': {'message': 'Bucketlist item deleted'},
              'bucketlist_item_updated': {'message': 'Bucketlist item updated'},
              'resource_not_found': 'Error: Cannot locate requested item or resource'}
