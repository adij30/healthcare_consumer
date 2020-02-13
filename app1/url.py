from django.urls import path
from app1 import view_address as va
from app1 import view_hospital as vh
from app1 import view_doctor as vd
from app1 import view_patient as vp

urlpatterns = [
    path('welcome/', va.welcome_clc),

    path('address/', va.welcome_address),
    path('address/save/', va.save_update),
    path('address/edit/<int:id>', va.edit),
    path('address/delete/<int:id>', va.delete),

    path('hospital/', vh.welcome_hospital),
    path('hospital/save/', vh.save_update),
    path('hospital/edit/<int:id>', vh.edit),
    path('hospital/delete/<int:id>', vh.delete),

    path('doctor/', vd.welcome_doctor),
    path('doctor/save/', vd.save_update),
    path('doctor/edit/<int:id>', vd.edit),
    path('doctor/delete/<int:id>', vd.delete),

    path('patient/', vp.welcome_patient),
    path('patient/save/', vp.save_update),
    path('patient/edit/<int:id>', vp.edit),
    path('patient/delete/<int:id>', vp.delete),

]