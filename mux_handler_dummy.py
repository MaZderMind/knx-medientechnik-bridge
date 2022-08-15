from dummy_input import dummy_input_handler
from mux_handler import MuxHandler


class MuxHandlerDummy(MuxHandler):
    def __init__(self, system_key, conf):
        super().__init__(system_key, conf)
        self.input_key = None
        for input_key in self.inputs.keys():
            dummy_input_handler().register_dummy_mux_callback(system_key, input_key, self.externally_set_input)

    async def select_input(self, input_key: str):
        self.log.info(f'Switching to {input_key}')
        self.input_key = input_key

    async def get_current_input(self) -> str:
        return self.input_key

    def externally_set_input(self, new_input_key):
        self.log.info(f'Externally set to {new_input_key}')
        self.input_key = new_input_key
