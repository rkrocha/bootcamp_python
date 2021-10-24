class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if not hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"The Bank"
	def __init__(self):
		self.account = []

	def add(self, account):
		self.account.append(account)

	def transfer(self, origin, dest, amount) -> bool:
		if isinstance(origin, int):
			origin = self.get_account_by_id(origin)
		elif isinstance(origin, str):
			origin = self.get_account_by_name(origin)
		else:
			return False

		if isinstance(dest, int):
			dest = self.get_account_by_id(dest)
		elif isinstance(dest, str):
			dest = self.get_account_by_name(dest)
		else:
			return False

		if (not isinstance(origin, Account)
		or not isinstance(dest, Account)
		or self.is_corrupted(origin)
		or self.is_corrupted(dest)
		or amount <= 0
		or amount > origin.value):
			print('unsafe')
			return False
		origin.value -= amount
		dest.value += amount
		return True

	def fix_account(self, account):
		pass

	def is_corrupted(self, account) -> bool:
		attrs = dir(account)
		if (any(attr.startswith('b') for attr in attrs)
		or not (hasattr(account, 'zip') or hasattr(account, 'addr'))
		or not all(hasattr(account, attr) for attr in ['name', 'id', 'value'])):
			print('corrupt')
			return True
		return False

	def get_account_by_id(self, id: int) -> Account:
		for account in self.account:
			if account.id == id:
				return account
		return None

	def get_account_by_name(self, name: str) -> Account:
		for account in self.account:
			if account.name == name:
				return account
		return None
