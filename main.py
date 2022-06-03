

def guestsAdd(guestIn):
    """
    Добавляем посетителя
    :param guestIn:  Имя фамилия сфера деятельности круг интересов
    :return:
    """
    table = guestsRead()
    table.append(guestIn)
    guestsUp(table)
    return True


def guestsUp(guest):
    """
    Обновляем таблицу с посетителями
    :param guest: Имя фамилия сфера деятельности круг интересов
    :return:
    """
    f = open('guests.txt', 'w')
    # f.write(guest)
    for i in guest:
        for n in i:
            f.write(n + ' ')
        f.write('\n')
    f.close()
    return f


def guestsRead():
    """
    :return: [] Таблица посетителей
    """
    l = []
    f = open('guests.txt')
    for line in f:
        row = line.split(' ')
        rowline = []
        for n in row:
            if n != '\n':
                rowline.append(n)
        l.append(rowline)

    f.close()
    return l


def eventsAdd(event):
    """
    Добовляем мероприятие
    Отправляем приглашение по участникам
    :param event: Дата Название сфера
    :return:
    """
    invitations(event)
    table = eventsRead()
    table.append(event)
    eventsUp(table)
    return True


def eventsUp(events):
    """
    Обновляем файл мероприятие
    :param guest: Имя фамилия сфера деятельности круг интересов
    :return:
    """
    f = open('events.txt', 'w')
    for i in events:
        for n in i:
            f.write(n + ' ')
        f.write('\n')
    f.close()
    return f


def eventsRead():
    """
    Получаем таблицу мероприятий
    :return: [] возвращаем таблицу в виде массива
    """
    l = []
    f = open('events.txt')
    for line in f:
        row = line.split(' ')
        rowline = []
        for n in row:
            if n != '\n':
                rowline.append(n)
        l.append(rowline)

    f.close()
    return l


def report(invitation: str):
    """
    Добовляем приглашение в отчет
    :param invitation: приглашение
    :return:
    """
    date = []
    f = open('report.txt')
    for line in f:
        date.append(line)
    date.append(invitation)
    f.close()
    f = open('report.txt', 'w')
    for i in date:
        if i != "\n":
            f.write(i+'\n')
    f.close()


def invitations(event):
    """
    Создаем приглашение и отправляем его в отчет
    :param event: мероприятие
    :return:
    """
    guests = guestsRead()
    for i in guests:
        if event[2] == i[2] or event[2] == i[3]:
            invitation = "Приглашаем "+str(i)+" на "+str(event)
            print(invitation)
            report(invitation)

    return True



