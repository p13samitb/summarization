from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


torch.cuda.empty_cache()

model_name = 'google/pegasus-cnn_dailymail'  ##Change mode if required

device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

def summarization(src_text):
    batch = tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(device)
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    tgt_text = str(tgt_text).replace('<n>',' ')
    return tgt_text