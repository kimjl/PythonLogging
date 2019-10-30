import logging

#Increasing level of severity
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

#All events at or above DEBUG level will now get logged
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

#Log to a file named app.log
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

#Formating your log output
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is a Warning')

#Formating output with date/time
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

#Formating date/time with datefmt
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

#Logging variable data
# name = 'John'
# logging.error('%s raised an error', name)
# logging.error(f'{name} raised an error')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  # logging.error("Exception occurred", exc_info=True)
  logging.exception("Exception occurred")
