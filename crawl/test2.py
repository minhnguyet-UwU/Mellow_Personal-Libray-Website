from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")

def get_descendants(person_code, graph):
    descendants = set()
    stack = [person_code]
    while stack:
        current_person = stack.pop()
        descendants.add(current_person)
        stack.extend(child for child in graph.get(current_person, []))
    return descendants

def build_graph(database):
    graph = {}
    for code, birth_date, father, mother, alive, region in database:
        if father != '0000000':
            graph.setdefault(father, []).append(code)
        if mother != '0000000':
            graph.setdefault(mother, []).append(code)
    return graph

def number_people(database):
    return len(database)

def number_people_born_at(database, date):
    birth_date = parse_date(date)
    return sum(1 for code, b_date, father, mother, alive, region in database if parse_date(b_date) == birth_date)

def most_alive_ancestor(database, person_code):
    def count_ancestors(person_code, graph, alive_ancestors):
        parents = graph.get(person_code, [])
        if not parents:
            return alive_ancestors
        return max(count_ancestors(parent, graph, alive_ancestors + 1) for parent in parents)

    return count_ancestors(person_code, build_graph(database), 0)

def number_people_born_between(database, from_date, to_date):
    start_date = parse_date(from_date)
    end_date = parse_date(to_date)
    return sum(1 for code, b_date, father, mother, alive, region in database if start_date <= parse_date(b_date) <= end_date)

def max_unrelated_people(database):
    graph = build_graph(database)

    def is_unrelated(person, subset):
        return all(person not in get_descendants(member, graph) for member in subset)

    max_subset_size = 0
    people_without_parents = [person[0] for person in database if person[2] == '0000000' and person[3] == '0000000']

    for person in people_without_parents:
        current_subset = [person] + [member for member in people_without_parents if member != person]
        current_size = 1
        for member in people_without_parents:
            if member != person and is_unrelated(member, current_subset):
                current_size += 1
                current_subset.append(member)

        if current_size > max_subset_size:
            max_subset_size = current_size

    return max_subset_size

database = []

# Read database
while True:
    line = input().strip()
    if line == "*":
        break
    person_data = line.split()
    database.append(person_data)

# Execute queries
while True:
    query_line = input().strip()
    if query_line == "***":
        break
    command, *args = query_line.split()
    if command == "NUMBER_PEOPLE":
        result = number_people(database)
    elif command == "NUMBER_PEOPLE_BORN_AT":
        result = number_people_born_at(database, args[0])
    elif command == "MOST_ALIVE_ANCESTOR":
        result = most_alive_ancestor(database, args[0])
    elif command == "NUMBER_PEOPLE_BORN_BETWEEN":
        result = number_people_born_between(database, args[0], args[1])
    elif command == "MAX_UNRELATED_PEOPLE":
        result = max_unrelated_people(database)
    print(result)
