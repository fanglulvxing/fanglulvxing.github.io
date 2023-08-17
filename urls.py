from django.urls import path
from .views import welcome,thank,search, AirlineDetailView, AddOrderView,SubmitOrderView, CheckBagView, CarbonOffsetView,SurveyView,get_destination_choices


urlpatterns = [
    path('new_order/', AddOrderView.as_view(), name='new_order'),
    path('', welcome, name='welcome'),
    path('thank/', thank, name='thank'),
    path('search/<int:pk>', search, name='search'),
    path('get_destination_choices/', get_destination_choices, name='get_destination_choices'),
    # path('get_starting_choices/', get_starting_choices, name='get_starting_choices'),
    path('arline_detail/<int:aid>/<int:oid>', AirlineDetailView, name='arline_details'),
    path('submit_order/<int:aid>/<int:oid>', SubmitOrderView.as_view(), name = 'submit_order'),
    path('check_bag/<int:aid>/<int:oid>', CheckBagView.as_view(), name = 'check_bag'),
    path('carbon_offset/<int:aid>/<int:oid>', CarbonOffsetView.as_view(), name = 'carbon_offset'),
    path('survey/<int:pk>', SurveyView.as_view(), name = 'survey'),
]
