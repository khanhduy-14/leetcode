class Bank {
private:
    vector<long long> bankAccounts;
public:
    Bank(vector<long long>& balance) : bankAccounts(balance) {}

    bool transfer(int account1, int account2, long long money) {
        if (account1 <= 0 || account2 <= 0 || account1 > bankAccounts.size() || account2 > bankAccounts.size()) 
            return false;
        if (bankAccounts[account1 - 1] < money) 
            return false;
        bankAccounts[account1 - 1] -= money;
        bankAccounts[account2 - 1] += money;
        return true;
    }

    bool deposit(int account, long long money) {
        if (account <= 0 || account > bankAccounts.size()) 
            return false;
        bankAccounts[account - 1] += money;
        return true;
    }

    bool withdraw(int account, long long money) {
        if (account <= 0 || account > bankAccounts.size() || bankAccounts[account - 1] < money)
            return false;
        bankAccounts[account - 1] -= money;
        return true;
    }
};