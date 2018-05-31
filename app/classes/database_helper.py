from sqlalchemy.orm import sessionmaker
#from pricing.utils.scoped_session import ScopedSession
#from pricing.utils.scalar_query import ScalarQuery


class DatabaseHelper(object):
    def __init__(self, engine=None):
        self.init(engine)

    def init(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

#    def scoped_session(self):
#        return ScopedSession(self.Session)

    def create_all(self, Base):
        Base.metadata.create_all(self.engine)

    def drop_all(self, Base):
        Base.metadata.drop_all(self.engine)
