
data_source_path = '/usr/local/airflow/dags/gcs_bq/data/supermarket_sales.csv'
gcs_bucket_name = 'gcs_bucket_255'
gcs_file_name = 'supermarket_sales.csv'

project_id = 'de-engr'

schema_fields = [
    {"name": "Invoice ID", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Branch", "type": "STRING", "mode": "NULLABLE"},
    {"name": "City", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Customer type", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Gender", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Product line", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Unit price", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Quantity", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Tax 5%", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Total", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Date", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Month Name", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Year", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Time", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Payment", "type": "STRING", "mode": "NULLABLE"},
    {"name": "cogs", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Rating", "type": "STRING", "mode": "NULLABLE"},
    ]