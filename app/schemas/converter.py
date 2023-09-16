from typing import Annotated
from fastapi import Query

class QueryParams:
    def __init__(self,
                 from_: Annotated[str, Query(description="From",
                                             max_length=3,
                                             min_length=3,
                                             alias="from")],
                 to: Annotated[str, Query(description="To",
                                          max_length=3,
                                          min_length=3,)],
                 value: Annotated[int, Query(description="Amount")]):
            self.from_ = from_
            self.to = to
            self.value = value
