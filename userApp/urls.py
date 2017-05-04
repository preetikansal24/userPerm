from django.conf.urls import url
import views as user_view

urlpatterns = [
    url(r'^user/?$', user_view.create_user),
    url(r'^user-group/?$', user_view.assign_user_group),
    url(r'^resource-perm/?$', user_view.assign_resource_permission),
    url(r'^resource-group/?$', user_view.assign_resource_group),
    url(r'^get-access/?$', user_view.has_access),
]
