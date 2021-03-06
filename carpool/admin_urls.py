from django.urls import path
from django.contrib.auth import views as auth_views
from carpool.admin_views import Admin_View, Owner_View, Owner_Approve, Owner_Details, ApproveView, RejectView, \
    Passenger_View, Passenger_Approve, Passenger_Details, Feed_Back, Notification, Feed_Back_To, Payment_by_Passenger, \
    Payment_action_owner, Published_Now, Pub_rate, Completed_Rides

urlpatterns = [
    path('',Admin_View.as_view()),
    path('ownerview',Owner_View.as_view()),
    path('ow_approve', Owner_Approve.as_view()),
    path('ow_details', Owner_Details.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('passengerview', Passenger_View.as_view()),
    path('pas_aprove', Passenger_Approve.as_view()),
    path('pas_details', Passenger_Details.as_view()),
    path('feedback', Feed_Back.as_view()),
    path('feedbackto', Feed_Back_To.as_view()),
    path('notification', Notification.as_view()),
    path('paymentbypassenger', Payment_by_Passenger.as_view()),
    path('paymentaction', Payment_action_owner.as_view()),
    path('pub_ride', Published_Now.as_view()),
    path('pub_rate', Pub_rate.as_view()),
    path('comp_ride', Completed_Rides.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ),
         name='logout'
         ),
]

def urls():
    return urlpatterns,'admin','admin'