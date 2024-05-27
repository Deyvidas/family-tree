from ..repository import RepositoryInterface


class Service:
    def __init__(
        self,
        repository: RepositoryInterface,
    ):
        self.repository = repository

    pass
