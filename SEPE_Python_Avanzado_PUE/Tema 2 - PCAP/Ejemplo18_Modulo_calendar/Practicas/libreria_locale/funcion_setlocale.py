import calendar
import locale

l = locale.setlocale(locale.LC_ALL, "sv_SE")
c = calendar.LocaleTextCalendar(locale=l)
print(c.formatmonth(2024, 4))

c = calendar.LocaleHTMLCalendar(locale=l)
print(c.formatmonth(2024, 4))
