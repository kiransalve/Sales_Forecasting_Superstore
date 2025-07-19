import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "<<<< Kiran, Error Occured in python file name [{0}] line number [{1}] error message is [{2}], solve it bro..! >>>>".format(
        file_name,
        exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    # You are inheriting from the built-in Exception class, which comes from Python's builtins module. 
    # This module is automatically available in every Python script, so you don't need to import it explicitly.
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        # It calls the constructor of the parent class (Exception) and passes the error_message to it.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
    

    
        
