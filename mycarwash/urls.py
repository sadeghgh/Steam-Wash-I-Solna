from .views import (
    GetCarModel,
    GetSelectionServices,
    PostDetailUser,
    PutSatisfactionUser,
    GetRequestUser,
    DeleteRequestUser,
    DeleteReasonUser,
    CreateCode,
    GetUserCode,
    GetDeleteReasonUser,
    PutRequestUserForAdmin,
    GetSatisfactionUser,
    PutCode,
    GetRequestUserForUser,
    GetUserCodeForAdmin
)

from django.urls import path


urlpatterns = [
    path('car_model/', GetCarModel.as_view()),
    path('select_services/', GetSelectionServices.as_view()),
    path('request_user/', PostDetailUser.as_view()),
    path('putSatisfaction_user/', PutSatisfactionUser.as_view()),
    path('get_my_request/', GetRequestUser.as_view()),
    path('get_my_request_user/', GetRequestUserForUser.as_view()),
    path('post_delete/<int:pk>/', DeleteRequestUser.as_view()),
    path('post_reason_delete/', DeleteReasonUser.as_view()),
    path('create_code/', CreateCode.as_view()),
    path('put_code/<int:pk>/', PutCode.as_view()),
    path('get_code/', GetUserCode.as_view()),
    path('get_code_for_admin/', GetUserCodeForAdmin.as_view()),
    path('get_post_delete/', GetDeleteReasonUser.as_view()),
    path('put_request_for_admin/<int:pk>/', PutRequestUserForAdmin.as_view()),
    path('getSatisfaction/', GetSatisfactionUser.as_view()),
]
