
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import BartForConditionalGeneration, BartTokenizer
from textsummarizer.entity import ModelTrainerConfig
from datasets import load_dataset, load_from_disk
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        # model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        tokenizer = BartTokenizer.from_pretrained(self.config.model_ckpt)
        model_bart = BartForConditionalGeneration.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_bart)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)



        # trainer_args = TrainingArguments(
        #     output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
        #     per_device_train_batch_size=1, per_device_eval_batch_size=1,
        #     weight_decay=0.01, logging_steps=10,
        #     evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
        #     gradient_accumulation_steps=16
        # ) 
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, 
            num_train_epochs=3,               # More training cycles for better results
            per_device_train_batch_size=1,    # Optimized for 6GB VRAM
            per_device_eval_batch_size=1,     # Keep same batch size for evaluation
            gradient_accumulation_steps=4,    # Reduce memory load
            weight_decay=0.01,                # Standard weight decay
            logging_steps=10,                  # Log progress frequently
            eval_strategy="steps",       # Evaluate every few steps
            eval_steps=500,                    # Evaluate model every 500 steps
            save_steps=2000,                    # Save checkpoint every 2000 steps
            save_total_limit=2,                # Keep only last 2 checkpoints
            fp16=True,                         # Mixed precision training (reduces memory usage)
        ) 

        trainer = Trainer(model=model_bart, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        
        trainer.train()

        ## Save model
        model_bart.save_pretrained(os.path.join(self.config.root_dir,"bart-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))

