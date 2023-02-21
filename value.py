id_user = None
input_data = None
result = None

def get_id_user(num_id):
    global id_user
    id_user = num_id

def get_input_data(data):
    global input_data
    input_data = data
    
def get_result(rslt):
    global result
    result = rslt
    
def save_val():
    with open('data_file.txt', 'a', encoding ='utf-8') as file:
        file.writelines(f'Пользователь: {id_user}, Начальные данные: {input_data}, Результат: {result}\n')