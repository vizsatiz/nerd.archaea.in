import unittest
from dal.applications_adapter import ApplicationAdapter


class ApplicationAdapterTest(unittest.TestCase):

    def application_adapter_test(self):
        application_id = ApplicationAdapter.create(account_guid='dmcmol',
                                                   application_name='app_name',
                                                   application_guid='some_guid',
                                                   application_key='wdmcmdkl',
                                                   application_secret='endednjkl',
                                                   application_algorithm='Salesforce',
                                                   user_id=2,
                                                   app_metadata='{djndckno}'
                                                   )
        ApplicationAdapter.update({
            'application_id': application_id
        }, {
            'application_name': 'updated_app_name'
        })

        updated_app = ApplicationAdapter.read({
            'application_id': application_id
        })

        self.assertEqual(updated_app[0].application_name, 'updated_app_name')

        ApplicationAdapter.delete({
            'application_id': application_id
        })

        deleted_app = ApplicationAdapter.read({
            'application_id': application_id
        })

        self.assertEqual(len(deleted_app), 0)

