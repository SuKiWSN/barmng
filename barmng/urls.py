from django.conf.urls import url
from . import profile_page, vertify, home_page, usercost
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles


urlpatterns = [
    url('profile/', profile_page.test),
    url('regist/', profile_page.regist),
    url('vertify/', vertify.mail_code),
    url('login_check/', profile_page.login_check),
    url('manage/', home_page.manage),
    url('user/', home_page.user),
    url('modify/', home_page.modify),
    url('changepwd/', home_page.changepwd),
    url('role/', home_page.role),
    url('getusers/', home_page.getusers),
    url('search_usr/', home_page.search_usr),
    url('addusr/', home_page.add_user),
    url('deleteusr/', home_page.deleteusr),
    url('inmoney/', home_page.inmoney),
    url('getrechargerecord/', home_page.get_Rechargerecord),
    url('user_spend', usercost.user_spend),
    url('consumerecord/', usercost.consume_record),
    url('changepower/', home_page.changerole),
    url('', profile_page.redirect),
]