from mux_handler_debug import MuxHandlerDebug
from mux_handler_dummy import MuxHandlerDummy
from mux_handler_zeevee import MuxHandlerZeeVee
from power_handler_debug import PowerHandlerDebug
from power_handler_dummy import PowerHandlerDummy
from power_handler_pjlink import PowerHandlerPJLink
from power_handler_tasmota import PowerHandlerTasmota

POWER_HANDLERS = {
    'dummy': PowerHandlerDummy,
    'debug': PowerHandlerDebug,
    'pjlink': PowerHandlerPJLink,
    'tasmota': PowerHandlerTasmota,
}

MUX_HANDLERS = {
    'dummy': MuxHandlerDummy,
    'debug': MuxHandlerDebug,
    'zeevee': MuxHandlerZeeVee,
}
