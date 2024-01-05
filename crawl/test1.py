from datetime import datetime

def total_number_submissions(submissions):
    return len(submissions)

def number_error_submissions(submissions):
    count = 0
    for i in submissions:
        if i.get('Status') == 'ERR':
            count += 1
    return count

def number_error_submissions_of_user(submissions, user_id):
    count = 0
    for i in submissions:
        if i.get('UserID') == user_id and i.get('Status') == 'ERR':
            count += 1
    return count

def total_point_of_user(submissions, user_id):
    point = 0
    problem = {}
    for i in submissions:
        if i.get('UserID') == user_id:
            problem_id = i.get('ProblemID')
            if problem_id in problem.keys():
                if int(i['Point']) > problem[problem_id]:
                    problem[problem_id] = int(i['Point'])
            else:
                problem[problem_id] = int(i['Point'])
    for i in list(problem.values()):
        point += int(i)
    return point

def number_submission_period(submissions, from_time_point, to_time_point):
    from_time_point = datetime.strptime(from_time_point, "%H:%M:%S")
    to_time_point = datetime.strptime(to_time_point, "%H:%M:%S")
    count = 0
    for i in submissions:
        if from_time_point <= i.get('TimePoint') <= to_time_point:
            count += 1
    return count

keyList = ["UserID",
            "ProblemID",
            "TimePoint",
            "Status",
            "Point"]
submissions = []

# Read submissions
while True:
    submission_line = input().strip()
    if submission_line == "#":
        break
    submission = {key: None for key in keyList}
    time_format = "%H:%M:%S"
    submission['UserID'], submission['ProblemID'], submission['TimePoint'], submission['Status'], submission['Point'] = submission_line.split()
    submission['TimePoint'] = datetime.strptime(submission['TimePoint'], time_format)
    submissions.append(submission)

# Execute queries
while True:
    query_line = input().strip()
    if query_line == "#":
        break
    command, *args = query_line.split()
    if command == "?total_number_submissions":
        result = total_number_submissions(submissions)
    elif command == "?number_error_submision":
        result = number_error_submissions(submissions)
    elif command == "?number_error_submision_of_user":
        result = number_error_submissions_of_user(submissions, args[0])
    elif command == "?total_point_of_user":
        result = total_point_of_user(submissions, args[0])
    elif command == "?number_submission_period":
        result = number_submission_period(submissions, *args)
    print(result)
