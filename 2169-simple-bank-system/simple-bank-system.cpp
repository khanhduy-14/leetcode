
class Bank {
private:
    vector<long long> bankAccounts;
public:
    Bank(vector<long long>& balance): bankAccounts(balance) {

    }
    
    bool transfer(int account1, int account2, long long money) {
        if(!isAccountExists(account1 - 1)) return false;
        if(!isAccountExists(account2 - 1)) return false;
        if (withdraw(account1, money)) {
            deposit(account2, money);
        } else {
            return false;
        }
        
       
        return true;
    }
    
    bool deposit(int account, long long money) {
        if(!isAccountExists(account - 1)) return false;
        bankAccounts[account - 1] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if(!isAccountExists(account - 1)) return false;
        if (bankAccounts[account - 1] < money) {
            return false;
        }
        bankAccounts[account - 1] -=money;
        return true;
    }

    bool isAccountExists(int account) {
        if (account < 0 || account >= bankAccounts.size()) {
            return false;
        }
        return true;
    }

};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */