#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <cmath>

#define MAX_SUBMISSIONS 1000

struct Submission {
    char UserID[50];
    char ProblemID[50];
    struct tm TimePoint;
    char Status[10];
    char Point[10];
};

int total_number_submissions(struct Submission *submissions, int n) {
    return n;
}

int number_error_submissions(struct Submission *submissions, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(submissions[i].Status, "ERR") == 0) {
            count++;
        }
    }
    return count;
}

int number_error_submissions_of_user(struct Submission *submissions, int n, char *user_id) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (strcmp(submissions[i].UserID, user_id) == 0 && strcmp(submissions[i].Status, "ERR") == 0) {
            count++;
        }
    }
    return count;
}

int total_point_of_user(struct Submission *submissions, int n, char *user_id) {
    int *user_points = (int *)malloc(100 * sizeof(int)); // Assuming a maximum of 100 problems
    memset(user_points, 0, 100 * sizeof(int));

    for (int i = 0; i < n; i++) {
        if (strcmp(submissions[i].UserID, user_id) == 0) {
            int problem_id = atoi(submissions[i].ProblemID);
            user_points[problem_id] = fmax(user_points[problem_id], atoi(submissions[i].Point));
        }
    }

    int total_points = 0;
    for (int i = 0; i < 100; i++) {
        total_points += user_points[i];
    }

    free(user_points);
    return total_points;
}

int number_submission_period(struct Submission *submissions, int n, struct tm from_time, struct tm to_time) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (difftime(mktime(&from_time), mktime(&submissions[i].TimePoint)) <= 0 &&
            difftime(mktime(&submissions[i].TimePoint), mktime(&to_time)) <= 0) {
            count++;
        }
    }
    return count;
}

int main() {
    struct Submission submissions[MAX_SUBMISSIONS];
    int submission_count = 0;

    while (1) {
        char submission_line[100];
        scanf("%s", submission_line);
        if (strcmp(submission_line, "#") == 0) {
            break;
        }

        sscanf(submission_line, "%s %s %d:%d:%d %s %s",
               submissions[submission_count].UserID,
               submissions[submission_count].ProblemID,
               &submissions[submission_count].TimePoint.tm_hour,
               &submissions[submission_count].TimePoint.tm_min,
               &submissions[submission_count].TimePoint.tm_sec,
               submissions[submission_count].Status,
               submissions[submission_count].Point);

        submission_count++;
    }

    while (1) {
        char query_line[100];
        scanf("%s", query_line);
        if (strcmp(query_line, "#") == 0) {
            break;
        }

        char command[100];
        sscanf(query_line, "%s", command);

        if (strcmp(command, "?total_number_submissions") == 0) {
            printf("%d\n", total_number_submissions(submissions, submission_count));
        } else if (strcmp(command, "?number_error_submision") == 0) {
            printf("%d\n", number_error_submissions(submissions, submission_count));
        } else if (strcmp(command, "?number_error_submision_of_user") == 0) {
            char user_id[50];
            sscanf(query_line, "%*s %s", user_id);
            printf("%d\n", number_error_submissions_of_user(submissions, submission_count, user_id));
        } else if (strcmp(command, "?total_point_of_user") == 0) {
            char user_id[50];
            sscanf(query_line, "%*s %s", user_id);
            printf("%d\n", total_point_of_user(submissions, submission_count, user_id));
        } else if (strcmp(command, "?number_submission_period") == 0) {
            struct tm from_time, to_time;
            char from_time_point[20], to_time_point[20];
            sscanf(query_line, "%*s %s %s", from_time_point, to_time_point);
            sscanf(from_time_point, "%d:%d:%d", &from_time.tm_hour, &from_time.tm_min, &from_time.tm_sec);
            sscanf(to_time_point, "%d:%d:%d", &to_time.tm_hour, &to_time.tm_min, &to_time.tm_sec);
            printf("%d\n", number_submission_period(submissions, submission_count, from_time, to_time));
        }
    }

    return 0;
}
