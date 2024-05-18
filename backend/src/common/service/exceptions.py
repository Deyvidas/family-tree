class ServiceErrorNotFound(Exception):
    """
    This error is raised when the service should have found one or more
    objects, but has not found anything
    """


class ServiceErrorMoreThanOneFound(Exception):
    """
    This error is raised when the service is supposed to find only one object,
    but found more than one.
    """
