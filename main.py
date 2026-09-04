

# Задача 1

def order_courses(courses: list, durations: list) -> str:
    durations_dict = {}

    for idx, course in enumerate(courses):
        key = durations[idx]

        if key not in durations_dict:
            durations_dict[key] = []

        durations_dict[key].append(course)

    durations_dict = dict(sorted(durations_dict.items()))

    result = []

    for duration, cour in durations_dict.items():
        if len(cour) == 1:
            result.append(f'{cour[0]}, {duration} месяцев')
        else:
            for course in cour:
                result.append(f'{course}, {duration} месяцев')

    return '\n'.join(result)


# Задача 2

def check_corr(courses_list: list) -> tuple:
    duration_index = []
    mcount_index = []

    for idx, course in enumerate(courses_list):
        duration_index.append([course['duration'], idx])
        mcount_index.append([len(course['mentors']), idx])

    duration_index.sort()
    mcount_index.sort()

    indexes_d = []
    indexes_m = []

    for duration_i in duration_index:
        indexes_d.append(duration_i[1])

    for indexes in mcount_index:
        indexes_m.append(indexes[1])

    has_corr = indexes_d == indexes_m

    return has_corr, indexes_d, indexes_m


# Задача 3

def same_name(courses_list: list) -> list:
    mentors_names = []

    for course in courses_list:
        course_names = []

        for mentor in course['mentors']:
            name = mentor.split()[0]
            course_names.append(name)

        mentors_names.append(course_names)

    result = []

    for names, course in zip(mentors_names, courses_list):
        unique_names = set(names)
        same_name_list = []

        for unique in unique_names:
            if names.count(unique) > 1:

                for mentor in course['mentors']:
                    if mentor.split()[0] == unique:
                        same_name_list.append(mentor)

        result.append(sorted(same_name_list))

    return result