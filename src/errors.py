import logging


class TaskPlannerException(Exception):
    """Base exception for task planner errors."""
    pass


class InvalidGoalError(TaskPlannerException):
    """Raised when goal is invalid or empty."""
    pass


class ConfigurationError(TaskPlannerException):
    """Raised when configuration is invalid."""
    pass


def validate_goal(goal: str) -> bool:
    """Validate that goal is not empty and has minimum length."""
    if not goal or len(goal.strip()) < 3:
        raise InvalidGoalError("Goal must be at least 3 characters long")
    return True


def safe_execute_tool(tool_func, *args, **kwargs):
    """Safely execute a tool with error handling."""
    try:
        result = tool_func(*args, **kwargs)
        return {
            "success": True,
            "result": result,
            "error": None
        }
    except Exception as e:
        # Catch all exceptions, not just TypeError
        return {
            "success": False,
            "result": None,
            "error": f"Error in tool execution: {type(e).__name__} - {str(e)}"
        }


def log_error(error: Exception, context: str = "") -> None:
    """Log an error with context using proper logging."""
    logger = logging.getLogger(__name__)
    error_msg = f"[{context}] {type(error).__name__}: {str(error)}"
    logger.error(error_msg)
