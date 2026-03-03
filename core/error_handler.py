"""
Simplified Error Handling for BharatVerse
Provides consistent error handling across the application
"""

import streamlit as st
import logging
from typing import Any
from functools import wraps
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class BharatVerseError(Exception):
    """Base exception for BharatVerse"""


class ServiceUnavailableError(BharatVerseError):
    """Raised when a required service is unavailable"""


class ConfigurationError(BharatVerseError):
    """Raised when configuration is invalid"""


def handle_errors(
    fallback_value: Any = None,
    show_error: bool = True,
    error_message: str = None,
    log_error: bool = True
):
    """Decorator for consistent error handling"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if log_error:
                    logger.error(f"Error in {func.__name__}: {e}")
                if show_error:
                    display_message = error_message or f"Error in {func.__name__}: {str(e)}"
                    st.error(display_message)
                return fallback_value
        return wrapper
    return decorator


@contextmanager
def error_boundary(
    error_message: str = "An error occurred",
    show_error: bool = True,
    log_error: bool = True
):
    """Context manager for error boundaries"""
    try:
        yield
    except Exception as e:
        if log_error:
            logger.error(f"Error in boundary: {e}")
        if show_error:
            st.error(f"{error_message}: {str(e)}")


def safe_import(module_name: str, fallback=None):
    """Safely import a module with fallback"""
    try:
        parts = module_name.split('.')
        module = __import__(module_name)
        for part in parts[1:]:
            module = getattr(module, part)
        return module
    except ImportError as e:
        logger.warning(f"Failed to import {module_name}: {e}")
        return fallback


# Common error messages
ERROR_MESSAGES = {
    "auth_required": "🔒 Authentication required to access this feature",
    "admin_required": "👑 Admin privileges required",
    "service_unavailable": "🚫 This service is currently unavailable",
    "configuration_error": "⚙️ Configuration error - please check your settings",
    "network_error": "🌐 Network error - please check your connection",
    "file_error": "📁 File operation failed",
    "database_error": "🗄️ Database operation failed",
}


def show_error_message(error_type: str, details: str = None):
    """Show standardized error message"""
    message = ERROR_MESSAGES.get(error_type, "❌ An error occurred")
    st.error(message)
    if details:
        with st.expander("🔍 Error Details"):
            st.code(details)
