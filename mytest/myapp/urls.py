
from django.urls import path,re_path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^employee/saveimage',views.saveImage),
    re_path(r'',views.test_page),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)