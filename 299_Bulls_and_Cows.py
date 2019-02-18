class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        # Solution 1:
        obssecret = dict()
        for sec in secret:
            obssecret[sec] = obssecret.get(sec, 0) + 1
        
        num_a = 0
        num_b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_a += 1
                obssecret[guess[i]] = obssecret.get(guess[i]) - 1
            elif obssecret.get(guess[i]):
                num_b += 1
                obssecret[guess[i]] = obssecret.get(guess[i]) - 1
        num_b += sum(x for x in obssecret.values() if x < 0)
        return '{0}A{1}B'.format(num_a, num_b)
    
        # Solution 2:
        # Simple Solution
        bulls = sum(map(operator.eq, secret, guess))
        boths = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        
        return '{0}A{1}B'.format(bulls, boths - bulls)