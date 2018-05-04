import json
import boto3
import logging
import time

AWS_ACCESS_KEY_ID = "xxxxxxxxxxxxxx"
AWS_SECRET_ACCESS_KEY = "xxxxxxxxxxxxxxxx"
MAX_RETRIES = 4
TIMEOUT_REMAINING = 1000


def lambda_handler(event, context):
    # TODO implement
    steps_list = [1, 2, 3, 4, 5]
    exec_list = []
    if 'pending_list' not in event.keys():
        print("the First lambda")
        event['pending_list'] = steps_list
        exec_list = event['pending_list']
    else:
        print("Not the First version of lambda")
        print("Event List :")
        print(event['pending_list'])
        exec_list = event['pending_list']
    print("Remaining minutes {}".format(context.get_remaining_time_in_millis()))

    for i in range(0, len(exec_list), 1):
        step = exec_list[i]
        if context.get_remaining_time_in_millis() > TIMEOUT_REMAINING:
            # do whatever retries function you want
            # (make sure the execution time here is lower than the TIMEOUT_REMAINING time)
            hello(step)
        else:
            print("Trying on Second or later lambda")
            # relaunch lambda function if retries left
            retries_left = update_num_retries(event)
            if retries_left > 0:
                event['pending_list'] = exec_list[i:]
                print("Resetting Context to value :")
                print(exec_list[i:])
                relaunch_lambda(event, context)
            else:
                return False


def update_num_retries(event):
    """
    Updates the number of iterations left that the lambda function.
    """
    if not event.get("NUM_RETRIES"):
        event["NUM_RETRIES"] = MAX_RETRIES
    elif event.get("NUM_RETRIES") > 0:
        event["NUM_RETRIES"] = event.get("NUM_RETRIES") - 1

    logging.info("Number of retries left: %d" % event["NUM_RETRIES"])

    return event.get("NUM_RETRIES")


def relaunch_lambda(event, context):
    """
    Creates a new AWS client and execute the same lambda function
    asynchronously
    """
    session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    lambda_cli = session.client("lambda")
    print(json.dumps(event))
    lambda_cli.invoke_async(FunctionName=context.function_name, InvokeArgs=json.dumps(event))


def hello(step):
    print("Hello {}".format(step))
    time.sleep(0.5)
