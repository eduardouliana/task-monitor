from datetime import date, timedelta
import locale

from models.date_configuration import DateConfiguration


class DateHelper:
    @staticmethod
    def get_date(configuration: DateConfiguration):
        if not configuration.date_on_title:
            return ""

        locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        return (date.today() + timedelta(days=configuration.days_offset)).strftime(
            configuration.date_format
        )
