import os
import django



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alarm_in_Ukraine.settings')
    django.setup()
    from alarms.tasks import set_states_to_db
    set_states_to_db()

if __name__ == '__main__':
    main()
