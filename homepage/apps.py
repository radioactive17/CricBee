from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'homepage'

    def ready(self):
        from . import views
        views.news_scheduler()
        views.int_fixture_scheduler()
        views.dom_fixture_scheduler()
        views.wom_fixture_scheduler()
