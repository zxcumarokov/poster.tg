from _typeshed import Incomplete
from telebot.asyncio_storage.base_storage import StateContext as StateContext, StateStorageBase as StateStorageBase

class StatePickleStorage(StateStorageBase):
    file_path: Incomplete
    data: Incomplete
    def __init__(self, file_path: str = './.state-save/states.pkl') -> None: ...
    async def convert_old_to_new(self) -> None: ...
    def create_dir(self) -> None: ...
    def read(self): ...
    def update_data(self) -> None: ...
    async def set_state(self, chat_id, user_id, state): ...
    async def delete_state(self, chat_id, user_id): ...
    async def get_state(self, chat_id, user_id): ...
    async def get_data(self, chat_id, user_id): ...
    async def reset_data(self, chat_id, user_id): ...
    async def set_data(self, chat_id, user_id, key, value): ...
    def get_interactive_data(self, chat_id, user_id): ...
    async def save(self, chat_id, user_id, data) -> None: ...
