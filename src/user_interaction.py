from src.api_sites import HeadHunterAPI, SuperJobAPI
from src.saver import JsonSaver


def user_interaction():
    """Функция для взаимодействия с пользователем."""

    site_dict = {'1': 'HeadHunter', '2': 'SuperJob', '3': 'HeadHunter_и_SuperJob'}
    print('Добро пожаловать!')
    site = input("Выберите платформу для поиска вакансий:\n"
                 "- Если выбираете HeadHunter, то в ответ введите: 1\n"
                 "- Если выбираете SuperJob, то в ответ введите: 2\n"
                 "- Если хотите посмотреть и на HeadHunter и на SuperJob, в ответ введите: 3\n")
    if site == '1' or site == '2' or site == '3':
        city = input("Введите город в котором хотите найти подходящую вакансию (например: Москва):\n")
        keyword = input("Введите профессию для поиска подходящих вакансий:\n")

        if site == '1':
            hh_api = HeadHunterAPI(keyword, city)
            list_vacancies = hh_api.get_vacancies()
        elif site == '2':
            super_job_api = SuperJobAPI(keyword, city)
            list_vacancies = super_job_api.get_vacancies()
        else:
            hh_api = HeadHunterAPI(keyword, city)
            super_job_api = SuperJobAPI(keyword, city)
            list_vacancies = hh_api.get_vacancies() + super_job_api.get_vacancies()

        if not list_vacancies:
            print(f"Вакансий в г. {city} по профессии {keyword} на {site_dict[site]} не найдено :(")
        else:
            json_saver = JsonSaver(site_dict[site])
            json_saver.add_vacancies_to_file(list_vacancies)
            print(f"Список вакансий на {site_dict[site]} в г. {city} по профессии {keyword}:\n")
            for vacancy in list_vacancies:
                print(vacancy)
            vacancy_sort = input("Хотите получить список полученных вакансий, отсортированных по зарплате?\n"
                                 "- Если хотите, то в ответ введите: Да\n"
                                 "- Если не хотите, то в ответ введите: Нет\n")
            if vacancy_sort.lower() == "да":
                for vacancy in json_saver.get_vacancies_from_file_sorted_by_salary():
                    print(vacancy)

            vacancy_salary = input("Хотите выбрать из списка, вакансии с определенной зарплатой?\n"
                                   "- Если хотите, то в ответ введите: Да\n"
                                   "- Если не хотите, то в ответ введите: Нет\n")
            if vacancy_salary.lower() == "да":
                salary_min = int(input("Введите минимальную зарплату:\n"))
                salary_max = int(input("Введите максимальную зарплату:\n"))
                vacancies = json_saver.get_vacancies_from_file_by_salary(salary_min, salary_max)
                if vacancies is None:
                    print(f"В списке нет вакансий с зарплатой от {salary_min} до {salary_max} руб.")
                else:
                    for vacancy in vacancies:
                        print(vacancy)

    else:
        print("Платформы с таким номером не существует")
