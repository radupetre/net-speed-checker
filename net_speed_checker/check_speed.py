import datetime
import glob
import logging
import os
import pickle
import speedtest
import sys

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Check(declarative_base()):
    __tablename__ = 'check'
    id = Column(Integer, primary_key=True)
    client_ip = Column(String)
    client_lat = Column(Float)
    client_lon = Column(Float)
    client_isp = Column(String)
    client_cc = Column(String)
    server_url = Column(String)
    server_lat = Column(Float)
    server_lon = Column(Float)
    server_cc = Column(String)
    server_city = Column(String)
    server_ping = Column(Float)
    upload = Column(Float)
    download = Column(Float)
    timestamp = Column(DateTime)
    success = Column(Boolean)
    message = Column(String)


def take_measurement():
    speed_test = speedtest.Speedtest()
    best_server = speed_test.get_best_server()

    download = speed_test.download()
    upload = speed_test.upload()
    config = speed_test.get_config()

    check = Check(
        client_ip=config['client']['ip'],
        client_lat=config['client']['lat'],
        client_lon=config['client']['lon'],
        client_isp=config['client']['isp'],
        client_cc=config['client']['country'],
        server_url=best_server['host'],
        server_lat=best_server['lat'],
        server_lon=best_server['lon'],
        server_cc=best_server['cc'],
        server_city=best_server['name'],
        server_ping=best_server['latency'],
        upload=upload / 1000000.0,
        download=download / 1000000.0,
        timestamp=datetime.datetime.now(),
        success=True,
        message='Pass.')

    file = "{}.pickle".format(check.timestamp.strftime("%Y_%d_%m-%H_%M_%S-%f"))
    pickle.dump(check, open(file, "wb"))
    logging.info("Measurement {} SAVED\n".format(file))


reusable_session = None


def get_session():
    global reusable_session
    if reusable_session is None:
        session = sessionmaker()
        db = sys.argv[1]
        user = sys.argv[2]
        database = sys.argv[3]
        host = sys.argv[4]
        password = sys.argv[5]
        engine = create_engine(
            '{}://{}:{}@{}/{}'.format(db, user, password, host, database))
        session.configure(bind=engine)
        reusable_session = session()
    return reusable_session


def persist_measurement(check, file):
    session = get_session()
    session.add(check)
    session.commit()
    logging.info("Measurement {} PERSISTED id {}".format(file, check.id))
    

def record_measurements():
    for file in glob.glob("*.pickle"):
        logging.info("Measurement {} RECORDED".format(file))
        check = pickle.load(open(file, "rb"))
        persist_measurement(check, file)
        os.remove(file)
        logging.info("Measurement {} CLEARED\n".format(file))


def exception_handler(exc_type, exc_value, traceback):
    logging.error("Uncaught Exception",
                  exc_info=(exc_type, exc_value, traceback))
    logging.info("STOPPED {}\n\n".format(datetime.datetime.now()))


def main():
    sys.excepthook = exception_handler
    logging.basicConfig(filename='check_speed.log', level=logging.DEBUG)
    logging.info("STARTED {}\n".format(datetime.datetime.now()))
    take_measurement()
    record_measurements()
    logging.info("STOPPED {}\n\n".format(datetime.datetime.now()))


if __name__ == '__main__':
    main()
