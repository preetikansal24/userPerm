import json

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from userApp.models import User, UserGroup, Resource, ResourcePermission, ResourceGroupPermissions


@api_view(['POST', 'GET'])
def create_user(request):
    if request.method == 'POST' :
        post_data = json.loads(request.body)
        if post_data is not None:
            username = post_data.get("username")
            if not User.objects.filter(user_name=username):
                user = User(name=post_data.get("name"), user_name=username, phone_no=post_data.get("phone"))
                user.save()
                return HttpResponse(user, status=200)
            else:
                return HttpResponse("user already exists", status=400)
        else:
            return HttpResponse("Wrong data", status=500)
    if request.method == 'GET':
        users = User.objects.filter(active=True).values_list(flat=True)
        return HttpResponse(users, status=200)


@api_view(['POST'])
def assign_user_group(request):
    post_data = json.loads(request.body)
    if post_data is not None:
        user = post_data.get("username")
        if user is None:
            raise ValidationError("Please provide user")
        group = post_data.get("group_id")
        if group is None:
            raise ValidationError("Please provide group")

        userObj = User.objects.filter(user_name=user).first()

        if userObj:
            user_grp = UserGroup(user=userObj, group_id=group)
            user_grp.save()
            return HttpResponse(user_grp, status=200)
        else:
            return HttpResponse("No such user present", status=400)
    else:
        return HttpResponse("Wrong data", status=500)


@api_view(['POST'])
def assign_resource_permission(request):
    post_data = json.loads(request.body)
    if post_data is not None:
        resource_id = post_data.get("resource_id")
        if resource_id is None:
            raise ValidationError("Please provide resource id")
        action_type = post_data.get("action_type")
        if action_type is None:
            raise ValidationError("Please provide specific action type")

        res_perm = ResourcePermission(resource_id=resource_id, action_type_id=action_type)
        res_perm.save()
        return HttpResponse(res_perm, status=200)
    else:
        return HttpResponse("Wrong data", status=500)


@api_view(['POST'])
def assign_resource_group(request):
    post_data = json.loads(request.body)
    if post_data is not None:
        resource_perm_id = post_data.get("resource")
        if resource_perm_id is None:
            raise ValidationError("Please provide resource with action type id")
        group = post_data.get("group")
        if group is None:
            raise ValidationError("Please provide group")
        resource_grp = ResourceGroupPermissions(resource_perm_id=resource_perm_id, group_id=group)
        resource_grp.save()
        return HttpResponse("Successfully added", status=200)
    else:
        return HttpResponse("Wrong data", status=500)


@api_view(['GET'])
def has_access(request):
    query_params = request.GET
    user_id = query_params.get('user_id')
    action_type = query_params.get('action_type')
    resource_id = query_params.get('resource_id')
    if resource_id is None or action_type is None or user_id is None:
        raise ValidationError("Please provide correct data")

    groups = ResourceGroupPermissions.objects.filter(resource_perm__action_type__id=action_type,
                                                     resource_perm__resource_id=resource_id).values('group')
    group_ids = [each.get('group') for each in groups]
    user_grp = UserGroup.objects.filter(user__id=user_id, group_id__in=group_ids).count()
    print user_grp
    if user_grp > 0:
        return HttpResponse("Has access", status=200)
    else:
        return HttpResponse("No access", status=200)

