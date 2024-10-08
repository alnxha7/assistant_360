from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('userreg', views.userreg,name="userreg"),
    path('staffreg', views.staffreg,name="staffreg"),
    path('admin', views.admin,name="admin"),
    path('adminhome', views.adminhome,name="adminhome"),
    path('staffhome', views.staffhome,name="staffhome"),
    path('userhome', views.userhome,name="userhome"),
    path('taxihome',views.taxihome,name="taxihome"),
    path('hotelhome',views.hotelhome,name="hotelhome"),
    path("Logout",views.Logout,name='Logout'),
    path("stafflogin",views.stafflogin,name="stafflogin"),
    path("getDistrict/",views.getDistrict,name="getDistrict"),
   
    path("Add_state/",views.Add_state,name="Add_state"),
    path("list_state/",views.list_state,name="list_state"),
    path("delete_state/",views.delete_state,name="delete_state"),
    path("edit_state/",views.edit_state,name="edit_state"),
   
    path("privacy/",views.privacy,name="privacy"),
    path("user_feed/",views.user_feed,name="user_feed"),
    path("staff_complaints/",views.staff_complaints,name="staff_complaints"),
    path("feedback/",views.feedback,name="feedback"),
    path("Feedback/",views.feedback,name="Feedback"),
    path("complaints/",views.complaints,name="complaints"),
path("find_labour/",views.find_labour,name="find_labour"),
path("book_labour/",views.book_labour,name="book_labour"),
path("staff_ongoing/",views.staff_ongoing,name="staff_ongoing"),
path("staff_rejected/",views.staff_rejected,name="staff_rejected"),
path("staff_completed/",views.staff_completed,name="staff_completed"),
path("request_payment/",views.request_payment,name="request_payment"),
path("waiting_payment/",views.waiting_payment,name="waiting_payment"),
path("payment_request",views.payment_request,name="payment_request"),
path("payment_completed/",views.payment_completed,name="payment_completed"),
path("payment_history/",views.payment_history,name="payment_history"),
path("reject_user/",views.reject_user,name="reject_user"),
path("ongoing/",views.ongoing,name="ongoing"),
path("approved_user/",views.approved_user,name="approved_user"),
path("reject_staff/",views.reject_staff,name="reject_staff"),
path("approved_staff/",views.approved_staff,name="approved_staff"),

path("schedule/",views.schedule,name="schedule"),
path("complete/",views.complete,name="complete"),
path("rejected/",views.rejected,name="rejected"),
path("delete_labour/",views.delete_labour,name="delete_labour"),
path("job_confirm/",views.job_confirm,name="job_confirm"),
path("confirm_labour/",views.confirm_labour,name="confirm_labour"),
path("reject_labour/",views.reject_labour,name="reject_labour"),


path("add_district/",views.add_district,name="add_district"),
    path("list_district/",views.list_district,name="list_district"),
    path("edit_district/",views.edit_district,name="edit_district"),
    path("delete_district/",views.delete_district,name="delete_district"),
    path("list_user/",views.list_user,name="list_user"),
    path("approve_user/",views.approve_user,name="approve-user"),
    path("delete_user/",views.delete_user,name="delete_user"),
    path("list_staff/",views.list_staff,name="list_staff"),
    path("approve_staff/",views.approve_staff,name="approve_staff"),
    path("delete_staff/",views.delete_staff,name="delete_staff"),
     path("approve_user/",views.approve_user,name="approve_user"),
     path("newjob",views.newjob,name="newjob"),
     path("newjob_approve",views.newjob_approve,name="newjob_approve"),
     path("task_complete/",views.task_complete,name="task_complete"),
     


     path("app_login",views.app_login,name="app_login"),
path("app_register",views.app_register,name="app_register"),
path("app_editPassword",views.app_editPassword,name="app_editPassword"),
path("app_getstate",views.app_getstate,name="app_getstate"),
path("app_getdist",views.app_getdist,name="app_getdist"),
path("app_getloc",views.app_getloc,name="app_getloc"),
path("app_getstaff",views.app_getstaff,name="app_getstaff"),
path("app_Booking",views.app_Booking,name="app_Booking"),
path("app_myBooking",views.app_myBooking,name="app_myBooking"),
path("app_pay",views.app_pay,name="app_pay"),
path("app_regComplaint",views.app_regComplaint,name="app_regComplaint"),
path("app_getComplaint",views.app_getComplaint,name="app_getComplaint"),
path("app_profile",views.app_profile,name="app_profile"),
path("newtaxi",views.newtaxi,name="newtaxi"),
path('taxiRegister',views.taxiRegister,name="taxiRegister"),
path('taxibook',views.taxibook,name="taxibook"),
path('taxibookDelete',views.taxibookDelete,name="taxibookDelete"),
path('approve_taxi',views.approve_taxi,name="approve_taxi"),
path('approved_taxi',views.approved_taxi,name="approved_taxi"),
path('taxi_approvelist',views.taxi_approvelist,name="taxi_approvelist"),
path('texibookingreject',views.texibookingreject,name="texibookingreject"),
path('approve_taxibook',views.approve_taxibook,name="approve_taxibook"),
path('approved_taxibook',views.approved_taxibook,name="approved_taxibook"),
path('edit_amt',views.edit_amt,name="edit_amt"),
path('edit_km',views.edit_km,name="edit_km"),
path('taxi_confirm',views.taxi_confirm,name="taxi_confirm"),


path('newtaxistf',views.newtaxistf,name="newtaxistf"),
path('approve_taxistf',views.approve_taxistf,name="approve_taxistf"),
path('approved_taxistf',views.approved_taxistf,name="approved_taxistf"),
path('reject_staff',views.reject_staff,name="reject_staff"),

path("payment_taxicompleted",views.payment_taxicompleted,name="payment_taxicompleted"),
path("request_taxipayment",views.request_taxipayment,name="request_taxipayment"),
path("waiting_taxipayment",views.waiting_taxipayment,name="waiting_taxipayment"),
path("payment_taxirequest",views.payment_taxirequest,name="payment_taxirequest"),
path("payment_taxihistory",views.payment_taxihistory,name="payment_taxihistory"),
path('taxi_rejected',views.taxi_rejected,name="taxi_rejected"),



path('Manage_Menutype',views.Manage_Menutype,name="Manage_Menutype"),
path('Manage_Menu',views.Manage_Menu,name="Manage_Menu"),
path('delete_type',views.delete_type,name="delete_type"),
path('delete_menu',views.delete_menu,name="delete_menu"),
path('getmenu',views.getmenu,name="getmenu"),
path('getdt',views.getdt,name="getdt"),
path('Manage_Stock',views.Manage_Stock,name="Manage_Stock"),
path('delete_stock',views.delete_stock,name="delete_stock"),
path('getlist',views.getlist,name="getlist"),
path('myorder2',views.myorder2,name="myorder2"),


path('newhotel',views.newhotel,name="newhotel"),
path('approve_hotel',views.approve_hotel,name="approve_hotel"),
path('approved_hotel',views.approved_hotel,name="approved_hotel"),
path('reject_hotel',views.reject_hotel,name="reject_hotel"),

path('success',views.success,name="success"),
path("labour_complaint/",views.labour_complaint, name="labour_complaint"),
path('delete_complaint/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),
path('edit_booking/', views.edit_booking, name='edit_booking'),
path('staff_complaints/', views.staff_complaints, name='staff_complaints'),
path('remove_blacklist/<int:staff_id>/', views.remove_blacklist, name='remove_blacklist'),
path('make_blacklist/<int:staff_id>/', views.make_blacklist, name='make_blacklist'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
