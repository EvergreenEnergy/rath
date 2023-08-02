class RathException(Exception):
    """RathException is the base exception for all Rath errors."""

    pass


class NotConnectedError(RathException):
    """NotConnectedError is raised when the Rath is not connected and autoload
    is set to false."""

    pass


class NotEnteredError(RathException):
    """NotEnteredError is raised when the Rath is not entered and access
    to protected methods is attempted."""

    pass
