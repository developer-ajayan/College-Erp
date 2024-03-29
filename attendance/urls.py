from front_page.views import FrontpageView
from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('front-page',FrontpageView.as_view(),name="front_page"),
    # path('',views.role_based_redirect_View,name="role_based_login"),

    path('login',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True),name='login'),
    path('userlogin', views.login_user, name="login-user"),
    path('user-register', views.registerUser, name="register-user"),
    path('logout',views.logoutuser,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('update-avatar',views.update_avatar,name='update-avatar'),
    path('update-password',views.update_password,name='update-password'),
    path('department',views.department,name='department-page'),
    path('manage_department',views.manage_department,name='manage-department-modal'),
    path(r'manage_department/<int:pk>',views.manage_department,name='edit-department-modal'),
    path('save_department',views.save_department,name='save-department'),
    path('delete_department',views.delete_department,name='delete-department'),
    path('course',views.course,name='course-page'),
    path('manage_course',views.manage_course,name='manage-course-modal'),
    path(r'manage_course/<int:pk>',views.manage_course,name='edit-course-modal'),
    path('save_course',views.save_course,name='save-course'),
    path('delete_course',views.delete_course,name='delete-course'),
    path('faculty',views.faculty,name='faculty-page'),
    path('manage_faculty',views.manage_faculty,name='manage-faculty-modal'),
    path(r'view_faculty/<int:pk>',views.view_faculty,name='view-faculty-modal'),
    path(r'manage_faculty/<int:pk>',views.manage_faculty,name='edit-faculty-modal'),
    path('save_faculty',views.save_faculty,name='save-faculty'),
    path('delete_faculty',views.delete_faculty,name='delete-faculty'),
    path('class',views.classPage,name='class-page'),
    path('manage_class',views.manage_class,name='manage-class-modal'),
    path(r'manage_class/<int:pk>',views.manage_class,name='edit-class-modal'),
    path(r'manage_class_student/<int:classPK>',views.manage_class_student,name='class-student-modal'),
    path('save_class_student/',views.save_class_student,name='save-class-student'),
    path(r'view_class/<int:pk>',views.view_class,name='class-page'),
    path('save_class',views.save_class,name='save-class'),
    path('delete_class',views.delete_class,name='delete-class'),
    path('delete_class_student',views.delete_class_student,name='delete-class-student'),
    path('student',views.student,name='student-page'),
    path('manage_student',views.manage_student,name='manage-student-modal'),
    path(r'view_student/<int:pk>',views.view_student,name='view-student-modal'),
    path(r'manage_student/<int:pk>',views.manage_student,name='edit-student-modal'),
    path('save_student',views.save_student,name='save-student'),
    path('delete_student',views.delete_student,name='delete-student'),
    path('attendance_class',views.attendance_class,name='attendance-class'),
    path(r'attendance/<int:classPK>',views.attendance,name='attendance-page'),
    path(r'attendance/<int:classPK>/<str:date>',views.attendance,name='attendance-page-date'),
    path('save_attendance',views.save_attendance,name='save-attendance'),
]
