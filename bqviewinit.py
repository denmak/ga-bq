from oauth2client.appengine import AppAssertionCredentials
import httplib2
from apiclient import discovery
import logging
import bqparams

class BQView():


    f = open('session_vw.sql','r')
    sessions_vw = "".join(f.readlines()[1:])
    f.close()

    def __init__(self):
        credentials = AppAssertionCredentials(
            'https://www.googleapis.com/auth/bigquery'
        )
        self.http = credentials.authorize(httplib2.Http())
        self.bigquery = discovery.build('bigquery', 'v2', http=self.http)
        # TODO add response check

    # client = bigquery.Client()
    # project = 'my-project'
    # source_dataset_id = 'my_source_dataset'
    # source_table_id = 'us_states'
    # shared_dataset_ref = client.dataset('my_shared_dataset')

    def create_session_vw(self):
        table_ref = {'tableId': bqparams.view_id,
                     'datasetId': bqparams.dataset_id,
                     'projectId': bqparams.project_id}

        sql_template = self.sessions_vw
        view_query = sql_template.format(bqparams.project_id, bqparams.dataset_id, bqparams.table_id)

        view = {'tableReference': table_ref, 'view': {'query': view_query}}

        view = self.bigquery.tables().update(
            body=view, datasetId=bqparams.dataset_id, projectId=bqparams.project_id
            , tableId=bqparams.view_id).execute()
        logging.info(view)

    def init_view(self):
         self.create_session_vw()