import processor.regex_processor as rp
import processor.bert_processor as bp
import processor.llm_processor as lp

def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels

def classify_log(source, log_msg):
    if source == "LegacyCRM":
        label = lp.classify_with_llm(log_msg)
    else:
        label = rp.classify_with_regex(log_msg)
        if not label:
            label = bp.classify_with_bert(log_msg)
    return label

def classify_csv(input_file):
    import pandas as pd
    df = pd.read_csv(input_file)

    # Perform classification
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

    # Save the modified file
    output_file = r"E:\Projects\gen-ai-log-classification\resources\output.csv"
    df.to_csv(output_file, index=False)

    return output_file

if __name__ == "__main__":

    classify_csv(r"E:\Projects\gen-ai-log-classification\resources\test.csv")

    # test_logs = [
    #     ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
    #     ("OldSystem", "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"),
    #     ("NewApp", "System reboot initiated by user 12345.")
    # ]
    # results = classify(test_logs)
    # for log, label in zip(test_logs, results):
    #     print(f"Log: {log[1]}\nClassified as: {label}\n")
