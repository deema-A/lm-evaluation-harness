output_path="/acegpt_7_chat_results"

lm_eval --model hf \
    --model_args parallelize=FreedomIntelligence/AceGPT-7B-chat \
    --tasks aratrust \
    --batch_size 1 \
    --write_out \