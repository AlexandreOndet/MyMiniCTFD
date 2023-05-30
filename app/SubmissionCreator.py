from datetime import datetime

from app.Submission import ValidSubmission, InvalidSubmission, DuplicatedSubmission


class SubmissionCreator:
    @staticmethod
    def create_valid_submission(userId, challenge, timestamp=datetime.now()):
        return ValidSubmission(userId, challenge, timestamp)

    @staticmethod
    def create_invalid_submission(userId, challenge, timestamp=datetime.now()):
        return InvalidSubmission(userId, challenge, timestamp)
    
    @staticmethod
    def create_duplicated_submission(userId, challenge, timestamp=datetime.now()):
        return DuplicatedSubmission(userId, challenge, timestamp)
