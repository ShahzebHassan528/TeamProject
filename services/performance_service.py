from models.evaluation import insert_evaluation

def evaluate_performance(emp_id, score, feedback):
    return insert_evaluation(emp_id, score, feedback)
