from oauth2client.appengine import AppAssertionCredentials
import httplib2
from apiclient import discovery
import logging
import schemas_bq_tables
import bqparams
class BQLoader():
    project_id = bqparams.project_id
    dataset_id = bqparams.dataset_id
    table_id =   bqparams.table_id

    table_schema =  schemas_bq_tables.main_table_schema
    def __init__(self):
        credentials = AppAssertionCredentials(
            'https://www.googleapis.com/auth/bigquery'
        )
        self.http = credentials.authorize(httplib2.Http())
        self.bigquery = discovery.build('bigquery', 'v2', http=self.http)
    def insert_rows(self,rows,stop_recursion = False):

        body = {"rows":rows}

        response = self.bigquery.tabledata().insertAll(
            projectId=self.project_id,
            datasetId=self.dataset_id,
            tableId=self.table_id,
            body=body).execute()

        # TODO add response check

    def create_table(self):
        table_ref = {'tableId': self.table_id,
                     'datasetId': self.dataset_id,
                     'projectId': self.project_id}
        table = {'tableReference': table_ref, 'schema': {'fields':self.table_schema},
                 'timePartitioning': {'type': 'DAY'}}

        table = self.bigquery.tables().insert(
            body=table, datasetId=self.dataset_id, projectId=self.project_id).execute()
        logging.info(table)
