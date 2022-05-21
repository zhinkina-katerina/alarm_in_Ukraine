from .models import States, Alarm
from django.views.generic import TemplateView
from django.db.models import Sum, When, Case
from datetime import timedelta, datetime
import pytz


class Statistic(TemplateView):
    template_name = 'statistic.html'  # noqa

    def get_db_objects(self):
        self.alarms = Alarm.objects.all().filter(alert=True)

    def get_context_data(self, **kwargs):

        context = super(Statistic, self).get_context_data(**kwargs)
        self.get_db_objects()

        states = States.objects.all()
        states_by_alerts = {}

        for state in states.values():
            state_name = state.get('state')
            states_by_alerts[state_name] = self.get_sum_of_alarms(state)

        sorted_dict = self.sort_dictionary(states_by_alerts)
        context['labels'] = list(sorted_dict.keys())
        context['data'] = list(sorted_dict.values())

        return context

    def sort_dictionary(self, dictionary):
        sorted_keys = sorted(dictionary, key=dictionary.get)
        sorted_dict = {}
        for i in sorted_keys:
            sorted_dict[i] = dictionary[i]
        return sorted_dict

    def get_sum_of_alarms(self, state):
        sum_alarms = self.alarms.filter(state_id=state.get('id')).aggregate(Sum(Case(
            When(alarms_alarm=True, then=1),
            When(alarms_alarm=None, then=0),
        ), 'alert')).get('alert__sum')

        return sum_alarms

    def get(self, request, *args, **kwargs):
        self.request = request
        return TemplateView.get(self, request, *args, **kwargs)


class StatisticWeek(Statistic):

    def get_db_objects(self):
        tz = pytz.timezone('Europe/Kiev')
        today = datetime.now(tz)
        week_ago = today - timedelta(days=8)
        self.alarms = Alarm.objects.all().filter(alert=True, date__range=[week_ago, today])


class StatisticDay(Statistic):

    def get_db_objects(self):
        tz = pytz.timezone('Europe/Kiev')
        today = datetime.now(tz)
        yesterday = today - timedelta(days=1)
        self.alarms = Alarm.objects.all().filter(alert=True, date__range=[yesterday, today])


def page_not_found(request, exception):
    return render(request, '404.html', status=404)  # noqa
