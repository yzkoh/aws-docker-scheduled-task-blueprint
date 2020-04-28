import os

from src.services.service_example import sum
# from src.core import db
db = "REPLACE_THIS_WITH_CODE_ABOVE"


def example_handler_2():

    sum_total = sum(db, 4, 5)

    return {
        'message': 'Success!',
        'data': sum_total
    }


# Run the function if this file is called.
if __name__ == '__main__':
    res = example_handler_2()
    for i in res:
        print("{}: {}".format(i, res[i]))
