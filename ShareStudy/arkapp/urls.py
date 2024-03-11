
from django.urls import path,include
from arkapp import views
from . import views
from .views import stu_sidecourse
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import send_notification,view_notifications,admin_notifications
from .views import upload_course_notes, download_course_notes,view_course_notes


urlpatterns = [
    
    path("signup/",views.signup,name="signup"),
    path("signupteacher/",views.signupteacher,name="signupteacher"),
    path("",views.index,name="index"),
    path("login",views.login,name="login"),
    path("adminreg",views.adminreg,name="adminreg"),
    path("loginhome",views.loginhome,name='loginhome'),
    path("teacherhome/",views.teacherhome,name='teacherhome'),
    path("edit_profile",views.edit_profile,name='edit_profile'),
    path("edit_profilete/",views.edit_profilete,name='edit_profilete'),
    path("handlelogout",views.handlelogout,name="handlelogout"),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),   
    path('custom_admin_page/', views.custom_admin_page, name='custom_admin_page'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path("adminnew",views.adminnew,name='adminnew'),
    path("userview",views.userview,name='userview'),
    path("teacherview",views.teacherview,name='teacherview'),
    path("add_course",views.add_course,name='add_course'),
    path("exammarkset",views.exammarkset,name='exammarkset'),
    path("view_course",views.view_course,name='view_course'),
    path("examdetails",views.examdetails,name='examdetails'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_thankyou/', views.feedback_thankyou, name='feedback_thankyou'), 
    path("adminfeedback",views.adminfeedback,name='adminfeedback'),
    path('exammarkset/', views.exammarkset, name='exammarkset'),
    path('assignment_list', views.assignment_list, name='assignment_list'),
    path('<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('update/<int:assignment_id>/', views.update_assignment, name='update_assignment'),
    path('delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('assignstu_list', views.assignstu_list, name='assignstu_list'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('view_student_names/<int:assignment_id>/', views.view_student_names, name='view_student_names'),
    path('list_submissions/', views.list_submissions, name='list_submissions'),

    # URL for teachers to download assignments (accessible to teachers)
    path('download_assignment/<int:submission_id>/', views.download_assignment, name='download_assignment'),
    path('course/<int:course_id>/', stu_sidecourse, name='stu_sidecourse'),
    path('send_notification', send_notification, name='send_notification'),
    path('view_notifications/', view_notifications, name='view_notifications'),
    path('admin_notifications', admin_notifications, name='admin_notifications'),
    path('upload_course_notes', upload_course_notes, name='upload_course_notes'),
    path('view_course_notes/', view_course_notes, name='view_course_notes'),  # Add this line
    path('download/<int:notes_id>/', download_course_notes, name='download_course_notes'),

    path('prepare_exam/', views.prepare_exams, name='prepare_exam'),
    path('questions/<int:pk>/', views.questions, name='questions'),
    path('add_product', views.add_product, name='add_product'),
    path('adminview_product', views.adminview_product, name='adminview_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('view_product', views.view_product, name='view_product'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('productssss/<int:product_id>/', views.product_detailssss, name='product_detailssss'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_page/', views.cart_page, name='cart_page'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('orders/', views.orders, name='orders'),
    path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('payment/<int:product_id>/', views.payment, name='payment'),
    path('payment/<int:product_id>/success', views.success, name='success'),
    path('chat/', views.messages_page, name='messages_page'),
]


