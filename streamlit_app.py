pip install openai
import openai 
  
openai.api_key = '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' 
 
 
def get_api_response(prompt: str) -> str | None: 
 
    try: 
        response: dict = openai.Completion.create( 
            model='text-davinci-003', 
            prompt=prompt, 
            temperature=0.9,#the randomness of the each response 
            max_tokens=200, 
            top_p=1,#alt to temp 
            frequency_penalty=0,#how often it repeats its verbatim 
            presence_penalty=0.6,#how often will it use a new topic 
 
        ) 
 
        # choices: dict = response.get('choices')[0] 
        # text = choices.get('text'); OR 
 
        text = (response.get('choices')[0]).get('text') 
        # print(response) #json file with api response 
 
    except Exception as e: 
        print('ERROR:', e) 
 
    return text; 
 
#saves context from ai and user chat to a list 
def update_list(message: str, promptList : list[str]): 
    promptList.append(message) 
 
def create_prompt(message: str, promptList : list[str])->str: 
    process_msg :str = f'\nUser: {message}' 
    update_list(process_msg, promptList) 
    prompt: str = ''.join(promptList) 
 
    return prompt 
 
def get_bot_response(message: str, promptList : list[str])->str: 
    prompt:str = create_prompt(message, promptList); 
    bot_response:str = get_api_response(prompt); 
 
    if(bot_response): 
        update_list(bot_response, promptList) 
        pos = bot_response.find(' Zola:') 
        # print(pos) 
        bot_response = bot_response[pos + 7:] 
    else: 
        bot_response = "Error" 
 
    return bot_response 
 
def main(): 
    prompt_list: list[str] = ['You will pretend to be Arnim Zola, who talks in a cocky and condescending manner, but is up to date with todays world'] 
 
    while(1): 
        user:str = input('User: ') 
        response: str = get_bot_response(user, prompt_list) 
 
 
        print(f'\nZOLA: {response}') 
        # print(prompt_list) 
 
 
if _name=='__main_': 
    main()
