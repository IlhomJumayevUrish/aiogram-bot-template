from aiogram import Dispatcher

from loader import dp
from .admins import AdminFilter
from .privete_chat import IsPriver
from .group_filter import IsGroup


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPriver)
    dp.filters_factory.bind(IsGroup)
