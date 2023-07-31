import numpy as np
import pandas as pd


emails = pd.read_csv(".\emails (1).csv")


def process_email(text):
    text = text.lower()
    return list(set(text.split()))


emails['words'] = emails['text'].apply(process_email)


num_email = len(emails)
num_spam = sum(emails['spam'])
print("Number of emails : " , num_email)
print("Number of spams : " , num_spam)

print("Prior Probability is : " , num_spam / (num_email))


#train

model = {}

for index , email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam' : 1 , 'ham' : 1}
        if word in model:
            if email['spam']:
                model[word]['spam'] += 1
            else:
                model[word]['ham'] += 1
    
                
#Particular word can be predicted by bayes    
def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return num_spam_with_word / (num_spam_with_word + num_ham_with_word)



print("Probability sale : " , predict_bayes('sale'))
print("Probability lottery : " , predict_bayes('lottery') )

def predict_naive_bayes(email):
    global num_email , num_spam
    num_ham = num_email - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam'] / num_spam * num_email)
            hams.append(model[word]['ham'] / num_ham * num_email)
    prod_spam = np.compat.long(np.prod(spams) * num_spam)
    prod_ham = np.compat.long(np.prod(hams) * num_ham)
    return prod_spam / (prod_spam + prod_ham)

print("Probability sale : " , predict_naive_bayes('lottery sale'))
            
            
            




    


















