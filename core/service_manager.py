"""
Centralized Service Manager for BharatVerse
Simplified standalone version using session-state storage
"""

import logging
from typing import Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ServiceStatus(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    ERROR = "error"


@dataclass
class ServiceInfo:
    name: str
    status: ServiceStatus
    instance: Optional[Any] = None
    error_message: Optional[str] = None


class ServiceManager:
    """Centralized service management"""

    def __init__(self):
        self._services: Dict[str, ServiceInfo] = {}
        self._initialize_services()

    def _initialize_services(self):
        """Initialize all services with proper error handling"""
        # Session-based storage (always available)
        self._register_service("storage", self._init_session_storage)
        # Cache (simple dict-based)
        self._register_service("cache", self._init_cache)

    def _register_service(self, name: str, init_func):
        """Register a service with its initialization function"""
        try:
            instance = init_func()
            self._services[name] = ServiceInfo(
                name=name,
                status=ServiceStatus.AVAILABLE,
                instance=instance
            )
            logger.info(f"Service '{name}' initialized successfully")
        except Exception as e:
            self._services[name] = ServiceInfo(
                name=name,
                status=ServiceStatus.ERROR,
                error_message=str(e)
            )
            logger.warning(f"Service '{name}' failed to initialize: {e}")

    def get_service(self, name: str) -> Optional[Any]:
        """Get a service instance if available"""
        service_info = self._services.get(name)
        if service_info and service_info.status == ServiceStatus.AVAILABLE:
            return service_info.instance
        return None

    def is_available(self, name: str) -> bool:
        """Check if a service is available"""
        service_info = self._services.get(name)
        return service_info is not None and service_info.status == ServiceStatus.AVAILABLE

    def get_status(self, name: str) -> ServiceStatus:
        """Get service status"""
        service_info = self._services.get(name)
        return service_info.status if service_info else ServiceStatus.UNAVAILABLE

    def get_error(self, name: str) -> Optional[str]:
        """Get service error message"""
        service_info = self._services.get(name)
        return service_info.error_message if service_info else None

    def list_services(self) -> Dict[str, ServiceStatus]:
        """List all services and their status"""
        return {name: info.status for name, info in self._services.items()}

    # Service initialization methods
    def _init_session_storage(self):
        """Initialize session-based storage"""
        return {"type": "session", "status": "active"}

    def _init_cache(self):
        """Initialize simple dict-based cache"""
        return {}


# Global service manager instance
_service_manager = None


def get_service_manager() -> ServiceManager:
    """Get the global service manager instance"""
    global _service_manager
    if _service_manager is None:
        _service_manager = ServiceManager()
    return _service_manager


def get_service(name: str) -> Optional[Any]:
    """Get a service instance"""
    return get_service_manager().get_service(name)


def is_service_available(name: str) -> bool:
    """Check if a service is available"""
    return get_service_manager().is_available(name)
