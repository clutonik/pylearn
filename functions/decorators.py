#!python3

# creating our own decorator
# adds additional functionality which can be standard/common for multiple functions
# In this example, I created a decorator called @database, which can be used for all
# methods which interact with database and returns/adds data
# this way, all database queries will be logged


def log_database_queries(func):  # should accept a function as param
    def wrapper_function(*args, **kwargs):
        # adds additional functionality
        print('open log file')
        result = func(*args, **kwargs)  # calls the function passed in as param
        print('close log file')
        return result
    return wrapper_function  # returns the wrapper function

@log_database_queries
def get_user(user_id: int):
    return {
        'username': 'Sahil',
        'id': user_id,
        'age': 30
    }


print(get_user(user_id=1))
