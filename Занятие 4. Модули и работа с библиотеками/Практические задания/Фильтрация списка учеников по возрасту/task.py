# TODO Напишите функцию calculate_average_age
def calculate_average_age(lists):
    allage = [i["age"] for i in lists]
    itog = sum(allage)
    sred = len(allage)
    return itog/sred


# TODO Напишите функцию filter_students_by_age
def filter_students_by_age(lists, age):
    final = [i for i in lists if i["age"]<age]
    return final


if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    # TODO Вычислите средний возраст учеников
    print("Средний возраст учеников:", calculate_average_age(students_list))
    filter = filter_students_by_age(students_list, calculate_average_age(students_list))
    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filter:
        print(current_student['name'])
