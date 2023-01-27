[![Tests](https://github.com//ckanext-generalpublic/workflows/Tests/badge.svg?branch=main)](https://github.com//ckanext-generalpublic/actions)

# ckanext-generalpublic

General Public is a plugin for CKAN. This plugin aims to restrict what none logged in user can view. 
This is done using the granular visibility framework plugin. Datasets which have a public visibility
can be seen, downloaded and viewed by any user. Whereas protected datasets allow none logged in users
to see it datasets metadata but not view the data contained.

This plugin is not plug and play and there is not intention of making it so. It has hard coded
items for its current use case. To make it work for your CKAN you will have to edit code.

## Requirements

This plugin requires ckanext-granularvisibility to work.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | no            |
| 2.7             | no            |
| 2.8             | no            |
| 2.9             | yes           |

values:

* "yes" - It works
* "no"  - Currently dont know if it work and no intention of making it work


## Installation

To install ckanext-generalpublic:

0. Make sure to install ckanext-granularvisibility, First.

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com//ckanext-generalpublic.git
    cd ckanext-generalpublic
    pip install -e .
	pip install -r requirements.txt

3. Add `generalpublic` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present



## Developer installation

To install ckanext-generalpublic for development, activate your CKAN virtualenv and
do:

    git clone https://github.com//ckanext-generalpublic.git
    cd ckanext-generalpublic
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-generalpublic

If ckanext-generalpublic should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
