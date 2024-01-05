from datetime import datetime

def total_number_orders(submissions):
    return len(submissions)

def total_revenue(submissions):
    return sum(int(i.get('Price', 0)) for i in submissions)

def revenue_of_shop(submissions, shop_id):
    return sum(int(submission['Price']) for submission in submissions if submission['ShopID'] == shop_id)

def total_consume_of_customer_shop(submissions, customer_id, shop_id):
    return sum(int(submission['Price']) for submission in submissions if submission['ShopID'] == shop_id and submission['CustomerID'] == customer_id)

def total_revenue_in_period(submissions, from_time_point, to_time_point):
    from_time_point = datetime.strptime(from_time_point, "%H:%M:%S")
    to_time_point = datetime.strptime(to_time_point, "%H:%M:%S")
    return sum(int(submission['Price']) for submission in submissions if from_time_point <= submission['TimePoint'] <= to_time_point)

keyList = ["CustomerID", "ProductID", "Price", "ShopID", "TimePoint"]
submissions = []

# Read submissions
while True:
    submission_line = input().strip()
    if submission_line == "#":
        break
    submission = {key: None for key in keyList}
    time_format = "%H:%M:%S"
    try:
        submission['CustomerID'], submission['ProductID'], submission['Price'], submission['ShopID'], submission['TimePoint'] = submission_line.split()
        submission['TimePoint'] = datetime.strptime(submission['TimePoint'], time_format)
        submissions.append(submission)
    except ValueError:
        continue

# Execute queries
while True:
    query_line = input().strip()
    if query_line == "#":
        break
    command, *args = query_line.split()
    if command == "?total_number_orders":
        result = total_number_orders(submissions)
    elif command == "?total_revenue":
        result = total_revenue(submissions)
    elif command == "?revenue_of_shop":
        result = revenue_of_shop(submissions, args[0])
    elif command == "?total_consume_of_customer_shop":
        result = total_consume_of_customer_shop(submissions, *args)
    elif command == "?total_revenue_in_period":
        result = total_revenue_in_period(submissions, *args)
    print(result)
