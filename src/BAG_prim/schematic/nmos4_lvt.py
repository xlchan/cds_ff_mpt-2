# -*- coding: utf-8 -*-

from typing import Any


from bag.design.module import MosModuleBase
from bag.design.database import ModuleDB
from bag.util.immutable import Param


# noinspection PyPep8Naming
class BAG_prim__nmos4_lvt(MosModuleBase):
    """design module for BAG_prim__nmos4_lvt.
    """

    def __init__(self, database: ModuleDB, params: Param, **kwargs: Any) -> None:
        MosModuleBase.__init__(self, '', database, params, **kwargs)

