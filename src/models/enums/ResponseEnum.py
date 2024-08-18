from enum import Enum

class ResponseSignal(Enum):
    
    FILE_VALIDATION_SUCCESS = "File validation success"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "File size exceeded"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"