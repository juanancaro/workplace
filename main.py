import psycopg2
import yaml
import sql_queries as sql

def connect_database(params, autocommit=True):
    conn = psycopg2.connect(f'dbname={params["dbname"]} \
                            user={params["user"]} \
                            password={params["password"]} \
                            host={params["host"]} \
                            port={params["port"]}')
    conn.autocommit = autocommit
    cursor = conn.cursor()
    return cursor

def execute_command(cursor,command):
    cursor.execute(command)
    





if __name__ == '__main__':
    with open('conf/database_config.yaml') as f:
        params = yaml.safe_load(f)
    cursor = connect_database(params)
    execute_command(cursor,sql.create_database)

    

