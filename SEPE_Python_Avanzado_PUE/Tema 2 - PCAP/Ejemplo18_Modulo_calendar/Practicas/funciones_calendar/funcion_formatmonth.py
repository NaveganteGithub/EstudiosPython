import calendar

calendario = calendar.TextCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.HTMLCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.LocaleTextCalendar()
print(calendario.formatmonth(2024, 4))
calendario = calendar.LocaleHTMLCalendar()
print(calendario.formatmonth(2024, 4))
