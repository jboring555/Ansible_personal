#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from dellemc_unity_sdk import runner
from dellemc_unity_sdk import supportive_functions
from dellemc_unity_sdk import constants
from dellemc_unity_sdk import validator

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['unstable'],
                    'supported_by': 'community'}
parameters_all = {
    'create': {
        'required': {'storageResource', 'name', 'path'},
        'optional': {'description', 'isReadOnly', 'defaultAccess', 'minSecurity', 'noAccessHosts',
                     'readOnlyHosts', 'readWriteHosts', 'rootAccessHosts'}
    },
    'modify': {
        'required': {'storageResource', 'nfsShare'},
        'optional': {'snap', 'path', 'description', 'isReadOnly', 'defaultAccess', 'minSecurity',
                     'noAccessHosts', 'readOnlyHosts', 'readWriteHosts', 'rootAccessHosts'},
    },
    'delete': {
        'required': {'storageResource', 'nfsShare'}
    }
}


def create(params, unity):
    storageId = params.get('storageResource').get('id')
    name = params.get('name')
    path = params.get('path')
    # if not validator.check_parameters(params, parameters_all.get('create')):
    # supportive_functions.raise_exception_about_parameters(parameters_all.get('create'))
    request_params = {'name': name, 'path': path}
    optional_params = dict()
    for parameter in parameters_all.get('create').get('optional'):
        if params.get(parameter):
            optional_params.update({parameter: params.get(parameter)})
    if optional_params:
        request_params.update({'nfsShareParameters': optional_params})

    request_params_wrapper = {'id': storageId, 'nfsShareCreate': [request_params]}
    unity.update('modifyFilesystem', 'storageResource', request_params_wrapper)
    return unity.query('nfsShare', {'fields': 'id'})


def modify(params, unity):
    storageId = params.get('storageResource').get('id')
    nfsShareId = params.get('nfsShare').get('id')
    # if not validator.check_parameters(params, parameters_all.get('modify')):
    # supportive_functions.raise_exception_about_results(parameters_all.get('modify'))
    request_params = {'nfsShare': {'id': nfsShareId}}
    optional_params = dict()
    for parameter in parameters_all.get('modify').get('optional'):
        if params.get(parameter):
            optional_params.update({parameter: params.get(parameter)})
    if optional_params:
        request_params.update({'nfsShareParameters': optional_params})

    request_params_wrapper = {'id': storageId, 'nfsShareModify': [request_params]}
    return unity.update('modifyFilesystem', 'storageResource', request_params_wrapper)


def delete(params, unity):
    storageId = params.get('storageResource').get('id')
    nfsShareId = params.get('nfsShare').get('id')
    request_params = [{'nfsShare': {'id': nfsShareId}}]
    request_params_wrapper = {'id': storageId, 'nfsShareDelete': request_params}
    return unity.update('modifyFilesystem', 'storageResource', request_params_wrapper)


template = {
    constants.REST_OBJECT: 'storageResource',
    constants.ACTIONS: {
        'create':
            {constants.EXECUTED_BY: create},
        'modify':
            {constants.EXECUTED_BY: modify},
        'delete':
            {constants.EXECUTED_BY: delete}
    }
}

"""TODO: create nfsShare through a snapshot
template = {
    constants.REST_OBJECT_KEY: 'nfsShare',
    constants.ACTIONS_KEY: {
        'create': 
        {constants.ACTION_TYPE_KEY:constants.ActionType.UPDATE, 
            constants.PARAMETER_TYPES_KEY:parameters_all.get('create')}
    }
}
"""


def main():
    arguments = supportive_functions.create_arguments_for_ansible_module(template)

    ansible_module = AnsibleModule(arguments, supports_check_mode=True)
    runner.run(ansible_module, template)


if __name__ == '__main__':
    main()
