class NaiveBayesClassifier:
    def __init__(self):
        self.spam_word_probabilities = {}
        self.not_spam_word_probabilities = {}

    def train(self, training_data):
        spam_count = 0
        not_spam_count = 0
        spam_word_counts = {}
        not_spam_word_counts = {}

        for subject, label in training_data:
            words = subject.lower().split()
            for word in words:
                if label == 'SPAM':
                    spam_word_counts[word] = spam_word_counts.get(word, 0) + 1
                    spam_count += 1
                else:
                    not_spam_word_counts[word] = not_spam_word_counts.get(word, 0) + 1
                    not_spam_count += 1

        total_words = len(spam_word_counts) + len(not_spam_word_counts)

        for word, count in spam_word_counts.items():
            self.spam_word_probabilities[word] = count / spam_count

        for word, count in not_spam_word_counts.items():
            self.not_spam_word_probabilities[word] = count / not_spam_count

    def predict(self, subject):
        spam_probability = 1.0
        not_spam_probability = 1.0

        for word in subject.lower().split():
            spam_probability *= self.spam_word_probabilities.get(word, 0.01)  # Smoothing
            not_spam_probability *= self.not_spam_word_probabilities.get(word, 0.01)  # Smoothing

        if spam_probability > not_spam_probability:
            return "SPAM"
        else:
            return "NOT SPAM"

def main():
    training_data = []

    while True:
        option = input("Enter 'c' to classify email subject, 't' to add training data, 'p' to predict, or 'quit' to exit: ")
        if option.lower() == 'quit':
            break
        elif option.lower() == 'c':
            email_subject = input("Enter email subject to classify: ")
            classifier = NaiveBayesClassifier()
            classifier.train(training_data)
            prediction = classifier.predict(email_subject)
            print("Prediction:", prediction)
        elif option.lower() == 't':
            subject = input("Enter the email subject: ")
            label = input("Enter the label (SPAM or NOT SPAM): ")
            if label.upper() in ['SPAM', 'NOT SPAM']:
                training_data.append((subject, label.upper()))
                print("Training data updated.")
            else:
                print("Invalid label. Please enter 'SPAM' or 'NOT SPAM'.")
        elif option.lower() == 'p':
            if len(training_data) > 0:
                classifier = NaiveBayesClassifier()
                classifier.train(training_data)
                print("Classifier trained with current training data.")
            else:
                print("No training data available. Please add training data first.")

if __name__ == "__main__":
    main()
