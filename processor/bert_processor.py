from sentence_transformers import SentenceTransformer
import joblib

# Load the pre-trained BERT model and classifier
bert_model = SentenceTransformer('all-MiniLM-L6-v2')
classifier = joblib.load(r'E:\Projects\gen-ai-log-classification\models\logistic_regression_model.joblib')

def classify_with_bert(log_message):

    # Encode the log message using BERT
    embedding = bert_model.encode([log_message])

    probalities = classifier.predict_proba(embedding)

    if probalities.max() < 0.7:
        return "Unclassified"
    # Predict the class label using the classifier
    predicted_label = classifier.predict(embedding)
    return predicted_label[0]

if __name__ == "__main__":
    test_logs = [
        "User User123 logged in.",
        "Backup started at 2024-06-01 10:00:00.",
        "System updated to version 2.1.0.",
        "File report.pdf uploaded successfully by user Alice.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user Admin.",
        "Account with ID 456 created by Bob."
    ]
    for test_log in test_logs:
        classification = classify_with_bert(test_log)
        print(f"Log: '{test_log}' => Classification: '{classification}'")