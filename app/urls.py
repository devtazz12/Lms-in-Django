from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('courses', views.courses, name="courses"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
    path('error-404', views.error_404, name="error_404"),
    path('course-detail/<name>', views.course_detail, name="course_detail"),
    path('videos-course/<int:pk>', views.videos, name="course_videos"),
    path('Billing-details/<int:pk>', views.billinginfo, name="billing_info"),
    path('my-courses', views.mycourses, name="mycourses"),
    path('enroll/<int:pk>', views.enroll, name="enroll"),
    path('login', views.login_page, name="login"),
    path('signup', views.registration_page, name="registration"),
    path('logout', views.logout_user, name="logout"),
    path('change-password/<int:pk>/', views.change_password, name="change_password"),
    path('Reset-Password', views.reset_password, name="reset_password"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
