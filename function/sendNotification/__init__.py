import logging
import psycopg2
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from azure.functions import ServiceBusMessage

connection = psycopg2.connect(
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PW'),
            host=os.getenv('POSTGRES_URL'),
            port=os.getenv('POSTGRES_PORT'),
            database=os.getenv('POSTGRES_DB'))
cursor = connection.cursor()

def main(msg: ServiceBusMessage):
    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s', notification_id)
    try:
        logging.info('Try: Python ServiceBus queue trigger processed message: %s', notification_id)
        notification = _get_notification(notification_id)
        attendees = _get_attendees()
        for attendee in attendees:
                _send_email(attendee[1], '{}: {}'.format(attendee[0], notification[0]), notification[1])
        cursor.execute(f'update public."notification" set "completed_date" = now(), "status" = \'Notified {len(attendees)} attendees\' where id = {notification_id}')
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        cursor.close()
        connection.close()

def _get_attendees():
    cursor.execute(f'select "first_name", "email" from public."attendee"')
    return cursor.fetchall()

def _get_notification(id):
    cursor.execute(f'select "subject", "message" from public."notification" where id = {id}')
    return cursor.fetchone()

def _send_email(email, subject, body):
    apiKey = os.getenv('SENDGRID_API_KEY')
    fromEmail = os.getenv('ADMIN_EMAIL_ADDRESS')
    try:
        message = Mail(
        from_email=fromEmail,
        to_emails=email,
        subject=subject,
        plain_text_content=body)

        sendGridClient = SendGridAPIClient(apiKey)
        response = sendGridClient.send(message)
        logging.info(response)
    except Exception as e:
        logging.error(e.message)