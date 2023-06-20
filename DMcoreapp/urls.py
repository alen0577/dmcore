from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('registration_form', views.registration_form, name='registration_form'),

    path('reset_password', views.reset_password, name='reset_password'),
    path('internshipform', views.internshipform, name='internshipform'),
    path('internship_save', views.internship_save, name='internship_save'), 
    path('get_warns', views.get_warns, name='get_warns'),
    path('get_requ', views.get_requ, name='get_requ'), 
    path('logout', views.logout, name='logout'),
    
    #---------------------------------------------------------------------------Admin Section
    path('ad_base', views.ad_base, name='ad_base'),
    path('ad_profile', views.ad_profile, name='ad_profile'),
    path('ad_dashboard', views.ad_dashboard, name='ad_dashboard'),
    path('ad_create_work', views.ad_create_work, name='ad_create_work'),
    path('save_create_work', views.save_create_work, name='save_create_work'),
    path('ad_view_work', views.ad_view_work, name='ad_view_work'),
    path('ad_view_clint/<int:id>', views.ad_view_clint, name='ad_view_clint'), 
    path('update_client/<int:id>', views.update_client, name='update_client'),
    path('ad_daily_work_det', views.ad_daily_work_det, name='ad_daily_work_det'),
    path('ad_work_analiz_det', views.ad_work_analiz_det, name='ad_work_analiz_det'),
    path('flt_dt_analiz', views.flt_dt_analiz, name='flt_dt_analiz'),
    path('ad_work_progress', views.ad_work_progress, name='ad_work_progress'),
    path('flt_progress', views.flt_progress, name='flt_progress'),
    path('ad_work_progress_det/<int:id>', views.ad_work_progress_det, name='ad_work_progress_det'),
    path('ad_warning_ex', views.ad_warning_ex, name='ad_warning_ex'),
    path('ad_warning_sugg_dash/<int:id>', views.ad_warning_sugg_dash, name='ad_warning_sugg_dash'),
    path('ad_warning_det/<int:id>', views.ad_warning_det, name='ad_warning_det'),
    path('ad_suggestions_det/<int:id>', views.ad_suggestions_det, name='ad_suggestions_det'),  
    path('change_pass', views.change_pass, name='change_pass'),  
   
    path('ad_imagechange/<int:id>', views.ad_imagechange, name='ad_imagechange'),
    path('ad_accountset', views.ad_accountset, name='ad_accountset'),  
    path('get_dis', views.get_dis, name='get_dis'), 
    path('ad_exe_smopost', views.ad_exe_smopost, name='ad_exe_smopost'),
    path('ad_sv_smopost/<int:id>', views.ad_sv_smopost, name='ad_sv_smopost'), 
    path('ad_get_smo_pst', views.ad_get_smo_pst, name='ad_get_smo_pst'), 
    path('get_event_det', views.get_event_det, name='get_event_det'), 
    path('filter_shedule/<int:id>', views.filter_shedule, name='filter_shedule'),  
    path('ad_export_excel/<int:id>', views.ad_export_excel, name='ad_export_excel'),
    #---------------------------------------------------------------------------Executive Section
    path('ex_base', views.ex_base, name='ex_base'),
    path('ex_profile', views.ex_profile, name='ex_profile'),
    path('ex_dashboard', views.ex_dashboard, name='ex_dashboard'), 
    path('ex_daily_work_clint', views.ex_daily_work_clint, name='ex_daily_work_clint'), 
    path('ex_daily_work_det/<int:id>', views.ex_daily_work_det, name='ex_daily_work_det'),
    path('daily_work_done/<int:id>', views.daily_work_done, name='daily_work_done'),
    path('ex_weekly_rep_clint', views.ex_weekly_rep_clint, name='ex_weekly_rep_clint'),
    path('ex_weekly_rep_clint_det/<int:id>', views.ex_weekly_rep_clint_det, name='ex_weekly_rep_clint_det'),
    path('sv_wk_rp/<int:id>', views.sv_wk_rp, name='sv_wk_rp'),
    path('ex_view_work_clint', views.ex_view_work_clint, name='ex_view_work_clint'),
    path('ex_view_clint_det/<int:id>', views.ex_view_clint_det, name='ex_view_clint_det'),  
    path('ex_warning', views.ex_warning, name='ex_warning'),
    path('add_warning/<int:id>', views.add_warning, name='add_warning'),
    path('add_suggestion/<int:id>', views.add_suggestion, name='add_suggestion'),  

    path('ex_warnings_dash', views.ex_warnings_dash, name='ex_warnings_dash'),
    path('ex_suggestions', views.ex_suggestions, name='ex_suggestions'),
    path('ex_change_pass', views.ex_change_pass, name='ex_change_pass'),
    path('ex_accountset', views.ex_accountset, name='ex_accountset'),
    path('ex_imagechange/<int:id>', views.ex_imagechange, name='ex_imagechange'),
    path('get_sub', views.get_sub, name='get_sub'),
    path('corrections', views.corrections, name='corrections'),
    path('add_corrections/<int:id>', views.add_corrections, name='add_corrections'),
    path('get_corrections', views.get_corrections, name='get_corrections'),
    path('ex_schedule_dash', views.ex_schedule_dash, name='ex_schedule_dash'),
    path('ex_calander', views.ex_calander, name='ex_calander'),
    path('ex_all_events', views.ex_all_events, name='ex_all_events'), 
    path('ex_add_event', views.ex_add_event, name='ex_add_event'), 
    path('ex_update', views.ex_update, name='ex_update'),
    path('ex_remove', views.ex_remove, name='ex_remove'),
    path('ex_shedule_work', views.ex_shedule_work, name='ex_shedule_work'),
    path('ex_edit_post_status/<int:id>', views.ex_edit_post_status, name='ex_edit_post_status'),
    path('ex_save_shedule', views.ex_save_shedule, name='ex_save_shedule'),
    

    #---------------marketing head
    
    path('he_profile', views.he_profile, name='he_profile'),
    path('he_project', views.he_project, name='he_project'),
    path('he_view_works',views.he_view_works,name='he_view_works'),
    path('he_work_asign/<int:pk>',views.he_work_asign,name='he_work_asign'),
    path('he_daily_task',views.he_daily_task,name='he_daily_task'),
    path('he_workprogress_executive',views.he_workprogress_executive,name='he_workprogress_executive'),
    path('he_progress_report/<int:pk>',views.he_progress_report,name='he_progress_report'),
    path('he_feedback',views.he_feedback,name='he_feedback'),
    path('he_feedbacke1/<int:pk>',views.he_feedbacke1,name='he_feedbacke1'),
    path('he_feedback_submit/<int:pk>',views.he_feedback_submit,name='he_feedback_submit'),
    path('he_work_add/<int:id>',views.he_work_add,name='he_work_add'),
    path('he_change_pass',views.he_change_pass,name='he_change_pass'),
    path('he_accountset',views.he_accountset,name='he_accountset'),
    path('he_imagechange/<int:id>',views.he_imagechange,name='he_imagechange'),
    path('he_flt_progress',views.he_flt_progress,name='he_flt_progress'),
    path('he_view_work_asign_client',views.he_view_work_asign_client,name='he_view_work_asign_client'),
    path('he_view_work_asign_exe/<int:id>',views.he_view_work_asign_exe,name='he_view_work_asign_exe'),
    path('he_view_post/<int:id>',views.he_view_post,name='he_view_post'),
    path('he_add_correction/<int:id>',views.he_add_correction,name='he_add_correction'),
    path('he_add_status/<int:id>',views.he_add_status,name='he_add_status'),
    path('he_smo_exe',views.he_smo_exe,name='he_smo_exe'),
    path('he_add_event_status/<int:id>',views.he_add_event_status,name='he_add_event_status'),
    path('he_add_correction_daily/<int:id>',views.he_add_correction_daily,name='he_add_correction_daily'),
    path('he_cor_exe',views.he_cor_exe,name='he_cor_exe'),
    path('he_cor_exe_det/<int:id>',views.he_cor_exe_det,name='he_cor_exe_det'),
    

    #--------------------------------------------------------------Smo Submission
    
    path('smo_login/<int:id>',views.smo_login,name='smo_login'),
    path('smo_dash',views.smo_dash,name='smo_dash'),
    path('smo_signup/<int:id>',views.smo_signup,name='smo_signup'),
    path('smo_reg/<int:id>',views.smo_reg,name='smo_reg'),
    path('smo_signin/<int:id>',views.smo_signin,name='smo_signin'),
    path('smo_cnt_chnl',views.smo_cnt_chnl,name='smo_cnt_chnl'),
    path('create_post',views.create_post,name='create_post'),
    path('published_post',views.published_post,name='published_post'),
    path('save_post_drft',views.save_post_drft,name='save_post_drft'),
    path('content',views.content,name='content'),
    path('edit_post_drft/<int:id>',views.edit_post_drft,name='edit_post_drft'),    
    path('logout_smo',views.logout_smo,name='logout_smo'),
    path('smo_change_pass',views.smo_change_pass,name='smo_change_pass'),
    path('sm_calendar',views.sm_calendar,name='sm_calendar'),
    path('all_events', views.all_events, name='all_events'), 
    path('add_event', views.add_event, name='add_event'), 
    path('update', views.update, name='update'),
    path('remove', views.remove, name='remove'),
    path('work_shedule_exe', views.work_shedule_exe, name='work_shedule_exe'),
    path('work_shedule/<int:id>', views.work_shedule, name='work_shedule'),


    # ---------------------------------------------------------------------------- data manager section

    path('dm_profile', views.dm_profile, name='dm_profile'),
    path('dm_dashboard', views.dm_dashboard, name='dm_dashboard'),

    
    path('dm_assigned_persons/',views.assigned_persons, name='assigned_persons'),
    path('dm_assigned_person_details/',views.assigned_person_details, name='assigned_person_details'),







    # ---------------------------------------------------------------------------- telecaller  section

    path('tc_profile', views.tc_profile, name='tc_profile'),
    path('tc_dashboard', views.tc_dashboard, name='tc_dashboard'),
    path('tc_view_leads', views.tc_view_leads, name='tc_view_leads'),
    path('tc_view_current_leads', views.tc_view_current_leads, name='tc_view_current_leads'),
    path('tc_view_previous_leads', views.tc_view_previous_leads, name='tc_view_previous_leads'),
    # path('update_status', views.update_status, name='update_status'),
    path('tc_accountset', views.tc_accountset, name='tc_accountset'),


    path('tc_followup/',views.tc_followup,name='tc_followup'),
    path('tc_closed/',views.tc_closed,name='tc_closed'),
    path('tc_flt_day_closed/',views.tc_flt_day_closed,name='tc_flt_day_closed'),
    path('tc_flt_month_closed/',views.tc_flt_month_closed,name='tc_flt_month_closed'),




 
]