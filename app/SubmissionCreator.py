from datetime import datetime

from app.Submission import ValidSubmission, InvalidSubmission


class SubmissionCreator:
    @staticmethod
    def create_valid_submission(user, challenge, timestamp=datetime.now()):
        return ValidSubmission(user, challenge, timestamp)

    @staticmethod
    def create_invalid_submission(user, challenge, timestamp=datetime.now()):
        return InvalidSubmission(user, challenge, timestamp)
