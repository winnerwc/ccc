from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
# 获取或创建表
engine = create_engine('mysql+pymysql://root:123456@localhost/testdb', echo=True)
def get_or_create_table(project_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if project_name in metadata.tables:
        return metadata.tables[project_name]
    else:
        # 如果表不存在，则创建表
        project_table = Table(
            project_name,
            metadata,
            Column('id', Integer, primary_key=True),
            Column('project_name', String(100), nullable=False),
            Column('job_name', String(100)),
            Column('job_num', Integer),
            Column('job_status', String(50)),
            Column('fail_reason', String(255)),
            Column('owner', String(100)),
            Column('time', DateTime)
        )
        metadata.create_all(engine)
        return project_table