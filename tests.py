import requests
import unittest


# Current forms in database
# name: ContactForm, date:date, client_email: email, question: text
# name: RegisterForm, reg_date: date, username: text, phone: phone, user_mail: email
# name: CallBackForm, customer_phone: phone, subject: text, date_to_call: date
# name: CommentForm, nickname: text, user_email: email 
# name: TicketBookingForm, destination: text, \
# contact: phone, second_contact: email, departure_date: date


class FormRetrievalTest(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(FormRetrievalTest, self).__init__(*args, **kwargs)
		self.host = 'http://127.0.0.1:5000'
		self.action = 'get_form'
		self.url = '{}/{}'.format(self.host, self.action)

	def test_correct_form_retrieval(self):
		data = {
			'client_email': 'this.should-work@mail.ru',
			'question': 'some text here',
			'date': '20.10.2017',
		}
		response = requests.post(self.url, data).json()
		self.assertEqual('ContactForm', response['template name'])

	def test_redundant_fields(self):
		data_to_post = {
			'destination': 'Rome',
			'contact': '+7 900 123 12 12',
			'second_contact': 'myemail@mail.ru',
			'departure_date': '21.12.1998',
			'description': 'some text here',
			'user_credentials': 'Ivan Ivanov'
		}
		actual_response = requests.post(self.url, data_to_post).json()
		self.assertEqual('TicketBookingForm', actual_response['template name'])

	def test_incorrect_phone(self):
		data_to_post = {
			'reg_date': '2012-12-31',
			'username': 'Myusername',
			'phone': '+7 123 12 0'
		}
		actual_response = requests.post(self.url, data_to_post).json()
		correct_response = {
			'reg_date': 'date',
			'username': 'text',
			'phone': 'text'
		}
		self.assertEqual(actual_response, correct_response)

	def test_incorrect_date(self):
		data_to_post = {
			'customer_phone': '+7 123 123 12 12',
			'date_to_call': '2012-06-33', # 33rd day
			'subject': 'blabla'
		}
		actual_response = requests.post(self.url, data_to_post).json()
		correct_response = {
			'customer_phone': 'phone',
			'date_to_call': 'text',
			'subject': 'text'
		}
		self.assertEqual(actual_response, correct_response)

	def test_incorrect_email(self):
		data_to_post = {
			'nickname': 'coolguy',
			'user_email': 'testuser@gmailcom' 
		}
		actual_response = requests.post(self.url, data_to_post).json()
		correct_response = {
			'nickname': 'text',
			'user_email': 'text'
		}
		self.assertEqual(actual_response, correct_response)

	def test_too_few_fields(self):
		data_to_post = {
			'phone': '+7 903 777 66 55'
		}

		res = requests.post(self.url, data_to_post).json()
		data = {'phone': 'phone'}
		self.assertEqual(data, res)

	def test_mismatching_field_names(self):
		data_to_post = {
			'first_name': 'Marcus',
			'second_name': 'Tullius',
			'congnomen': 'Cicero',
			'birth_date': '0106-01-03',
			'email': 'marcus-tullius.cicero@gmail.com',
			'cellphone': '+7 903 777 66 55'
		}
		actual_response = requests.post(self.url, data_to_post).json()
		correct_response = {
			'first_name': 'text',
			'second_name': 'text',
			'congnomen': 'text',
			'birth_date': 'date',
			'email': 'email',
			'cellphone': 'phone'
		}
		self.assertEqual(actual_response, correct_response)

if __name__ == '__main__':
    unittest.main(verbosity=2)