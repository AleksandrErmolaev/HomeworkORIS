import threading
import random

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Condition()

    def withdraw(self, amount, client_id):
        with self.lock:
            while self.balance < amount:
                print(f"Клиент {client_id}: Недостаточно средств на счете. Ожидание...")
                self.lock.wait()
            if self.balance >= amount:
                self.balance -= amount
                print(f"Клиент {client_id}: Снято {amount}. Остаток: {self.balance}")
                self.lock.notify_all()

def client(account, client_id):

    amount_to_withdraw = random.randint(100, 500)
    account.withdraw(amount_to_withdraw, client_id)



if __name__ == "__main__":
    initial_balance = 10000
    num_clients = 5
    account = Account(initial_balance)

    clients = []
    for i in range(num_clients):
        client_thread = threading.Thread(target=client, args=(account, i + 1))
        clients.append(client_thread)
        client_thread.start()

    for client_thread in clients:
        client_thread.join()

    print(f"Окончательный остаток на счете: {account.balance}")