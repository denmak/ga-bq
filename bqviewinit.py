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
        view_ref = self.bigquery.shared_dataset_ref.table("sessions_vw")
        view = self.bigquery.Table(view_ref)
        sql_template = self.sessions_vw
        view.view_query = sql_template.format(bqparams.project_id, bqparams.dataset_id, bqparams.table_id)
        try:
            view = self.bigquery.update_table(view, ["view_query"])
            logging.info('update session_vw')
        except:
            view = self.bigquery.create_table(view)  # API request
            logging.info('create session_vw')
        logging.info(view)

    def init_view(self):
         self.create_session_vw()