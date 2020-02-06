from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from operator import itemgetter, attrgetter

site = admin.site

def applist(request):
	app_dict = {}
	user = request.user
	for model, model_admin in site._registry.items():
		app_label = model._meta.app_label
		has_module_perms = user.has_module_perms(app_label)
		
		if has_module_perms:
			perms = model_admin.get_model_perms(request)
			
			if True in perms.values():
				model_dict = {
					'name': capfirst(model._meta.verbose_name_plural),
					'admin_url': mark_safe('/tenant/%s/%s/' % (app_label, model.__name__.lower())),
					'perms': perms,
				}
				if app_label in app_dict:
					app_dict[app_label]['models'].append(model_dict)
				else:
					app_dict[app_label] = {
						'name': app_label.title(),
						'app_url': app_label + '/',
						'has_module_perms': has_module_perms,
						'models': [model_dict],
					}
					
	my_app_list = app_dict.items()
	# my_app_list = list(app_dict)
	# print(my_app_list)
	# my_app_list = sorted(my_app_list, lambda x, y: x['name'], y['name'])
	my_app_list = sorted(my_app_list, key = lambda x: x[0])
	# print(my_app_list)
	# print(list(app_dict))
	return {'my_app_list': my_app_list}