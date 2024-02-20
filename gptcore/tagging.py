from gpt_utils import get_completion, write_json, json_to_df, tag_reviews
from business_context import business_context
from prompt import PROMPT

class AutoTag():
    def __init__(self,custom_prompt,feedbacks):
        self.custom_prompt = custom_prompt
        self.feedbacks = feedbacks
    def tag_feebacks(self):	
        tagged_responses = []
        if self.feedbacks:
            for i in range(len(self.feedbacks)):
                feedback = self.feedbacks[i]
                prompt_str = self.custom_prompt + feedback 
                try:
                    response = get_completion(prompt_str) 
                    tagged_responses.append(response)
                except Exception as e:
                    print(e)
                    pass
        return tagged_responses
    def write_tagged_responses(self,tagged_responses_file):
        write_json(self.tagged_responses,tagged_responses_file)
    def write_tagged_responses(input_json_path,output_csv_path):
        json_to_df(input_json_path,output_csv_path)
