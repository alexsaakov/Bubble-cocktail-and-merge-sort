from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def get_journals(self) -> None:
        pass

    @abstractmethod
    def download_text(self) -> None:
        pass

    @abstractmethod
    def users_acess(self) -> None:
        pass


class RealSubject(Subject):

    def get_journals(self) -> None:
        print("Список журналов получен")

    def download_text(self) -> None:
        print("Текст скачен")

    def users_acess(self) -> None:
        print("Только пользователи из внутренней сети могут скачать текст!")
        print("Остальные пользователи могут просматривать список журналов!")



class Proxy(Subject):


    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def get_journals(self) -> None:
        self._real_subject.get_journals()

    def download_text(self) -> None:
        if self.check_access():
            self._real_subject.download_text()
        else:
            print("У вас нет доступа! Узнайте права доступа.")

    def users_acess(self) -> None:
        self._real_subject.users_acess()

    def check_access(self) -> bool:
            return False


def client_code(subject: Subject) -> None:

    print('\nСмотрим журналы\n')
    subject.get_journals()
    print('\nСкачиваем текст\n')
    subject.download_text()
    print('\nИнтерфейс прав доступа\n')
    subject.users_acess()


if __name__ == "__main__":
    print("")
    print("Выполнение кода без использования Прокси(для внутренней сети):\n")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\n")

    print("Выполнение кода с использованием Прокси(для внешней сети):\n")

    proxy = Proxy(real_subject)
    client_code(proxy)