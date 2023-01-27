import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.generalpublic import helper, middleware

class GeneralpublicPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IMiddleware)

    ######################################################################
    ######################### IConfigurer ################################
    ######################################################################

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic','generalpublic')

    ######################################################################
    ######################### ITEMPLATESHELPER ###########################
    ######################################################################

    def get_helpers(self):
        return {'is_logged_in': helper.is_logged_in,
                "is_public": helper.is_public
                }

    ######################################################################
    ######################### IMiddleware ################################
    ######################################################################

    def make_middleware(self, app, config):
        return middleware.AuthMiddleware(app, config)

    def make_error_log_middleware(self, app, config):
        return middleware.AuthMiddleware(app, config)