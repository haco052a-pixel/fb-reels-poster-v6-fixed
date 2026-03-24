import json

class TokenManager:
    def __init__(self, filename='accounts.json'):
        self.filename = filename
        self.accounts = self.load_accounts()

    def add_account_flow(self, account):
        if account not in self.accounts:
            self.accounts.append(account)
            self.save_accounts()
            return f'Account {account} added successfully.'
        return 'Account already exists.'

    def load_accounts(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_accounts(self):
        with open(self.filename, 'w') as f:
            json.dump(self.accounts, f, indent=4)

    def add_pages(self, account, pages):
        if account in self.accounts:
            for page in pages:
                if page not in self.accounts[account].get('pages', []):
                    self.accounts[account].setdefault('pages', []).append(page)
            self.save_accounts()
            return f'Pages added to {account}.'
        return 'Account not found.'

    def remove_page(self, account, page):
        if account in self.accounts:
            if page in self.accounts[account].get('pages', []):
                self.accounts[account]['pages'].remove(page)
                self.save_accounts()
                return f'Page {page} removed from {account}.'
        return 'Account or page not found.'

# Example usage
if __name__ == '__main__':
    manager = TokenManager()
    print(manager.add_account_flow('user@example.com'))
    print(manager.add_pages('user@example.com', ['Page1', 'Page2']))
    print(manager.remove_page('user@example.com', 'Page1'))