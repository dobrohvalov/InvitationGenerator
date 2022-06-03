from main import eventsAdd, guestsAdd

"""
Guests
invitationsList
"""
from datetime import datetime

# guest = [['Андрей', 'Петров', 'Производство', 'Маркетинг'],
#          ['Андрей', 'Петров', 'Продажы', 'Автоматизация']]
# events = [['04.06.2022', 'Выстовка_роботов', 'Автоматизация'],
#           ['05.06.2022', 'День_продаж', 'Продажы']]
guestIn = ['Андрей', 'Петров', 'Продажы', 'Автоматизация']
event = ['05.06.2022', 'День_продаж', 'Продажы']
print(eventsAdd(event))
# print(main.guestsAdd(guestIn))
