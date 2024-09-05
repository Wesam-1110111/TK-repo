# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
import numpy as np


arr = np.array([2, 2, 7], dtype=int)
print(arr)
#
# # تحميل النموذج والمحول
# model_name = "microsoft/DialoGPT-medium"
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
#
#
# # دالة للحصول على الرد
# def generate_response(user_input):
#     # ترميز الإدخال
#     input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
#     # توليد الرد باستخدام النموذج
#     chat_history_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#     # فك ترميز الرد
#     response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
#     return response
#
#
# # حلقة الدردشة
# print("مرحبا! أنا شات بوت ذكاء اصطناعي. كيف يمكنني مساعدتك؟")
# while True:
#     user_input = input("أنت: ")
#     if user_input.lower() in ["خروج", "إنهاء", "وداعا"]:
#         print("شات بوت: وداعا!")
#         break
#     response = generate_response(user_input)
#     print(f"شات بوت: {response}")
