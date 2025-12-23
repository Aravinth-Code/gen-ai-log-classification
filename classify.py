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

