"""

Tests for general public plugin.

"""

import ckan.tests.factories as factories
import ckan.plugins.toolkit as toolkit

from ckanext.generalpublic import helper as h

import pytest

@pytest.mark.ckan_config('ckan.plugins','generalpublic')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
def test_public_access_to_resource(app):
    '''
        Test if a user that isnt logged in 
        cannot access a resource
    '''

    # Create a resource that will be used for testing
    admin = factories.User()
    owner_org = factories.Organization(admin=[{
        'name': admin['id'],
        'capacity': 'admin'
    }])
    dataset = factories.Dataset(owner_org=owner_org['id'])
    resource = factories.Resource(package_id=dataset['id'])

    # Try and access the resource
    url = toolkit.url_for('{}_resource.read'.format(dataset['type']),
                  id=dataset['name'], resource_id=resource['id'])
    res = app.get(url)

    assert res.status_code == 404

@pytest.mark.ckan_config('ckan.plugins','generalpublic')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
def test_user_access_to_resource(app):
    '''
        Test if a user that is logged in 
        can access a resource
    '''
    # Create the test user
    user = factories.User()

    # Create a resource that will be used for testing
    admin = factories.User()
    owner_org = factories.Organization(admin=[{
        'name': admin['id'],
        'capacity': 'admin'
    }])
    dataset = factories.Dataset(owner_org=owner_org['id'])
    resource = factories.Resource(package_id=dataset['id'])

    # Try and access the resource
    url = toolkit.url_for('{}_resource.read'.format(dataset['type']),
                  id=dataset['name'], resource_id=resource['id'])
    env = {"Authorization": user["apikey"]}
    res = app.get(url, environ_overrides=env)

    assert res.status_code == 200

@pytest.mark.ckan_config('ckan.plugins','generalpublic')
@pytest.mark.usefixtures('clean_db', 'with_plugins', 'with_request_context')
def test_logged_in_helper():
    '''
        Test is_logged_in helper
    '''

    # Test with no user logged in
    with pytest.raises(AttributeError) as e:
            h.is_logged_in()
    assert e.type == AttributeError

    # Test with a user logged in
    user = factories.User()
    toolkit.c.userobj = user
    assert h.is_logged_in()