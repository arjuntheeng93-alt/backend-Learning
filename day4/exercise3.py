class AppException(Exception):  #base class for all application exceptions
    def __init__(self, message: str, status_code: int = 400): #constructor for AppException, takes a message and a status code, default status code is 400
        self.message = message # set the message attribute to the message passed in the constructor
        self.status_code = status_code # set the status_code attribute to the status code passed in the constructor
        super().__init__(self.message)# call the constructor of the base Exception class with the message, this allows us to use the built-in exception handling features of Python while still providing our own custom message and status code for our application exceptions
        
class NotFoundError(AppException):# subclass of AppException for not found errors
    def __init__(self, resource: str, resource_id: int): #constructor for NotFoundError, takes a resource name and a resource id, constructs a message using these parameters and sets the status code to 404
        super().__init__(f"{resource} with ID {resource_id} not found", 404) #call the constructor of the base AppException class with a message that indicates which resource was not found and its id, and set the status code to 404 (Not Found)
        
class ValidationError(AppException):# subclass of AppException for validation errors
    def __init__(self, message: str):#constructor for ValidationError, takes a message and sets the status code to 422
        super().__init__(message=message, status_code=422)# call the constructor of the base AppException class with the message passed in the constructor and set the status code to 422 (Unprocessable Entity)
        

try:
    raise NotFoundError("MenuItem", 42)# raise a NotFoundError with resource "MenuItem" and id 42, should have a message indicating that the MenuItem with ID 42 was not found and a status code of 404
except AppException as e:# catch the AppException, which will also catch NotFoundError since it is a subclass of AppException
    print(f"status: {e.status_code}")# print the status code of the exception, which should be 404 for NotFoundError
    print(f"message: {e.message}")# print the message of the exception, which should indicate that the MenuItem with ID 42 was not found