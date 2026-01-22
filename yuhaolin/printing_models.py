def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，
    打印每个设计后，将其移动到列表completed_models
    """
    while unprinted_designs:
        curr_design = unprinted_designs.pop()
        print(f"Printing model: {curr_design}")
        completed_models.append(curr_design)
        
def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone', 'robot', 'dog']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)