import pytest

from main import order_courses, check_corr, same_name


@pytest.mark.parametrize(
    'courses, durations, expected',
    [
        (
            [
                "Java-разработчик с нуля",
                "Fullstack-разработчик на Python",
                "Python-разработчик с нуля",
                "Frontend-разработчик с нуля"
            ],
            [14, 20, 12, 20],
            (
                "Python-разработчик с нуля, 12 месяцев\n"
                "Java-разработчик с нуля, 14 месяцев\n"
                "Fullstack-разработчик на Python, 20 месяцев\n"
                "Frontend-разработчик с нуля, 20 месяцев"
            )
        ),
        (
            ["Python", "Java"],
            [10, 5],
            "Java, 5 месяцев\nPython, 10 месяцев"
        ),
        (
            ["Python", "Java", "C++"],
            [12, 12, 6],
            "C++, 6 месяцев\nPython, 12 месяцев\nJava, 12 месяцев"
        )
    ]
)
def test_order_courses(courses, durations, expected):
    result = order_courses(courses, durations)
    assert result == expected


@pytest.mark.parametrize(
    'courses_list, expected',
    [
        (
            [
                {"title": "Java", "mentors": ["A", "B", "C"], "duration": 14},
                {"title": "Python", "mentors": ["A"], "duration": 12},
                {"title": "Frontend", "mentors": ["A", "B"], "duration": 20},
            ],
            (False, [1, 0, 2], [1, 2, 0])
        ),
        (
            [
                {"title": "Java", "mentors": ["A", "B", "C"], "duration": 30},
                {"title": "Python", "mentors": ["A"], "duration": 10},
                {"title": "Frontend", "mentors": ["A", "B"], "duration": 20},
            ],
            (True, [1, 2, 0], [1, 2, 0])
        ),
    ]
)
def test_check_corr(courses_list, expected):
    result = check_corr(courses_list)
    assert result == expected


@pytest.mark.parametrize(
    'courses_list, expected',
    [
        (
            [
                {
                    "title": "Python",
                    "mentors": [
                        "Александр Иванов",
                        "Александр Петров",
                        "Иван Сидоров"
                    ]
                }
            ],
            [["Александр Иванов", "Александр Петров"]]
        ),
        (
            [
                {
                    "title": "Java",
                    "mentors": [
                        "Иван Иванов",
                        "Петр Петров",
                        "Сергей Сергеев"
                    ]
                }
            ],
            [[]]
        ),
        (
            [
                {
                    "title": "Frontend",
                    "mentors": [
                        "Анна Иванова",
                        "Анна Петрова",
                        "Мария Сидорова",
                        "Мария Козлова"
                    ]
                }
            ],
            [[
                "Анна Иванова",
                "Анна Петрова",
                "Мария Козлова",
                "Мария Сидорова"
            ]]
        )
    ]
)
def test_same_name(courses_list, expected):
    result = same_name(courses_list)
    assert result == expected